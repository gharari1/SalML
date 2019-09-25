import os
import urllib.request
import json
import base64
import sys
from urllib.request import HTTPError
import logging
import pandas as pd

'''
*************************
Thanks to Dana Rapoport
for contributing to
the code.
*************************
'''


# You must have a valid API Token
API_TOKEN =''
SERVER_ADDRESS = 'http://enterobase.warwick.ac.uk'
SEROTYPE = 'Typhi'
DATABASE = 'senterica'
filename_out= "Enterobase.xlsx"


def __create_request(request_str):
    request = urllib.request.Request(request_str)
    base64string = base64.encodestring(('%s:%s' % (API_TOKEN,'')).encode('UTF-8')).decode('ascii').replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    return request

address_human= SERVER_ADDRESS+'/api/v2.0/%s/straindata?serotype=%s&only_fields=strain_name&only_fields=source_type&only_fields=source_details&only_fields=download_fasta_link&assembly_status=Assembled&source_type=Human&limit=%d' %(DATABASE, SEROTYPE, 224)
response = urllib.request.urlopen(__create_request(address_human))
data = json.load(response)

enterobase_human = pd.DataFrame.from_dict(data['straindata'],orient='index')

address_poultry= SERVER_ADDRESS+'/api/v2.0/senterica/straindata?offset=0&only_fields=strain_name&only_fields=source_type&only_fields=source_details&only_fields=download_fasta_link&source_details=poultry%2Cchicken%2Cpoultry%20tissue%3B%20Gallus%20gallus%2CComminuted%20poultry%2CGallus%20gallus%3B%20poultry&sortorder=asc&orderby=source_details&assembly_status=Assembled&source_type=Avian&limit=2500'

response = urllib.request.urlopen(__create_request(address_poultry))
data = json.load(response)

enterobase_poultry = pd.DataFrame.from_dict(data['straindata'],orient='index')

enterobase = pd.concat([enterobase_poultry, enterobase_human])


cols = enterobase.columns.tolist()
cols = [cols[4] , cols[3] , cols[2] , cols[1]]
enterobase = enterobase[cols]
enterobase.index = list(range(len(enterobase.index.tolist())+1))[1:]
enterobase.to_excel(filename_out)




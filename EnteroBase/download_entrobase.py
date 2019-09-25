import pandas as pd
import urllib.request
import base64
import json


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

in_path= "Enterobase.xlsx"
out_path="Enterobase Genomes\\"


def __create_request(request_str):
    request = urllib.request.Request(request_str)
    base64string = base64.encodestring(('%s:%s' % (API_TOKEN,'')).encode('UTF-8')).decode('ascii').replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    return request

df= pd.read_excel(in_path,index_col=0)

for i in range(len(df['strain_barcode'])):
    response = urllib.request.urlopen(__create_request(df.iloc[i,3]))
    with open(out_path + '%s.fasta' %df.iloc[i,0],'wb') as out_ass:
        out_ass.write(response.read())

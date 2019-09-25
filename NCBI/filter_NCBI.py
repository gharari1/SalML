'''
*************************
Thanks to Dana Rapoport
for the code.
*************************
'''

import pandas as pd
#load NCBI data from file
filename_in= "NCBI_unfiltered.csv"
filename_out= "NCBI_filtered.xlsx"
ncbi = pd.DataFrame.from_csv(filename_in,  encoding='utf-8', index_col=None)
#Add 'Human' & 'Poultry' True/False columns
ncbi['Human']=ncbi['#Organism/Name'].apply(lambda x: any(substring in x for substring in ['Typhi ','Paratyphi A']))
ncbi['Poultry']=ncbi['#Organism/Name'].apply(lambda x: any(substring in x for substring in ['Pullorum','Gallinarum']))
#filter data
ncbi = ncbi[(ncbi.Human == True) | (ncbi.Poultry == True)]
#save data
ncbi.to_excel(filename_out)

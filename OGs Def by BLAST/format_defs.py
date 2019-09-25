import csv
import pandas as pd
import numpy as np

d = {}

with open('ogs_def.csv', 'r', newline='') as og_f:
    r = csv.reader(og_f, delimiter=',')
    for row in r:
        d[int(row[0])] = row[1]
        

selected_ogs = pd.read_excel('selected_ogs.xlsx', header = None)

for i in range(selected_ogs.shape[0]):
    for j in range(1, selected_ogs.shape[1]):
        if np.isnan(selected_ogs.loc[i,j]):
            break
        selected_ogs.loc[i,j] = d[selected_ogs.loc[i,j]]


selected_ogs.to_excel('selected_ogs_def.xlsx', header = False, index = False) 

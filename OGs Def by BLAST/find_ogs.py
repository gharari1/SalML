import numpy as np
import pandas as pd
import csv

X_new_df = pd.read_excel('X_new.xlsx')

X_new = np.array(X_new_df)

## Import ML Data
fn_g = 'phyletic_pattern.fas.txt'


data = np.loadtxt(fn_g,str)

g_id = data[::2]
for i in range(len(g_id)):
    g_id[i] = g_id[i].strip('>')

g_data = data[1::2]


X_ = np.empty([len(g_data),len(g_data[0])],int)

for i in range(len(g_data)):
    X_[i] = list(g_data[i])


X, ind, inv, con = np.unique(X_, axis=1, return_index=True, return_inverse=True, return_counts=True)

def find_gene(M1,M2):
    m1 = np.transpose(M1)
    m2 = np.transpose(M2)
    l=[]
    for i in range(m1.shape[0]):
        l.append(np.argwhere(np.all((m2-m1[i])==0,axis=1)).tolist()[0])
        # Credit: CT Zhu
        # https://stackoverflow.com/a/19228714
    return l

m_og = find_gene(X_new,X_)
m_og.sort()

og_dict = {}

for i in m_og:
    og_dict[i[0]] = np.argwhere(inv[i[0]]==inv).flatten()


df = pd.DataFrame()
ind = 1
for key in og_dict.keys():
    name = pd.DataFrame(['Group #'+str(ind)])
    data = pd.DataFrame(og_dict[key])
    data = data.transpose()
    ser = pd.concat([name, data], axis = 1)
    ser.columns = range(0,ser.shape[1])
    df = pd.concat([df, ser])
    ind += 1


df.to_excel('selected_ogs.xlsx', header = False, index = False) 

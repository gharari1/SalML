'''
*************************
Thanks to Naama Wagner
for contributing to
the code.
*************************
'''

import pandas as pd
import csv
import numpy as np

from hunga_bunga import HungaBungaClassifier, HungaBungaRegressor

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel



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


fn_d = 'Enterobase.xlsx'

WS = pd.read_excel(fn_d)

sb = WS['strain_barcode']
st = WS['source_type']

y_ = []

for i in range(len(g_id)):
    g_id[i] = g_id[i].strip('>')
    y_.append(st[g_id[i]==sb].ravel()[0])
    
y = np.array(y_)

y[y=='Human'] = 0
y[y=='Avian'] = 1
y=y.astype('int')

## Filter Features
clf = ExtraTreesClassifier(n_estimators=50)
clf = clf.fit(X, y)
clf.feature_importances_ 
selectmodel = SelectFromModel(clf, prefit=True)
X_new = selectmodel.transform(X)

## Hunga Bunga
clf = HungaBungaClassifier()
clf.fit(X_new, y)

import csv

d = {}

with open('ogs_def_old.csv', 'r', newline='') as og_f:
    r = csv.reader(og_f, delimiter=',')
    for row in r:
        if "\n" in row[1]:
            d[int(row[0])] = '-'
        else:
            d[int(row[0])] = row[1]
        
with open('ogs_def.csv', 'w', newline = '') as f:
    w = csv.writer(f)
    for key in d.keys():
        w.writerow([key,str(d[key])])

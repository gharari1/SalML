from Bio import SeqIO
from Bio.Blast import NCBIWWW
import pandas as pd
import numpy as np
import csv

ogs_fp = "OGs AA\\" 

selected_ogs = pd.read_excel('selected_ogs.xlsx', header = None)

og_srt = []
og_fin = []
og_fil = []

for i in range(selected_ogs.shape[0]):
    for j in range(1, selected_ogs.shape[1]):
        og = selected_ogs.loc[i,j]
        if np.isnan(og):
            break
        og = int(og)
        og_srt.append(og)
        for seq_record in SeqIO.parse(ogs_fp+'og_'+str(og)+'_aa.fas', "fasta"):
            seq = seq_record
            break
        try:
            result_handle = NCBIWWW.qblast("blastp","refseq_protein",seq, hitlist_size = 1, entrez_query='Salmonella[Organism]')
            s = result_handle.read()
            og_def = s[s.find('<Hit_def>')+9:s.find('</Hit_def>')]
            og_fin.append(og)
        except:
            og_def = '-'
            og_fil.append(og)
        with open('ogs_def.csv', 'a', newline='') as og_f:
            w = csv.writer(og_f)
            w.writerow([str(og),og_def])

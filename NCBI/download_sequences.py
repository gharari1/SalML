import ftplib
import pandas as pd

in_path="NCBI_filtered.xlsx"
out_path="Compressed Genomes\\"

df= pd.read_excel(in_path,index_col=0)
num_genomes=len(df)
successful_download=[]


def get_file_from_ftp(path_to_ftp):
    try:
        ftp = ftplib.FTP("ftp.ncbi.nlm.nih.gov")
        ftp.login()
        path_to_ftp = path_to_ftp.split("ftp.ncbi.nlm.nih.gov")[-1]
        filename = path_to_ftp.split("/")[-1] + "_cds_from_genomic.fna.gz"
        ftp.cwd(path_to_ftp)
        ftp.retrbinary("RETR " + filename, open(out_path + filename, 'wb').write)
        ftp.quit()
        successful_download.append(True)
    except ftplib.error_perm:
        successful_download.append(False)

for i in range(num_genomes):
    get_file_from_ftp(df.iloc[i,18])
    print (i,successful_download[i])
df['Successful Download']=successful_download
df.to_excel(in_path)


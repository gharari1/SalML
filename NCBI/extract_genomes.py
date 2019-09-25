import os
import gzip

in_path="Compressed Genomes\\"
out_path="Uncompressed Genomes\\"

file_list=os.listdir(in_path)

for path in file_list:
    print (file_list.index(path))
    input=gzip.GzipFile(in_path+path,'rb')
    contents=input.read()
    input.close()
    if len(contents)==0:
        continue
    output=open(out_path+path[:-3],'wb')
    output.write(contents)
    output.close()

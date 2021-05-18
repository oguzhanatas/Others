'this code finds lines you are looking for in the irregular files'
import pandas as pd
import numpy as np
from glob import glob

####irregular files for getting lines
datas=glob('data/readLines*')

####find lines in the files and save found lines
'I use some words (keV and nH) to find in the irregular files'
for i in datas:
    f=open('data_output/'+i[5:-4]+'_out.txt','w')
    searchfile = open(i, "r")
    for line in searchfile:
        if "keV" in line: 
            f.write(line+'\n')
        elif "nH" in line:
            f.write(line+'\n')
    f.close()
    searchfile.close()

####read saved output
datas_fix=glob('data_output/readLines*')

for i in datas_fix:
    d=pd.read_csv(i,header=None,sep='\s+',usecols=[5,6])
    print(d)
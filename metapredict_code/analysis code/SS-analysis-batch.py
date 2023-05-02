import os 
import scipy
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

'''
This part is getting the file names in the current folder. 
current folder is where this code at.
'''

path = os.path.abspath(os.path.dirname(__file__))
data_name = os.listdir(path)
file = []
for k in range(len(data_name)):
    name = data_name[k]
    if name[0:5] != 'total' and name[0:5] !='SS010' and name[0:5] !='AA010' and name[-3:] == 'csv':  
        # get the code with end .out and start with MT could change to any you want.
        file.append(name[:-4])

out_path = path + '/' + 'total-SS-resluts.csv'
with open(out_path,'w+') as data_name_meta:
    for j in range(len(file)):
        data_name = file[j] + '.csv'
        data_path = path + '/' +  data_name
        # print(data_path)
        df=pd.read_csv(data_path,header=None,names=["name","PLDDT","MT-Pre","ss"],sep ='\s+')
        r2_p = float("%.3f"%scipy.stats.pearsonr(df['MT-Pre'], df['PLDDT'], alternative = 'two-sided')[0])
        print(file[j],r2_p,file=data_name_meta)

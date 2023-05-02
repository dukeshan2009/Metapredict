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
r2_batch = []
for i in range(0,11): 
    folder_path = path + '/' + str(i)
    data_name = os.listdir(folder_path)
    file = []
    for k in range(len(data_name)):
        name = data_name[k]
        if name[0:5] != 'total' and name[0:5] !='SS010' and name[0:5] !='AA010' and name[-3:] == 'csv':  
            # get the code with end .out and start with MT could change to any you want.
            file.append(name[:-4])
    r2_total = []
    # PLDDT_total = []
    # MT_total = []
    for j in range(len(file)):
        data_name = file[j] + '.csv'
        data_path = folder_path + '/' +  data_name
        # print(data_path)
        df=pd.read_csv(data_path,header=None,names=["name","PLDDT","MT-Pre","ss"],sep ='\s+')
        r2_p = float("%.3f"%scipy.stats.pearsonr(df['MT-Pre'], df['PLDDT'], alternative = 'two-sided')[0])
        r2_total.append(r2_p)
    r2_batch.append(r2_total)


test=pd.DataFrame(columns=file,data=r2_batch)
out_path = path + '/' + 'SS010_resluts.csv'
test.to_csv(out_path,encoding='utf-8')


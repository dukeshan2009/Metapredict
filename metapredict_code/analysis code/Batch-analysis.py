import os 
import scipy
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

'''
This part is getting the file names in the current folder. 
current folder is where this code at.
'''

path = os.path.abspath(os.path.dirname(__file__))   # 当前文件夹目录

PLDDT_Batch = []
MT_Batch = []
r2_Batch = []
for i in range(1,21): 
    file_path = path + '/' + 'out-data-' + str(i) 
    data_name = os.listdir(file_path)
    file = []
    for k in range(len(data_name)):
        name = data_name[k]
        if name[0:2] == 'MT' and name[-3:] == 'out':  
            # get the code with end .out and start with MT could change to any you want.
            file.append(name[:-4])
    r2_total = []
    PLDDT_total = []
    MT_total = []
    for j in range(len(file)):
        data_name = file[j] + '.out'
        data_path = file_path + '/' +  data_name
        # print(data_path)
        df=pd.read_csv(data_path,header=None,names=["name","PLDDT","MT-Pre","ss","MSE","MAE"],sep ='\s+')
        r2_p = float("%.3f"%scipy.stats.pearsonr(df['MT-Pre'], df['PLDDT'], alternative = 'two-sided')[0])
        r2_total.append(r2_p)
        PLDDT_total.extend(df['PLDDT'])
        MT_total.extend(df['MT-Pre'])
    PLDDT_Batch.extend(PLDDT_total)
    MT_Batch.extend(MT_total)
    r2_Batch.extend(r2_total)

r2_low, r2_0 , r2_1 , r2_2, r2_3, r2_4, r2_5, r2_6, r2_7, r2_8, r2_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for m in range(len(r2_Batch)):
    r2_count = 0
    r2_count = r2_Batch[m] / 0.1 
    if r2_count <0 : 
        r2_low = r2_low + 1 
    elif r2_count > 0 and r2_count <= 1: 
        r2_0 = r2_0 + 1 
    elif r2_count > 1 and r2_count <= 2: 
        r2_1 = r2_1 + 1 
    elif r2_count > 2 and r2_count <= 3: 
        r2_2 = r2_2 + 1 
    elif r2_count > 3 and r2_count <= 4: 
        r2_3 = r2_3 + 1 
    elif r2_count > 4 and r2_count <= 5: 
        r2_4 = r2_4 + 1 
    elif r2_count > 5 and r2_count <= 6: 
        r2_5 = r2_5 + 1 
    elif r2_count > 6 and r2_count <= 7: 
        r2_6 = r2_6 + 1 
    elif r2_count > 7 and r2_count <= 8: 
        r2_7 = r2_7 + 1 
    elif r2_count > 8 and r2_count <= 9: 
        r2_8 = r2_8 + 1 
    elif r2_count > 9 :  
        r2_9 = r2_9 + 1 

name_list = ['r2_low', 'r2_0' , 'r2_1' , 'r2_2', 'r2_3', 'r2_4', 'r2_5', 'r2_6', 'r2_7', 'r2_8', 'r2_9']
results_list = [r2_low, r2_0 , r2_1 , r2_2, r2_3, r2_4, r2_5, r2_6, r2_7, r2_8, r2_9]
r2_ave_batch = np.mean(r2_Batch)
# r2 results counting plot 
r2_batch_p = float(scipy.stats.pearsonr(MT_Batch, PLDDT_Batch, alternative = 'two-sided')[0])
for (a, b) in zip(name_list, results_list):
       plt.text(b, a, str(b))
plt.barh(name_list, results_list)

plt.title('Counting for r2_value for each protein in ' + path.split('/')[-2], fontsize = 15)
plt.legend(loc='best',title= 'total residue r2_value = ' +str("%.3f"%r2_batch_p) + '\n' 
           +'Ave r2_value = ' + str("%.3f"%r2_ave_batch) + '\n'
           + 'Protien_numeber = ' + str(len(r2_Batch)), 
           fontsize=10)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.savefig(path + '/' +'whole_' + path.split('/')[-2] + '_r2-ave = ' + str("%.3f"%r2_ave_batch) + ' _couting_results.png')

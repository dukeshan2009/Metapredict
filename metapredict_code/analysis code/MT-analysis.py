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
    if name[0:2] == 'MT' and name[-3:] == 'out':  
        # get the code with end .out and start with MT could change to any you want.
        file.append(name[:-4])
r2_total = []
PLDDT_total = []
MT_total = []
for j in range(len(file)):
    data_name = file[j] + '.out'
    data_path = path + '/' +  data_name
     # print(data_path)
    df=pd.read_csv(data_path,header=None,names=["name","PLDDT","MT-Pre","ss","MSE","MAE"],sep ='\s+')
    r2_p = float("%.3f"%scipy.stats.pearsonr(df['MT-Pre'], df['PLDDT'], alternative = 'two-sided')[0])
    r2_total.append(r2_p)
    PLDDT_total.extend(df['PLDDT'])
    MT_total.extend(df['MT-Pre'])

r2_low, r2_0 , r2_1 , r2_2, r2_3, r2_4, r2_5, r2_6, r2_7, r2_8, r2_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for m in range(len(r2_total)):
    r2_count = 0
    r2_count = r2_total[m] / 0.1 
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
r2_ave = np.mean(r2_total)
# r2 results counting plot 
r2_batch = float(scipy.stats.pearsonr(MT_total, PLDDT_total, alternative = 'two-sided')[0])
for (a, b) in zip(name_list, results_list):
    plt.text(b, a, str(b))
plt.barh(name_list, results_list)

if path.split('/')[-1][-1] == '0' and path.split('/')[-1][-2] == '1':
    plt.title('r2_value for residue length over 1000', fontsize = 15)
else: 
    plt.title('r2_value for residue length in range (' + str(int(path.split('/')[-1][-1])*100) + 
              '~' + str((int(path.split('/')[-1][-1])+1)*100) + ')' , fontsize = 15)

plt.legend(loc='best',title= 'total residue r2_value = ' +str("%.3f"%r2_batch) + '\n' 
        +'Ave r2_value = ' + str("%.3f"%r2_ave) + '\n'
        + 'Protien_numeber = ' + str(len(r2_total)), 
        fontsize=10)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.savefig(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/' + path.split('/')[-1] + '_r2_ave = ' + str("%.3f"%r2_ave) + '_couting_results.png')
plt.clf()


out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/' + path.split('/')[-1] + '-resluts.csv'
with open(out_path,'w+') as data_name_meta:
    print(str(int(path.split('/')[-1][-1])*100) 
          + '~' + 
          str((int(path.split('/')[-1][-1])+1)*100),
          r2_batch,r2_ave, str(len(r2_total)),file=data_name_meta)
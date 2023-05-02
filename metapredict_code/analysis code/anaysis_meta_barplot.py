import numpy as np 
import pandas as pd
import os 
import sys
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

'''
This part is getting the file names in the current folder. 
current folder is where this code at.
'''
path = os.path.abspath(os.path.dirname(__file__))
data_name = os.listdir(path)
# print(path.split('\\')[-1] )
# print(data_name)
file = []
for i in range(len(data_name)):
    name = data_name[i]
    if name[0:2] == 'MT' and name[-3:] == 'out':  
        # get the code with end .out and start with MT could change to any you want.
        file.append(name[:-4])

# In the MT*.out files, we have PLDDT and MT-Pre PLDDT. 
# Use sklearn r2_score package to get r2 results. 
# This part is to grap all r2 results in the folder. 

r2_total = []
for k in range(len(file)):
    data_name = file[k] + '.out'
    data_path = path + '/' +  data_name
    # print(data_path)
    df=pd.read_csv(data_path,header=None,names=["name","PLDDT","MT-Pre","ss","MSE","MAE"],sep ='\s+')
    x_axis = list(range(1,len(df['PLDDT'])+1))
    r2 = r2_score(df['PLDDT'], df['MT-Pre'],multioutput='variance_weighted', force_finite=False)
    r2_total.append(r2)

# print(r2_total)
# analysis r2 results
# give the count of each 10% into bar plot. 

r2_low, r2_0 , r2_1 , r2_2, r2_3, r2_4, r2_5, r2_6, r2_7, r2_8, r2_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for n in range(len(r2_total)):
    r2_count = 0
    r2_count = r2_total[n] / 0.1 
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

plt.barh(name_list, results_list)
plt.savefig(os.path.dirname(__file__) + '/' + path.split('/')[-1] + '_results_r2.png')

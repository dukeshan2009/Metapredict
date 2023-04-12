import os
import numpy as np 
import glob 
import argparse
from Bio.PDB import PDBParser
import metapredict as meta
import pandas as pd
from sklearn import metrics

path = os.path.abspath(os.path.dirname(__file__))
data_name = os.listdir(path)
print(data_name)
file = []
for i in range(len(data_name)):
    # print(i)
    # print(data_name[i])
    name = data_name[i]
    # print(name[-3:])
    # print(name[:2])

    if name[-3:] == 'out' and name[0:2] == 'AF':
        file.append(name[:-4])
    

for i in range(len(file)):
    data_name = file[i] + '.out'
    data_name_1 = 'MT-' + file[i] + '.out'
    out_path = path + '/' +  data_name_1
    data_path = path + '/' +  data_name
    with open(out_path,'w+') as data_name_meta:
        with open (data_path, 'r') as p_file: 
            protein_data = p_file.readlines()
            res = []
            plddt = []
            ss = []
            for j in protein_data: 
                res.append(j[0:3])
                plddt.append(j[4:-3])
                ss.append(j[-2])
            dictn = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
                    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
                    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
                    'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
            amino_acid = [dictn[triple] for triple in res]
            protein_seq = "".join(amino_acid)
            print(protein_seq)
            print(len(protein_seq))
            # print(data_name)
            
            metapredict_result = meta.predict_pLDDT(protein_seq)
            meta_array=np.array(metapredict_result, dtype = float )[:,np.newaxis]
            af_array=np.array(plddt, dtype = float )[:,np.newaxis]

            for k in range(len(res)):
                MSE = metrics.mean_squared_error(af_array[k], meta_array[k])
                MAE = metrics.mean_absolute_error(af_array[k], meta_array[k])
                RMSE = metrics.mean_squared_error(af_array[k], meta_array[k])**0.5
                MAPE = metrics.mean_absolute_percentage_error(af_array[k], meta_array[k])
                print(res[k],plddt[k],"%.2f"%metapredict_result[k],ss[k],
                      "%.2f"%MSE,"%.2f"%MAE,file=data_name_meta)


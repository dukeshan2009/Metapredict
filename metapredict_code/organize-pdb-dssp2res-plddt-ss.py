# this code extract amino acid and PLDDT from the pdb file and secondary structure from the data file

import sys
#import numpy 

name=sys.argv[1]

pdb_name=name+".pdb"
ss_name=name+".dssp"
out_name=name+".out"

file_ss=open(ss_name,"r")
file_out=open(out_name,"w+")

# skip the first 28 line for the secondary structure file
for i in range(28):
  file_ss.readline()

with open(pdb_name) as file_pdb:
  for line in file_pdb:
    if line.split()[0]=='ATOM':
      if (line.split()[2]=='CA'):
        ss=file_ss.readline()[16]
        if (ss==' '):
          ss='~'
        # v2 in here we changed split()place from [10]to[-2],some dssp file have some error when we using [10]to grab data. 
        print(line.split()[3],line.split()[-2],ss,file=file_out)

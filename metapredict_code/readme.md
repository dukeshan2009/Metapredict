Codes could directly running in testing data folder. 

# metapredict_byout.py 

This code is generate metapredict plddt result by feeding residue sequence data. 
The results is mentioned in testing data folde readme.md

#anaysis_meta_barplot.py

this code is for calculate r2 value.
r2 value is calculate by sklearn package. 
We use AF2 plddt as y_true, Meta plddt as y_pred 
The result will show in the .png file's name. 
And it will also genreate a counting picture by every 10% diffferent for a large group of protein data. 

# organize-pdb-dssp2res-plddt-ss.py 
# output-dssp-mcc-folder.sh  
# do-dssp-mcc-folder.sh 

These three codes are using for grab amino acid and second structure information and orgnized in AF*.out files. 
It will convert .pdb files into .dssp file, and then combine two file together to get AF*.out
Af*.out files are in order of amino acid, AF2_plddt score, Second structure.



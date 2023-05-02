# extract the ss information based on number of residues
# 10/26/2022 added 5-turn-helix
import sys

file_path = sys.argv[1]
res_num = sys.argv[2]
ss=['~','E','B','T','S','H','G','I']
ss_name=['coil','beta-sheet','beta-bridge','turn','bend','ahelix','three-helix','five-helix']

output_file=["" for i in range(len(ss_name))]

for i in range(len(ss_name)):
  filename=ss_name[i] + ".csv"
  output_file[i]=open(f"{res_num}/{filename}","a")


with open(file_path) as input_file:
  for line in input_file:
   if len(line.split())==4:
    for k in range(len(ss_name)):
     if line.split()[3]==ss[k]:
      print(line[:-1],file=output_file[k])
      print(f"Added line to {output_file[k]}") 

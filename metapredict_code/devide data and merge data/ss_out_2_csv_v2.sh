#!/bin/bash
#SBATCH --time=25:15:00             # Time limit for the job (REQUIRED).
#SBATCH --job-name=ss2csv      # Job name
#SBATCH --nodes=1               # Number of nodes to allocate. Same as SBATCH -N (Don't use this option for mpi jobs)
#SBATCH --ntasks=64                  # Number of cores for the job. Same as SBATCH -n 1
#SBATCH --mem=128g
#SBATCH --partition=normal          # Partition/queue to run the job in. (REQUIRED)
#SBATCH -e slurm-res-%j.err             # Error file for this job.
#SBATCH -o slurm-res-%j.out             # Output file for this job.
#SBATCH -A coa_qsh226_uksr       # Project allocation account name (REQUIRED)
#SBATCH --mail-type ALL         # Send email when job starts/ends
#SBATCH --mail-user xsh230@uky.edu   # Where email is sent to (optional)
# Find *out files and add them to corresponding *csv files.
# how-to-run: ./ss_out_2_csv.sh .
# This assumes the scripts and out-folders are in the same folder.
find $1 -type f -name "MT*.out" | xargs -I {} -P 1000 python3 analyze-ss_v2.py {};

#find $1 -type f -name "AF*.out" | while read dir; do
#    python analyze-ss.py $dir
#    echo $dir
#done

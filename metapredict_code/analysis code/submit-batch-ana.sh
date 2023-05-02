#!/bin/bash
#SBATCH --time=12:00:00             # Time limit for the job (REQUIRED).
#SBATCH --job-name=Batch-ana      # Job name
#SBATCH --nodes=1               # Number of nodes to allocate. Same as SBATCH -N (Don't use this option for mpi jobs)
#SBATCH --ntasks=64                  # Number of cores for the job. Same as SBATCH -n 1
#SBATCH --mem=128g
#SBATCH --partition=normal          # Partition/queue to run the job in. (REQUIRED)
#SBATCH -e slurm-%j.err             # Error file for this job.
#SBATCH -o slurm-%j.out             # Output file for this job.
#SBATCH -A coa_qsh226_uksr        # Project allocation account name (REQUIRED)
#SBATCH --mail-type ALL         # Send email when job starts/ends
#SBATCH --mail-user xsh230@uky.edu   # Where email is sent to (optional)

conda init
module load ccs/conda/python
source activate /scratch/xsh230/metapredict

python Batch-analysis.py

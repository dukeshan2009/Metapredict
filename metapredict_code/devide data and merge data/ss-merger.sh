#!/bin/bash
#SBATCH --time=5:15:00             # Time limit for the job (REQUIRED).
#SBATCH --job-name=ss010     # Job name
#SBATCH --nodes=1               # Number of nodes to allocate. Same as SBATCH -N (Don't use this option for mpi jobs)
#SBATCH --ntasks=64                  # Number of cores for the job. Same as SBATCH -n 1
#SBATCH --mem=128g
#SBATCH --partition=normal          # Partition/queue to run the job in. (REQUIRED)
#SBATCH -e slurm-res-%j.err             # Error file for this job.
#SBATCH -o slurm-res-%j.out             # Output file for this job.
#SBATCH -A coa_qsh226_uksr       # Project allocation account name (REQUIRED)
#SBATCH --mail-type ALL         # Send email when job starts/ends
#SBATCH --mail-user xsh230@uky.edu   # Where email is sent to (optional)
# This script finds all .out files, counts their lines (as a proxy for number of residues),
# and groups the protein info according to the range they fall in. This last part is done by
# append-residues.py
module load Miniconda3
conda init
source ~/.bashrc
conda activate py310

appender () {
  x=`wc -l $1`; lines=($x);  line=${lines[0]};
  line_no=$(( line / 100 ))
  dir=$1 
  if (( $line_no>10 ))
  then
    line_no=10
  fi

  python3 append-ss.py $dir $line_no
#  echo $1 $line_no
}

export -f appender
find $1 -type f -name "MT*.out" | xargs -I {} -P 1000 bash -c 'appender  "$@"' _ {};


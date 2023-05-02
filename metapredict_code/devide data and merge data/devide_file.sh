#!/bin/bash
#SBATCH --time=24:00:00             # Time limit for the job (REQUIRED).
#SBATCH --job-name=b3dev      # Job name
#SBATCH --nodes=1               # Number of nodes to allocate. Same as SBATCH -N (Don't use this option for mpi jobs)
#SBATCH --ntasks=64                  # Number of cores for the job. Same as SBATCH -n 1
#SBATCH --mem=128g
#SBATCH --partition=normal          # Partition/queue to run the job in. (REQUIRED)
#SBATCH -e slurm-batch5-%j.err             # Error file for this job.
#SBATCH -o slurm-batch5-%j.out             # Output file for this job.
#SBATCH -A coa_qsh226_uksr        # Project allocation account name (REQUIRED)
#SBATCH --mail-type ALL         # Send email when job starts/ends
#SBATCH --mail-user xsh230@uky.edu   # Where email is sent to (optional)

# This script finds all .out files, counts their lines (as a proxy for number of residues),
# and groups the protein info according to the range they fall in. This last part is done by
# append-residues.py

appender () {
  x=`wc -l $1`; lines=($x);  line=${lines[0]};
  line_no=$(( line / 100 ))
  dir=$1 
  if (( $line_no>10 ))
  then
    line_no=10
  fi

  cp $dir MT-$line_no
  #echo $1 $line_no
}

export -f appender
find $1 -type f -name "MT*.out" | xargs -I {} -P 1000 bash -c 'appender  "$@"' _ {};


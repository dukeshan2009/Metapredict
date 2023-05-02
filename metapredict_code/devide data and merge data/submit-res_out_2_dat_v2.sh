#!/bin/bash

# $1 is the location of the out-folders.

for i in {1..20}; 
do 
{
    sbatch ./res_out_2_dat_v2.sh out-data-$i;
}

done


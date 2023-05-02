#!/bin/bash 

for i in {0..10};

do 
{
    cp anaysis_meta_barplot.py MT-$i/
    cp do_anaysis_meta_barplot.sh MT-$i/
    cd MT-$i 
    sbatch do_anaysis_meta_barplot.sh
    cd ..
}

done
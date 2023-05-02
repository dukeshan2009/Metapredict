#!/bin/bash


for i in {0..10};
do
{
cp MT-analysis.py MT-$i/
cp MT-ana.sh MT-$i/
cd MT-$i
sbatch MT-ana.sh
cd ..
}
done
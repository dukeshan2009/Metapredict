#!/bin/bash



./mk-folders.sh
for i in {1..20};
do
{
    sbatch ./ss-merger.sh out-data-$i
}
done

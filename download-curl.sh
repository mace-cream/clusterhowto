#!/bin/bash
# curl --head url Content-Length:  13923888724
set -e -x
url=https://cvml.ist.ac.at/AwA2/AwA2-base.zip
total_bytes=$(curl --head $url | grep Content-Length | awk '{split($0,a," ");print a[2]}' | awk '{print substr($0, 1, length($0)-1)}') 
start_id=$SLURM_ARRAY_TASK_ID
end_id=$((SLURM_ARRAY_TASK_ID+1))
total_id=$((SLURM_ARRAY_TASK_MAX+1))
echo $total_bytes
echo $total_id
start=$((start_id * total_bytes / total_id))
end=$((end_id * total_bytes / total_id -1))
#echo $filename
curl -H "Range: bytes=$start-$end" $url -o $start-$end.partial.zip

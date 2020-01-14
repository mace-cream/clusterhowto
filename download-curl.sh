#!/bin/bash
# Usage: sbatch --array=0-N download-curl.sh file_url
# replace N with the number of thread you want
# and file_url with the url you want
# The file server should support partial downloading for multithreading download to work
# Current limitation: the file prefix is hard coded, e.g. zip format.
set -e -x
url=$1
suffix="${url##*.}"
total_bytes=$(curl --head $url | grep Content-Length | awk '{split($0,a," ");print a[2]}' | awk '{print substr($0, 1, length($0)-1)}') 
start_id=$SLURM_ARRAY_TASK_ID
end_id=$((SLURM_ARRAY_TASK_ID+1))
total_id=$((SLURM_ARRAY_TASK_MAX+1))
echo $total_bytes
echo $total_id
start=$((start_id * total_bytes / total_id))
end=$((end_id * total_bytes / total_id -1))
filename=$(printf %02d $start_id).partial.$suffix
curl -H "Range: bytes=$start-$end" $url -o $filename
# after the downloading complete, please use `cat *.partial.$suffix > total.$suffix` to join the partial files together

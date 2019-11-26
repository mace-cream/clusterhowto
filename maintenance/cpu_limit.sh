#!/bin/bash
# get the top 5 processes
result=1490.0
mapfile -t proc_list < <(ps --no-headers --sort=-pcpu -Ao pid,pcpu | head -n 5)
for i in "${proc_list[@]}"; do
    process_cpu_list=($i)
    process_id=${process_cpu_list[0]}
    cpu_usage_percentage=${process_cpu_list[1]}
    compare_result=$(awk 'BEGIN{ print '$cpu_usage_percentage'<'$result' }')
    if [ ! "$compare_result" -eq 1 ]; then
      nohup /usr/local/bin/cpulimit -b -p $process_id -l $result -z
    fi
done

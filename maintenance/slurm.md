## How to check slurm usage report

Below command check the usage report form a specific time.
```shell
sreport cluster all Start=2019-09-10
```

How to check GPU status of three computing nodes ( you should be root to execute this command)
```shell
pdsh -w node01,node02,node03 /cm/local/apps/cuda/libs/current/bin/nvidia-smi | dshbak
```
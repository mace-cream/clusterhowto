## How to check slurm usage report

Below command check the usage report form a specific time.
```shell
sreport cluster all Start=2019-09-10
```

How to check GPU status of three computing nodes ( you should be root to execute this command)
```shell
pdsh -w node01,node02,node03 /cm/local/apps/cuda/libs/current/bin/nvidia-smi | dshbak
```

The daemon service on computing node is called `slurmd` which read configuration file `/etc/slurm/gres.conf`. This file will be reset on rebooting (provision of computing node).
The default file is located at `/cm/shared/apps/slurm/var/etc/gres.conf` which sayes the machine has 8 GPUs. This is true for node01 but node02 and node03 have only 6 gpus. Therefore,
the configuration file should be modified to suit such purpose. Otherwise the slurm daemon on node02 (or node03) cannot be restarted. Currently, the replace file is located at
`/data2/gres.conf`. All you should do after rebooting of node02 or node03 is:

```shell
cp /data2/gres.conf /etc/slurm/gres.conf
```

## How to undrain a node
Using `root` account. 
```shell
scontrol
update NodeName=node01 State=RESUME
```
See [how-to-undrain-slurm-nodes-in-drain-state](https://stackoverflow.com/questions/29535118/how-to-undrain-slurm-nodes-in-drain-state)
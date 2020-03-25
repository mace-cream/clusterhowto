# How to Use Our New Cluster 

---------------------------------------
## Quality of Sevice (QoS)

* The home directory of each user is restricted to 10TB in maximal.
* Task directly running on manage node is allowed to use up to 10 GB memory and 14 CPUs. See [cron.md](./cron.md) for detail.
* Task submitted by Slurm can choose different Quality of Sevice (QoS):

|        QoS       |    Users   | \#GPUs | Priority |                        Example                       |
|:----------------:|:----------:|:------:|:--------:|:----------------------------------------------------:|
| normal (Default) |  Everyone  |    3   |   High   |       `srun --gres=gpu:1 -t 100 python main.py`      |
|       high       | Applicants |    7   |  Normal  | `srun --qos=high --gres=gpu:1 -t 100 python main.py` |

The high QoS have 7 extra GPUs for students submitting papers (and therefore 10 avaliable in total). You can apply it by consulting with Yang Li. 
The Priority decide the order of the queue of jobs waiting to be scheduled. And jobs of same Priority will follow a FIFO schedule.

## 1. Access the cluster
If you are outside Nanshan Park, please turning on the [institute vpn](vpn.md) first.

### Shell
On Windows client, [ModaXterm](https://mobaxterm.mobatek.net/) is recommended though it is a commercial freeware. It integrates SFTP and SSH so that you can view and edit your file 
easily. You can even change the default editor used by ModaXterm. Other client options are possible. For example, if you install git client for windows. You 
can ssh to the server using git bash. The syntax is simply:

```bash
> ssh -Y [username]@10.8.4.170
```

On Mac client, you can use the terminal to connect to the server. The syntax is listed as above. If you encounter locale setting warning, please add
`export LC_ALL=en_US.UTF-8` to your `~/.bash_profile`. See [ssh.md](./ssh.md) for detailed doc.

* `username` is the same user name you had on the old server .  

* `-Y` is optional for opening the X11 display

* The default password is `123456`

We also recommand [VSCode](https://code.visualstudio.com/), which combines code editor, shell, git control and debug
tools all-in-one. With the help of Remote-SSH extension of VSCode, you can manage your project directly on cluster as it is in your local. You can install 
many other extensions for your preference, such as Language support (Python/Matlab/C++/...), SFTP and UI Theme.

**IMPORTANT Notice** for first time login: Once you log in, reset password using the passwd tool and follow the prompt.  

```bash
> passwd 
```
The password change is shared, which means your login password to other machines are changed as well.

### Remote Desktop
See [vnc](./vnc.md)

### Webpage
Our lab homepage is located at [http://10.8.4.170](http://10.8.4.170). From there you can find the link to our lab's wiki, gitlab and jupyter etc.
For wiki and gitlab web service you need to register first. For jupyter web service, you login with your ssh username and password.

You can program in Python language using anaconda3 kernel on jupyter.

Currently the jupyter kernel is run on manage node and does not support GPU.

## 2. Where are my files?

Your home directory is located at `/home/[username]`.  It contains the following:

* System created directories, such as Desktop, Document, Download etc
* All files from your home directory on the old server.  
* If you have stored files on `/data` or `/data/users` of the old server, you can find those files in `/home/[username]/_data` . 

In addition, `/data/datasets` is now located at `/home/dataset`. 

**Important Notice** for personal directory limit: our storage node only has limited space. To make sure most users can have enough space for their scientific research, it is required that each user can have at most 10 TB space. If you exceed this hard limit, please clean up your folder as soon as possible. You can move datasets to `/home/dataset` and erase unused intermediate model files. Your slurm account will be banned if you violate this. Thanks for your cooperation.

## 3. First look of the BCM Cluster 

Our cluster has 5 nodes (servers)

| nodename | direct shell access | ip address | OS           |
| -------- | ------------------- | ---------- | ------------ |
| bcm      | Yes                 | 10.8.4.170 | CentOS 7.6   |
| node01   | No                  |            | CentOS 7.6   |
| node02   | No                  |            | CentOS 7.6   |
| node03   | No                  |            | CentOS 7.6   |
| nfs      | Yes                 | 10.8.4.172 | Ubuntu 16.04 |

* `bcm`:  management node  
* `node01` : computing node with 8 TITAN V GPUs, 56 CPUs, 256GB RAM
* `node02`: computing node with 8 TITAN V GPUs, 256GB RAM
* `node03` : computing node with 4 Telsa K80 GPU cores and 2 TITAN V GPUs, 128GB RAM, fastest CPU among all nodes
* `nfs`: storage node that hosts the 77T file system `/home`

As a user, you can access to the `bcm` and `nfs` node using the same username and password.
These User information is stored in a central database. 
To take advantage of the computing resources on nodes 1-3, you will need to use the SLURM workload manager.   (See Section 5.)

By default, your home directory has `700` permissions, which means others do not have read access to the files in your home. 
You can change the permission to enable file sharing or you can place shared files in 

*  `/home/dataset` : save large public datasets here 
* `/data1`: 5T temporary storage space 
* `/data2`: 5T temporary storage space

## 4. Setup a working environment

### Load modules

BCM allows each user to customize their working environment, such as choosing different software version, through "module" commands. 

For example, the default python version is 2.7. To use python 3, you need to load the `anaconda3 /py3` module.

```shell
module add anaconda3/py3
```

This adds anaconda 3 to your current session.  Now you can use Python 3.6 by typing `python`. To make this module load every time you log in, type

```
module initadd anaconda3/py3
```

You can also directly add the module to your session profile. i.e.  add the following line to the end of `~/.bashrc` ( a script that runs at the start of every new terminal session).
If you use `zsh`, put the command in `~/.zshrc`.
``` 
module load anaconda3/py3 
```

To make your code work on the cluster, you will likely need additional modules, such as

- `cuda90/toolkit/9.0.176` is needed for NVIDIA tools  
- `cudnn/7.0` is needed for using the GPUs for deep learning
- `openmpi` is for parallel processing  

Here is a sample `.bashrc` file that include all the above packages:

```bash
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
module load gcc anaconda3/py3 cuda90/toolkit/9.0.176 cudnn/7.0 openmpi/cuda/64/3.1.3
module load slurm 
```

The last two lines is where modules are loaded.  `gcc` is the C compiler, `slurm` is the workload manager (this line is added by default)

After you modify `.bashrc`, use

```
soure .bashrc
```

to make the change take into effect in your current session. Alternatively, you can simply start a new session by re-logging.

### C/C++ developer

See [cpp.md](./cpp.md) for detail.

### Python packages
Important Notice: Since python 2.7 will not be supported from Jan. 1st 2020 and many famous packages do not support python version 2 now. Therefore any new problems about python 2 will not be supported by our lab's server admin.  

#### Simple Solution

If you need any additional Python packages which is not installed by anaconda or system python by default, you can use `pip` to install it within your home directory (with `--user` option)

For example, to install a package called graphviz, which is not bundled by anaconda. You can type:

```shell
python -m pip install --user graphviz
```
#### Custom Environment
If you need another version of Python package which is incompatible with existing installation. You need to configure your own Python environment using `conda`.
See [Configure Environment](http://10.8.4.170/wiki/index.php/Configure_the_environment) for detail.

For further detail you can check [python.md](./python.md).

## 5. How to use slurm 

We will use SLURM to submit jobs to the cluster. It automatically allocates GPU/CPU resources to you based on your requests. 
This is the **only way to use the GPU resources** on our lab server.

### Using srun

For interactive development, you can use `srun`  to submit a single job.

```
srun --gres=gpu:1 [command]
```

* `--gres=gpu:1` requests one GPU for running the code. 
* `[command]` can be any terminal command such as `python test.py` or `nvidia-smi` 

Note that setting `--gres=gpu` to more than one will NOT automatically make your code faster! You also need to make sure your code supports multiple GPUs. See the following links on how to achieve this.

* Keras: https://keras.io/getting-started/faq/#how-can-i-run-a-keras-model-on-multiple-gpus
* Tensorflow: https://www.tensorflow.org/guide/using_gpu#using_multiple_gpus
* Pytorch: https://pytorch.org/tutorials/beginner/former_torchies/parallelism_tutorial.html

Each user is currently limited to use at most 6 GPUs at a time. We may adjust this limit later depending on the cluster usage. 

### Using sbatch

While `srun` executes commands in real time, `sbatch` schedules your job for later execution. Therefore it is good for longer training jobs. e.g. You can submit as many jobs as you want to the slurm queue, and each job will be executed as soon as resources become available.  

To submit a job, you need to wrap terminal commands within a `sbatch` script.   Suppose you want to run a GPU program `test.py`. First create a new file  `submit_jobs.sh`  with the following content:

```bash
#!/bin/bash
#SBATCH -J yang       # job name
#SBATCH -p defq       # partition name (should always be defq)
#SBATCH -N 1          # number of computing node (should always be 1)
#SBATCH --ntasks=1    # maximum number of parallel tasks (processes) 
#SBATCH --gres=gpu:1  # number of gpus allocated on each node
#SBATCH -t 105:00     # maximum running time in hh:mm:ss format

python test.py    
```

* Lines starting with `#BATCH` are slurm allocation requests. In this example, we created a job named "yang" on the default queue (defq), allocated one computing node with one CPU core and one GPU per node. The allocation will be available for a maximum of 105 minutes.
* The last line `python test.py` is the command to be run. If multiple commands are listed, they will be always be executed sequentially, NOT in parallel. 
* `ntasks` and `--gres=gpu` should be 1 unless your code have multi-GPU support.  When using multiple GPUs, be nice and allocate no more than a few.  

Make the script executable by

```bash
chmod a+x submit_jobs.sh
```

Then submit the job with `sbatch`

```bash
[yang@node01 ~]$ sbatch submit_jobs.sh                   
Submitted batch job 177
```

 The output log of this job will be saved to  `slurm-[jobID].out` in the current directory. A useful way to display the log in real time is via the tail command. e.g

```
tail -f slurm-177.out
```

To exit, use Ctrl-C.

### View and Cancel jobs

You can view the job queue using `squeue`. (This applies to all jobs submitted with `srun` or `sbatch`)  

```bash
[yang@bcm ~]$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               177      defq     yang     yang  R       0:30      1 node01 
```

* The column named ST displays the status of your job. 'R' stands for running and 'PD' stands for pending (waiting for resource).

You can also monitor your jobs using GUI program `sview` or using a web browser. Visit https://10.8.4.170 and select User Portal. Log in with your account name and go to the Workload page (https://10.8.4.170:8081/userportal/#/workload) from the left menu. You will see the status of all your submitted jobs.

![](images/tutorial02.png)

 To cancel a job, use `scancel`:

```
scancel [jobID]
```

Do NOT use `kill` to stop a slurm job! It will only stop the slurm process, but not the job itself. 

You can pipeline your work by submitting multiple sbatch scripts. The jobs will be allocated on different GPUs that are available. 

### Useful stuff about slurm
You can find many useful tutorial about slurm from world wide web. Here are some tips:
`pestat -G` prints Slurm cluster status with 1 line per node. 

![](images/tutorial05.png)

Find out who is using all the resources with `showuserjobs`

![](images/tutorial04.png)

For extra documentation about how to use slurm, you can check [slurm.md](./slurm.md) or 
see extra online resources:

* Official documentation: https://slurm.schedmd.com/documentation.html
* A tutorial: https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html

## 7. Further documentation
You can download the official user guide of how to user cluster at [User Manual](http://10.8.4.170/wiki/index.php/文件:user-manual.pdf)

## 8. Further questions
You can submit issues on [our github](https://github.com/mace-cream/clusterhowto/issues) or [intranet gitlab](http://10.8.4.170:88/yang/clusterhowto/issues). For instant communication please join the [slack](https://join.slack.com/t/lab2c/shared_invite/enQtODk0MDAxNDM2MjEwLTk3YzA3ZTRkODljZWQ0ZmI5MjJmMWNkNWUwMzhhZGRlNmNlZTNiMTlkZDc2NjcwZDNhZjBjYmY0NzhhMDVkNTg) channel of our lab.
WeChat is not recommended to ask technical questions.

## Changelog

### Version 3.5
* Add many slurm tips
* Add github and intranet gitlab support.
* Add slack invitation link

### Version 3.4
* Add Matlab on Manage Node

### Version 3.3
* Add conda advanced tutorial

### Version 3.2
* Add how to use Jupyter

### Version 3.1
* Add how to use remote desktop
* Add how to use C++ documentation
* Removed web browser access since it is super laggy
* Disabled ssh between nodes since we are moving to slurm for GPU management
* Clarified instructions on module load
* Added instructions on using slurm interactively with srun

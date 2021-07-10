# How to Use Our Cluster 

We have a high performance cluster for your research computation.

This repo servers as a quick start tutorial for cluster usage.

You can find further details in other chapters.

## 5 minutes Quick Start
- Access server via SSH. You may need [VPN](vpn.md) outside iPark. You also need an SSH client. If you use windows operating system,
  [ModaXterm](https://mobaxterm.mobatek.net/) is recommended. For other operating systems, you can use the system default terminal.
```bash
> ssh [username]@10.8.6.22
```
  Then You use the following command to load necessary modules to run GPU code:
```bash
> module load slurm anaconda3/py3 cuda90/toolkit/9.0.176 cudnn/7.0
```
- Submit a GPU job using
```bash
> srun --gres=gpu:1 python /home/feng/mcr/k_mnist_xregression_simple.py
```
If you encounter any errors, please run `module purge` first and retry. If errors persist, please report your issue to the server admin.

## 1. Access the cluster

### 1.1 Account

For new students, you need to apply for a cluster account from [server administrators](http://10.8.6.22/wiki/index.php/ServerAdmin).
The cluster account consists of 3 parts: shell access to manage node(10.8.6.22) and storage node(10.8.6.21); universal identity verification(seafile, jupyter, etc);
slurm account, which is used to submit jobs to computing node.

You will get an initial password, which is very complex and
it is VERY IMPORTANT to change password once you log in, reset password using the `passwd` tool and follow the prompt. 

```bash
> passwd 
```

**Never** use simple password like 123456, cluster admin may have a regular check on password complexity and reset your weak password.

Your home directory is located at `/home/[username]`.
You can put/find commonly used datasets in `/home/dataset`.
If you want to put data in this directory. Please declare it on [Dataset](http://10.8.6.22/wiki/index.php/Dataset).
Otherwise, your dataset in `/home/dataset` may be removed without notice.

By default, your home directory has `700` permissions, which means others do not have read access to the files in your home.

### 1.2 VPN

If you are outside Nanshan Park, please turning on the [institute vpn](vpn.md) first. It is prohibited to use personal reverse proxies for security concern.
If you use general reverse proxies (which means anyone can access the server using the cluster accounts from outside) on the lab, your slurm account will be banned.

### 1.3 Shell Access(Recommend)
For Windows client, [ModaXterm](https://mobaxterm.mobatek.net/) is recommended though it is a commercial freeware. It integrates SFTP and SSH so that you can view and edit your file 
easily. You can even change the default editor used by ModaXterm. Other client options are possible. For example, if you install git client for windows. You 
can ssh to the server using git bash. The syntax is simply:

```bash
> ssh -Y [username]@10.8.6.22
```

For Mac client, you can use the terminal to connect to the server. The syntax is listed as above. If you encounter locale setting warning, please add
`export LC_ALL=en_US.UTF-8` to your `~/.bash_profile`(if you use other shells, the profile name is different). See [ssh.md](./service.md#ssh) for detailed doc.

* `username` is the same user name you had on the old server .  

* `-Y` is optional for opening the X11 display, this options works natively for Linux desktop; if you install Xterm support on Mac or use ModaXterm on windows.

We also recommand [VSCode](https://code.visualstudio.com/), which combines code editor, shell, git control and debug
tools all-in-one. With the help of Remote-SSH extension of VSCode, you can manage your project directly on cluster as it is in your local. You can install 
many other extensions for your preference, such as Language support (Python/Matlab/C++/...), SFTP and UI Theme.

### 1.4 Cluster Home Page
Our lab homepage is located at [http://10.8.6.22](http://10.8.6.22). From there you can find the link to our lab's wiki, gitlab, overleaf and jupyter etc. You can also connect to our manage node or storage node using remote desktop there. For wiki and gitlab web service you need to register first. For jupyter web service, you login with your ssh username and password.


## 2. Cluster Structure

Our cluster has 7 nodes (servers)

| nodename | direct shell access | ip address | OS           |
| -------- | ------------------- | ---------- | ------------ |
| bcm      | Yes                 | 10.8.6.22 | CentOS 7.6   |
| node01   | No                  |            | CentOS 7.6   |
| node02   | No                  |            | CentOS 7.6   |
| node03   | No                  |            | CentOS 7.6   |
| node04   | No                  |            | CentOS 7.6   |
| node05   | No                  |            | CentOS 7.6   |
| nfs      | Yes                 | 10.8.6.21 | Ubuntu 16.04 |

* `bcm`:  management node  
* `node01` : computing node with 8 TITAN V GPUs, 56 CPUs, 256GB RAM
* `node02`: computing node with 8 TITAN V GPUs, 256GB RAM
* `node03` : computing node with 4 Tesla K80 GPU cores and 2 TITAN V GPUs, 128GB RAM, fastest CPU among all nodes
* `node04`: computing node with 8 RTX 3090 GPUs, 256GB RAM
* `node05`: computing node with 8 RTX 3090 GPUs, 256GB RAM
* `nfs`: storage node that hosts the 77T file system `/home`

As a user, you can access to the `bcm` and `nfs` node using the same username and password.

To take advantage of the computing resources on nodes 1-5, you will need to use the SLURM workload manager.


## 3. Setup a working environment

### 3.1 Load modules

BCM allows each user to customize their working environment, such as choosing different software version, through "module" commands. 

For example, the default python version is 2.7 on CentOS. To use python 3, you need to load the `anaconda3 /py3` module.

```shell
module add anaconda3/py3
```

This adds anaconda 3 to your current session.  Now you can use Python 3.6 by typing `python`. 

We have a lot of pre-installed modules like CUDA (for GPU programs), cuDNN (for deep learning). You can use following command to see the complete software list.
``` 
module avail
```

To make modules automatic loaded every time you log in, type

```
module initadd anaconda3/py3
```

You can also directly add the module to your session profile. i.e.  add the following line to the end of `~/.bashrc` ( a script that runs at the start of every new terminal session).
If you use `zsh`, put the command in `~/.zshrc`.
``` 
module load anaconda3/py3 
```
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
module load gcc anaconda3/py3 cuda90/toolkit/9.0.176 cudnn/7.0
module load slurm 
```

The last two lines is where modules are loaded.  `gcc` is the C compiler, `slurm` is the workload manager (this line is added by default)

After you modify `.bashrc`, use

```
source .bashrc
```

to make the change take into effect in your current session. Alternatively, you can simply start a new session by re-logging.

### 3.2 Python Environment
#### Python Version
We have pre-installed multiple versions of python interpreter, together with many popular packages. Load corresponding module to use them:

| Module Name    | Python Version | Package Version                  |
|----------------|----------------|----------------------------------|
| anaconda2/py2  | 2.7.16         | -                                |
| anaconda3/py3  | 3.6.5          | tensorflow 1.8.0; pytorch 1.0.1  |
<!-- | anaconda3/py38 | 3.8.5          | tensorflow 2.4.1; pytorch 1.8.1  | -->

Important Notice: any problems about python 2 will not be supported by our lab's server admin.

#### Deep Learning Environment
Due to different GPU type and driver version, an sepecific envrionment may not work well on all computing node. For simplicity,
the table below lists the recommanded envrionment for different computing nodes:

|                | node[01-03]                           | node[04-05]                                   |
|----------------|---------------------------------------|-----------------------------------------------|
| Pytorch        | cuda10.1 cudnn7.6.5 pytorch/1.7.1     | cuda11.1 cudnn8.0-cuda11.1 pytorch/1.8.0      |
| Tensorflow 1.x | cuda10.0 cudnn7.6.5 tensorflow/1.15.0 | NOT SUPPORTED                                 |
| Tensorflow 2.x | cuda10.1 cudnn7.6.5 tensorflow/2.3.0  | cuda11.1, cudnn8.0-cuda11.1, tensorflow/2.4.1 |

#### PIP

If you need any additional Python packages which is not installed by anaconda or system python by default, you can use `pip` to install it within your home directory (with `--user` option)

For example, to install a package called graphviz, which is not bundled by anaconda. You can type:

```shell
python -m pip install --user graphviz
```
#### Custom Environment
If you need another version of Python package which is incompatible with existing installation. You need to configure your own Python environment using `conda`.
See [Configure Environment](http://10.8.6.22/wiki/index.php/Configure_the_environment) for detail.

### Deep Learning Environment

## 4. Submit a job using Slurm

We will use SLURM to submit jobs to the cluster. It automatically allocates GPU/CPU resources to you based on your requests. 
This is the **only way to use the GPU resources** on our lab server.

### 4.1 Using srun

After interactive development on local workstation, you can use `srun`  to submit a single job.

```
srun --gres=gpu:1 [option] [command]
```

* `--gres=gpu:1` requests one GPU for running the code. 
* `[command]` can be any terminal command such as `python test.py` or `echo "hello world"` 
* `[option]` can be any of following:

| option     | description                                         | default value         |
| ---------- | --------------------------------------------------- | --------------------- |
| -w node01  | use node01 for computation                          | automictic allocation |
| --qos=high | use high quality of service                         | --qos=normal          |
| -t 200     | the maximum job running time is limited to 200 mins | -t 4320 (3 days)      |
| --gres=gpu:1  | use 1 GPU for computation                          | None |
| --unbuffered  | display output in real-time                          | None |

The maximal time each GPU job is allowed to run is 3 days divided by the number of GPUs your job is using.

Note that setting `--gres=gpu` to more than one will NOT automatically make your code faster! You also need to make sure your code supports multiple GPUs. See the following links on how to achieve this.

* Keras: https://keras.io/getting-started/faq/#how-can-i-run-a-keras-model-on-multiple-gpus
* Tensorflow: https://www.tensorflow.org/guide/using_gpu#using_multiple_gpus
* Pytorch: https://pytorch.org/tutorials/beginner/former_torchies/parallelism_tutorial.html

### 4.2 Using sbatch

While `srun` executes commands in real time, `sbatch` schedules your job for later execution. Therefore it is good for longer training jobs. e.g. You can submit as many jobs as you want to the slurm queue, and each job will be executed as soon as resources become available.

To submit a job, you need to wrap terminal commands within a `sbatch` script.   Suppose you want to run a GPU program `test.py`. First create a new file  `submit_jobs.sh`  with the following content:

```bash
#!/bin/bash
#SBATCH -J yang       # job name, optional
#SBATCH -p defq       # partition name (should always be defq)
#SBATCH -N 1          # number of computing node
#SBATCH --ntasks=1    # maximum number of parallel tasks (processes)
#SBATCH --gres=gpu:1  # number of gpus allocated on each node
#SBATCH -t 105:00     # maximum running time in hh:mm:ss format, optional

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
sbatch submit_jobs.sh                   
```

The output log of this job will be saved to  `slurm-[jobID].out` in the current directory. A useful way to display the log in real time is via the `tail` command. e.g

```
tail -f slurm-177.out
```

To exit, use Ctrl-C.

### 4.3 View and Cancel jobs

You can view the job queue using `squeue`. (This applies to all jobs submitted with `srun` or `sbatch`)

```bash
[yang@bcm ~]$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               177      defq     yang     yang  R       0:30      1 node01 
```

* The column named ST displays the status of your job. 'R' stands for running and 'PD' stands for pending (waiting for resource).

You can also monitor your jobs using GUI program `sview` or using a web browser. Visit [User Portal](https://10.8.6.22:8081/userportal). Log in with your account name and go to the Workload page (https://10.8.6.22:8081/userportal/#/workload) from the left menu. You will see the status of all your submitted jobs.

![](images/tutorial02.png)

 To cancel a job, use `scancel`:

```
scancel [jobID]
```

You can pipeline your work by submitting multiple sbatch scripts. The jobs will be allocated on different GPUs that are available. 

### 4.4 Useful stuff about slurm
You can find many useful tutorial about slurm from world wide web. Here are some tips:
`pestat -G` prints Slurm cluster status with 1 line per node. 

![](images/tutorial05.png)

Find out who is using all the resources with `showuserjobs`

![](images/tutorial04.png)

For extra documentation about how to use slurm, you can check [slurm.md](./slurm.md) or 
see extra online resources:

* Official documentation: https://slurm.schedmd.com/documentation.html
* A tutorial: https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html


## 5. Quality of Service (QoS)

### 5.1 How many GPUs can I use?

* The home directory of each user is restricted to 10TB in maximal.
* Task directly running on manage node is allowed to use up to 10 GB memory and 14 CPUs. See [cron.md](./cron.md) for detail.
* Task submitted by Slurm can choose different Quality of Service (QoS):

|        QoS       |    Users   | \#GPUs | Priority |                        Example                       |
|:----------------:|:----------:|:------:|:--------:|:----------------------------------------------------:|
| normal (Default) |  Everyone  |    3   |   High   |       `srun [--qos=normal] --gres=gpu:1 python main.py`      |
|       high       | Applicants |    ~7   |  Normal  | `srun --qos=high --gres=gpu:1 python main.py` |

The high QoS have 7 extra GPUs for students submitting papers (and therefore 10 avaliable in total). You can apply it by consulting with Yang Li.

Note that, the number of extra high QoS may change depends on overall workload of our sever, i.e., get larger at low-workload and smaller at high-workload. This kind of change will take effect without further notice and you can check the latest quota in this page. 

### 5.2 Why my jobs are waiting?

There are two reasons:
- You have run out of your quota. In this case your waiting jobs will not be scheduled even though there's free rescources. Please wait for your previous job or apply more quota.
- Your job is queued. In such case, our sever is very busy. The Priority decide the order of the queue of jobs waiting to be scheduled. As you see, normal QoS have hgher Priority than high QoS, and jobs of same Priority will follow a FIFO schedule.


## 6. Further documentation
You can download the official user guide of how to user cluster at [User Manual](http://10.8.6.22/wiki/index.php/File:user-manual.pdf).

## 7. Further questions
You can submit issues on [our github](https://github.com/mace-cream/clusterhowto/issues) or [intranet gitlab](http://10.8.6.22:88/yang/clusterhowto/issues).
For instant communication please join the [slack](https://join.slack.com/t/lab2c/shared_invite/enQtODQyMTY4OTcyNTMwLWRkOTlkYmM2MWI3NGYzOWMwYTRkYzEzMTBjNjcxMWMxNTMxZjg2N2U1YzE5ZjI4YTE3ZTQ2ZWU2YzEyODNmMmU) channel of our lab.
Though we have a wechat group for server related issues, it is not recommended to use it compared with the above ways.



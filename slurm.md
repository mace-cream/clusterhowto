`slurm` is our workload manager. Here are some tips:

1. If you need to specify the node to run your program use:

    ```shell
    #SBATCH --nodelist=node03
    ```

    in your script.

    For `srun`, you can use `srun -w node01 echo "hello world".
    
2. If you need more cpu resources to run your program, add

   ```shell
   #SBATCH -c 4
   ```
   Or you can use `srun -c 4 your_multi_threaded_or_multi_process_program`.
   
   That is, you require 4 cpus to run your program.
   By default, you only have one physical cpu if not specified. This cpu has 2 logical cores. You can request maximum 32 cpus.
   
3. You can submit several serial programs within one job and run them in parallel.

    ```shell
    #!/bin/bash
    srun your_first_program -options &
    METHOD=cpu_forward srun your_second_program -options &
    wait
    ```

    You should add `&` to each `srun`. Also, do not forget `wait` at the very end.

    After job finishes, you can check the detail by `sacct -j your_job_id`. It may shows how the job is decomposed into 2 tasks which are running in parallel.

    ![](./images/slurm_job_2_task.png)

4. Check cpu and memory usage of other nodes

    ```shell
    srun --nodelist=node02 ps -u feima -o pid,user,%mem,%cpu,cmd
    ```
5. submit array jobs
   See [Introduction to array jobs](https://slurm.schedmd.com/job_array.html). 
   For 2d array jobs. see usage example of [2d array jobs](https://wiki.anunna.wur.nl/index.php/Array_jobs)
   You can use this techniques to download file in multi-threaded way. See [download-curl.sh](./download-curl.sh) for example.

6. neural network library using cpus
   If your gpu resource limit is hit or you want to train your neural network using CPU. You can explicitly do this by specificying
   some environment variable. See [Python Guide](./python.md) for detail.

7. Interactive Shell
   ```shell
   srun --gres=gpu:1 -t 500 --pty bash
   ```
   You can use this method to debug your GPU program. Please quit it after your debugging session. This slurm job will also occupy one GPU.
   You can use `tmux` in this temporary session to open multiple windows. This is useful when you need to inspect the resource usage of current node with `top` or `/cm/local/apps/cuda/libs/current/bin/nvidia-smi`.
   Notice that all your tmux sessions are killed if you quit the shell. This behaviour is different with normal tmux usage.
   
8. openmpi
   ```shell
   module load openmpi/gcc/64/1.10.7
   # compile your programs
   salloc -N 2 mpirun your_mpi_program
   ```
   If you need to use hybrid programming (e.g. OpenMP + MPI), you need to enable specifically:
   ```shell
   salloc -N 2 -c 8
   mpirun -n 2 --cpus-per-rank 4 --oversubscribe --bind-to none nvtc/nvtc-variant -f /home/dataset/triangle_counting_dataset/s28.e15.kron.edgelist.bin
   ```
   You can have one line
   ```shell
   salloc -N 2 -c 6 mpirun -n 2 --cpus-per-rank 3 --bind-to none --oversubscribe ./hybridhello
   ```
   If `mpirun` is invoked using `sbatch`, the sample file for `run.sh` is
   ```bash
   #!/bin/bash
   #SBATCH -N 2
   #SBATCH --gres=gpu:1
   #SBATCH -t 500
   #SBATCH -c 8
   mpirun -n 2 --bind-to none --cpus-per-rank 4 --oversubscribe /home/feng/triangle_counting_gpu_v2/build/nvtc/nvtc-variant -f /home/dataset/soc-LiveJournal1.bin
   ```
9. Unbuffer
   If you are using `srun` to run your commands you can use the `--unbuffered` option which disables the output buffering.

10. mpich
   Run `mpich` program is similar but different with `openmpi`. First you need load `mpich/ge/gcc/64/3.3`, then compile your programs with `mpicc` provided by `mpich`. Finally run
   your program with `srun -N 2 --mpi=pmi2 your_program`.

11. Request nodes unavailable
   In some cases when some programs are running on `node01` and GPU is used out. Then you want to use CPU of `node01` to do some computation. You find your cpu job is pending.
   You can add the time limit to make your job run. That is `srun -t 500 -w node01 python --version`.

12. Submit graphics jobs
   You can use `slurm` to request graphics jobs, for example `xterm`. First you need to use `ssh-keygen -m pem` on our server to generate default 
   `~/.ssh/id_rsa.pub` and `~/,ssh/id_rsa`. You cannot specify the paraphrase. Then you should add `id_rsa.pub` to `~/.ssh/authorized_keys`. You can automatically
   do so by `ssh-copy-id username@10.8.4.172`.
   Finally make sure you `ssh -Y` to our server. Then use `srun --pty --x11 xterm` and enjoy it.

13. Debug mpi programs within slurm
   For openmpi, first using `salloc -N 2 --x11` to allocate nodes. Then use `mpirun -n 2 xterm -e gdb --args nvtc/nvtc-variant -f test_io_nvgraph.bin` to launch user programs within `xterm`.
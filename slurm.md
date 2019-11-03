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
    srun --nodelist=node02 ps -u feima -o pid,user,%mem,%cpu
    ```
5. submit array jobs
   See usage example of [array jobs](https://wiki.anunna.wur.nl/index.php/Array_jobs)

6. neural network library using cpus
   If your gpu resource limit is hit or you want to train your neural network using CPU. You can explicitly do this by specificying
   some environment variable. See [Python Guide](./python.md) for detail.
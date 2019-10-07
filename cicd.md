This guide introduces how to use CI feature of gitlab to help your experiment.

Currently, this proposal is experimental.

Since slurm does not provides a way to organize the log, it is very easy to end up with a lot of `slurm-1234.out`. Deleting these files will lose some useful informations.

Actually you can use gitlab-runner to upload these log files, a sample project is at [self-hosted-runner](https://gitlab.com/zhaofeng-shu33/triangle_counting_self-hosted_runner/).
Feel free to check the job logs at [log](https://gitlab.com/zhaofeng-shu33/triangle_counting_self-hosted_runner/pipelines).

1. Create a project in gitlab.com (or our self hosted gitlab).

1. You need to configure your runner at the project setting page. Your runner is private and project wide. That is, it will not be used by other people and other project. You do not need
to install again `gitlab-runner` as it is already available on our manage node. You should register for your own purpose.

1. Using `srun` to submit your job in `.gitlab.yml` configuration file.

1. Check the CICD page of the project.
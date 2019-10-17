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

## How to create multiple gitlab-runner instance on the same machine?
The default runner installed on our manage node is a service, you can check it by
```shell
systemctl status gitlab-runner
```
Since this runner registers several jobs for [gitlab.com](https://gitlab.com), it takes much longer time to check the job status for each registered runner (due to overseas speed limitation).
Therefore it is benificial to install another gitlab-runner instance on manage node.

To do this, we resort to the docker solution. That is, we start the gitlab-runner as a docker service. The configuration file is located at [docker-compose.yml](http://10.8.4.170:88/zhaofeng-shu33/lab2cnew/blob/master/docker-compose.yml).
After using `docker-compose start` to start the service. We can register for each project we need. However, since this runner is a Docker container, the shell executor is within the
container environment and is not usefully. We need to use the Docker executor as well. See [executor](https://docs.gitlab.com/runner/executors/README.html) how to configure Docker executor.

For more information, please check [cicd doc](http://10.8.4.170:88/help/ci/yaml/README.md).

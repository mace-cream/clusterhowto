# Docker
To use docker, you need to be within the docker group of node01. You can contact the server admin to add you to the docker group if needed.

Currently, you can only use docker in node01 with GPU support. There are some security issues when using docker. Therefore it is not recommended to use docker container in service mode.

## Example
```shell
srun -w node01 docker run --rm alpine:3.11 /bin/sh -c "echo 123;"
```
## Run docker with current user
```shell
srun -w node01 docker run -it --rm --user="$(id -u):$(id -g)" your_image
```

## Build docker images using mainland mirror
It is painful to build docker images at the step of installing overseas software stacks. There should be a mirror switch to deal with this problem, so that
the following effect is achieved:
* normally no mirror is used
* mirror is used when certain environment variable is set

To do this, use the following script switch in `build.sh`
```shell
if [[ ! -z "$A_MIRROR" ]] # not empty
  do something
fi
```

For `Dockerfile`, explicitly pass the environment variable to the build script:

```
ARG A_MIRROR
ENV A_MIRROR=$A_MIRROR
```

Finnaly, run the `docker` command with custom args:
```shell
srun -w node01 docker build -t your_target --build-arg A_MIRROR=1 .
```

## Remove images with `none` tag
```shell
srun -w node01 docker rmi $(srun -w node01 docker images --filter "dangling=true" -q)
```

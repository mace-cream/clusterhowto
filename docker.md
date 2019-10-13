# Docker
To use docker, you need to be within the docker group. You can contact the server admin to add you to the docker group if needed.

Currently, you can only use docker in the manage node without GPU support.

## Run docker with current user
```shell
docker run -it --rm --user="$(id -u):$(id -g)" your_image
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
docker build -t your_target --build-arg A_MIRROR=1 .
```
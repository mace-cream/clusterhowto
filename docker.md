# Docker
To use docker, you need to be within the docker group. You can contact the server admin to add you to the docker group if needed.

Currently, you can only use docker in the manage node without GPU support.

## Run docker with current user
```shell
docker run -it --rm --user="$(id -u):$(id -g)" your_image
```

## Build docker images using mainland mirror
to be written
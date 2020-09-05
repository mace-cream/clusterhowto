The docker installed on manage node is used by server maintainers.

How to run gui program in docker (manage node)
```
module load docker
xhost +local:root
docker run -it --rm -e 'DISPLAY=:3.0' -v /tmp/.X11-unit:/tmp/.X11-unix debian-xterm xterm
```
## How to manage sharelatex service
This service is maintained by `docker-compose`, configuration file at `/home/feng/sharelatex-config`.
After modifying the configuration file, you need to stop the service, remove the container and create
the service. Simply restarting the service does not work.

In specific, the following commands should be executed:
```
docker stop 
docker rm # do not use docker down to preserve the network
docker create
docker start # do not use docker up to start in backend
```

If you encounter the problem of cannot create bridged network, restarting docker daemon by
`systemctl restart docker`.
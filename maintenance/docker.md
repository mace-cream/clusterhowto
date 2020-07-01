The docker installed on manage node is used by server maintainers.

How to run gui program in docker (manage node)
```
module load docker
xhost +local:root
docker run -it --rm -e 'DISPLAY=:3.0' -v /tmp/.X11-unit:/tmp/.X11-unix debian-xterm xterm
```
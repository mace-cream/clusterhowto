The executable is located at:
```
/home/feng/minikube
```
Before using it, make sure the service is started, which is a virutal machine using VirtualBox.
```
./minukube status
```

If the service is not running, please start it first:
```
minikube start --driver=virtualbox
```

To simplify the management
```
alias kubectl="./minikube kubectl --"
```

To connect the docker daemon in the vm, run
```
eval $(./minikube -p minikube docker-env)
```
Then you can use `docker` to do some low-level management task.
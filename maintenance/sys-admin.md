You should execute the following command in `root` user.

## Rebooting
（计划之内的计算节点重启，由于安装新的软件等缘故）

```shell
cmsh # enter cmsh shell
device
reboot node03
```

## Swap Space
Node03 has no swap space due to etcd installation on `node03`. That is node03 has etcd role in kubernetes cluster.
The swap space can be checked with `free -m` command when logged in.

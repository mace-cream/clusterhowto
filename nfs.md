If you use unix system for your workstation, you can mount our nfs server by

```shell
sudo apt-get install nfs-common # Ubuntu
sudo mkdir -p /mnt/server
sudo mount 10.8.4.172:/data /mnt/server
```

Limitations: you may not have proper access to your home directory. A possible solution is to change your local user id and group id to match the
remote one.
For clients, sometimes it is necessary to mount nfs as network disk.
The command is
```
mkdir -p /media/data
sudo mount -t nfs 10.8.4.172:/data /media/data
```

Persistent mounting (modify `/etc/fstab`, add one line)
```
10.8.4.172:/data /media/data    nfs         rw              0       0
```
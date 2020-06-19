# Admin Wiki

## Log onto root: sudo su -

```
mongo -u root -p root_pass --authenticationDatabase admin
```

Test user: username: `ntfs`. This user is controled by LDAP and is a non-root user. The purpose of this user is used to test some functionality of our server.

## Add new user

To add a new user, use the [web portal](https://10.8.4.170:8081/bright-view/#!/auth/login).

## slurm job accounting add new user 

To grant slurm access (for using GPU nodes) to the new user "alice", use
```shell
sacctmgr create user name=alice DefaultAccount=users
```
## grant sudo privilege to user

Sudo users are in the `wheel` group (for rhel only, the group name is called `sudo` for debian based system). Grant sudo access by adding an existing user to `wheel` 
```shell
sudo usermod -aG wheel alice
```
## change the slurm quota for all users
 The following line limits the number of CPUs per user to 32, number of GPUs per user to 6
```shell 
sacctmgr modify qos normal set MaxTRESPerUser=cpu=32,gres/gpu=6
```

## add users to high usage GPU group
 To divide high usage users into a separate group for higher computing resource allocation, follow the steps below:
 
 Create a new Quality of Service (QOS) group called high:
```shell 
sacctmgr add qos high
```

 Set the GPU limit of the high QOS group to 10:
```shell 
sacctmgr modify qos high set MaxTRESPerUser=cpu=32,gres/gpu=10
```

 Put a user named feima into the high QOS group (the default group that all the users are in is normal)
```shell 
sacctmgr -i modify user where name=feima set QOS=normal,high
``` 

 Change the default QOS group of feima into high:
```shell 
sacctmgr -i modify user where name=feima set DefaultQOS=high
```

 Now user feima can use 10 GPUs for multiple jobs at the same time.

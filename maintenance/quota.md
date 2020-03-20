The user quota is setup on storage node to restrict the home directory of each user.

For detailed instruction, please see [quota large than 4TB](https://serverfault.com/questions/348015/setup-user-group-quotas-4tib-on-ubuntu).

Before executing these commands, make sure you are at storage node.

```shell
quotaon /data # start the quota monitoring
quotaoff /data # stop the quota monitoring
sudo repquota -s /data # check the quota
sudo setquota -u feng 1024G 1024G 0 0 /data # set the quota for user feng to use 1024G in maximum
```


Currently, two root cron jobs are responsible to monitor the manage node. The two programs are run every one minites, configured by
```
* * * * * /usr/local/bin/cpu_limit.sh >> /var/log/cpu_limit_cron.log 2>&1
* * * * * /usr/local/bin/cpu_monitor >> /var/log/cpu_monitor_cron.log 2>&1
```

You can find the source code of the two programs in `maintenance` folder. 

You can also check the log files.
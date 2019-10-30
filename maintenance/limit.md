This document applies to manage node only. This configuration is used for abuse use of manage node to run large experiment.


# CPU Limit
see `/usr/local/bin/cpu_limit.sh`.
I set this to a root cronjob, see by `sudo crontab -e`.
This cronjob run `cpu_limit.sh` every minute and check whether there are processes consumes more than 14 CPUs.
If The program consumes more than 14 CPUs, a hook process is started to limit it to at most 15 CPUs.
Also the program is run on backend.
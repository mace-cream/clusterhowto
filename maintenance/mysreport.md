### How to show the GPU usage report
***
Use the following command to show the usage report from a specific time. (`module load slurm` first.)

```
mysreport 2019-10-01
```

The time format is YYYY-mm-dd.

The report time unit is minute.

If you don't append a specific time, it will count from 7 days ago.

```
mysreport
```


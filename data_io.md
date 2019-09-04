# How to upload large files to server
Use `rsync`.

On Windows platform, you can use Mobaxterm local terminal to finish this job. First `cd /drives/c/[your large files on disk C]` to your file. Then 
```shell
rsync -av --progress your_file user@10.8.4.172:/home/user/[your path]
```
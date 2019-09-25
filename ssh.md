## About ssh in general
SSH client has a configuration file. On macos it is located at `/etc/ssh/ssh_config`. It forwards `LC_*` and `LANG` environment variables to the server you ssh to by default. If these environment variables are not set properly, they could cause problems. See [locale setting](https://askubuntu.com/questions/412495/setlocale-lc-ctype-cannot-change-locale-utf-8) and [ssh forwarding env](https://superuser.com/questions/513819/utf-8-locale-portability-and-ssh) for detailed explanation.

## How to upload files to server
### GUI
`sftp` is recommended
### scp
Using `scp` you can upload one file or file glob to or from the server.
### rsync
If you need to upload multiple files within a directory or upload large files, you can use `rsync`.

On Windows platform, you can use Mobaxterm local terminal to finish this job. First `cd /drives/c/[your large files on disk C]` to your file. Then 
```shell
rsync -av --progress your_file user@10.8.4.172:/home/user/[your path]
```
欲使用远程桌面，首先在[官网](https://www.cendio.com/thinlinc/download) 下载相应操作系统的客户端。

连接时只需输入IP地址，无需输入端口号。下图是 windows 客户端使用截图：

![](screenshot.png)

thinlinc 还支持用浏览器作为客户端登录(HTTPS)，使用 300端口。https://10.8.4.170:300。

# 注意
由于实验室很多同学在自己的`.bashrc` 文件中 load anaconda3 模块与系统 python 冲突，使用 vnc 会出现闪退的问题。建议在自己的HOME 目录下更改
`.bash_profile`文件：
```shell
4c4
< if [ -f ~/.bashrc ] && [ -z "$TLPREFIX" ]; then
---
> if [ -f ~/.bashrc ]; then
```

thinlinc 是商业软件，实验室买的授权是10个用户同时在线。
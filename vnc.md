本文档介绍远程桌面的使用，目前支持11个连接同时在线，未来有可能有所增加。

目前实验室部署的远程桌面有2类，均通过vnc连接，一类是 centos 7 操作系统(Linux), 是非虚拟化的；

另一类是用 VMWare 虚拟机部署的一台 Win 10 （公共账号用户名：lab2c，密码：guest，是Win10 普通用户）。

欲使用第一类远程桌面，首先在[官网](https://www.cendio.com/thinlinc/download) 下载相应操作系统的客户端（**专用**）。

连接时只需输入IP地址，无需输入端口号，用户名与密码与ssh 登录的用户名和密码相同。下图是 windows 客户端使用截图：

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

欲使用第二类远程桌面，首先下载 VNC 客户端，这里推荐 [realvnc](https://www.realvnc.com/en/connect/download/viewer/)
输入 `10.8.4.170:9327` 和密码 `lab2c` 即可连接，连接后输入Win10 公用账号和密码即可登录。
vmware 是商业软件，服务器部署的是免费版本，功能多有限制，本桌面目前只能一人使用。


# 官方VPN
目前使用清华深研院的VPN可以在外网连接实验室服务器。请从 [http://vpn.sz.tsinghua.edu.cn](http://vpn.sz.tsinghua.edu.cn) 下载相应的客户端。
下载安装打开VPN，服务器地址填 [https://vpn.sz.tsinghua.edu.cn](https://vpn.sz.tsinghua.edu.cn)，
VPN 初始用户名是学号，初始密码是身份证后8位。

由于该VPN 5分钟内无连接即自动断开，给使用SSH 造成不便，建议通过设置客户端`ssh_config`中添加：
```
ServerAliveInterval 30
ServerAliveCountMax 60
```
本地 ssh 每隔30s向 server 端 sshd 发送 keep-alive 包，如果发送 60 次，server 无回应断开连接。

虽然官网上可以下载Linux 的客户端，但客户端比较旧了，据说只支持 Ubuntu 16.04, Ubuntu 17.04.

# 自建内网穿透
如果你使用其他 Linux 发行版的操作系统，很可能无法使用官方VPN外网接入实验室服务器，此时可以用自建内网穿透的方式，
比如 [ssh 端口转发](https://www.cnblogs.com/zhaofeng-shu33/p/10685685.html) 或者 搭建[frp](https://github.com/fatedier/frp)
服务。由于智园网络不是很稳定以及这两种方式本身的局限性，可能会断掉。断掉后可以结合官方VPN重启。

# GFW
See [How to break through GFW](http://10.8.4.170/wiki/index.php/Guild_gfw)

# 官方VPN
官方VPN目前有两个，一个指校本部的 VPN（pulse secure），另一个指清华深研院的VPN (easy connect)
## 清华深研院的VPN 
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

## 校本部的VPN
智园和大学城的网络做过特殊处理，可以直接访问 info 等网站，但有些站点还不行（比如软件中心下载软件、激活 Win10、Matlab 等），此时要用到 校本部 VPN
客户端 pulse secure。
Windows 和移动端下载地址 在 [https://sslvpn.tsinghua.edu.cn](https://sslvpn.tsinghua.edu.cn) 页面可以找到。
Mac 和 Linux 下载地址学校官方没有提供，可以自行搜索，这里给出推荐地址（国外网站，客户端下载速度较慢）：
* [https://apple.lse.ac.uk/resources/PulseSecureStandardInstaller.pkg](https://apple.lse.ac.uk/resources/PulseSecureStandardInstaller.pkg)

使用时，地址是 https://sslvpn.tsinghua.edu.cn, 用户名和密码与 info 相关。
以下是 Mac 和 Linux 版本的使用截图
![mac](./mac.png)
# 自建内网穿透
如果你使用其他 Linux 发行版的操作系统，很可能无法使用官方VPN外网接入实验室服务器，此时可以用自建内网穿透的方式，
比如 [ssh 端口转发](https://www.cnblogs.com/zhaofeng-shu33/p/10685685.html) 或者 搭建[frp](https://github.com/fatedier/frp)
服务。由于智园网络不是很稳定以及这两种方式本身的局限性，可能会断掉。断掉后可以结合官方VPN重启。

# GFW
See [How to break through GFW](http://10.8.4.170/wiki/index.php/Guild_gfw)

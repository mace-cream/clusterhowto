# 官方VPN

## 清华深研院的VPN -- easy connect
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

## VPN of library of University Town of Shenzhen
If you need access to some electronical resources, you can also use VPN of the library.
See [lib vpn how to](https://lib.utsz.edu.cn/page/id-544.html?locale=zh_CN) for detail.
The username is the student id (prefix with 11).
The password is the one of universal identification authentication for UTSZ service. 

## 校本部的VPN
智园和大学城的网络做过特殊处理，可以直接访问 info 等网站，但有些站点还不行（比如软件中心下载软件、激活 Win10、Matlab 等），此时要用到 校本部 VPN
客户端 pulse secure。
Windows 和移动端下载地址 在 [https://sslvpn.tsinghua.edu.cn](https://sslvpn.tsinghua.edu.cn) 页面可以找到。
Mac 下载地址学校官方没有提供，可以自行搜索，这里给出开发这个客户端软件的公司提供的下载地址（国外网站，客户端下载速度较慢）：
* [MacOS](http://trial.pulsesecure.net/clients/ps-pulse-mac-9.0r4.0-b1731-installer.dmg)

官网上下载的Linux 的客户端，无法成功使用；[openconnect](https://www.infradead.org/openconnect/index.html) 可以用（不可用了）：
```
sudo /usr/local/sbin/openconnect --protocol=nc https://sslvpn.tsinghua.edu.cn
```

使用时，地址是 https://sslvpn.tsinghua.edu.cn, 用户名和密码与 info 相同。
以下是 Mac 版本的使用截图
![mac](./images/mac_juniper.png)



## GFW
See [How to break through GFW](http://10.8.6.22/wiki/index.php/Guild_gfw)


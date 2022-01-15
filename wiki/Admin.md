Miscellaneous Material
----------------------

### BCM Releated

![](BCM详细介绍.pdf "BCM详细介绍.pdf")

![](培训文档第二版.pptx "培训文档第二版.pptx")

![](Thinlinc-adminguide.pdf "Thinlinc-adminguide.pdf")

![](machine-learning-manual.pdf "machine-learning-manual.pdf")

![](admin-manual.pdf "admin-manual.pdf")

![](Yum_cheatsheet.pdf "Yum_cheatsheet.pdf")

### Pywikibot

Do not use this account manually. Username: Pywikibot Password:
pywikibot123

You can use this account to upload pictures in batch mode.

See [pywikibot](mediawikiwiki:Manual:Pywikibot "wikilink") for detail
usage.

Since pywikibot is a very old project based on python2, there are some
caveat before using this tool. For example, you need to use system
<kbd>/bin/python</kbd>. Maybe you need to tweak the code of pywikibot.
For the worst, if the target wiki is blocked by GFW, you need to specify
the proxy for pywikibot ( internally python2's <kbd>urlopen<kbd> )

On the server, you can specify the http proxy as

``` shell
export HTTPS_PROXY=http://localhost:8123 # listened by polipo
```

### VMWare 配置

实验室服务器上使用的是 VMware Player，是 VMWare
免费版本，锁定了一些高级功能，但这些功能可以结合命令行实现。

重启VMWare Service

``` shell
sudo /etc/init.d/vmware restart
```

打开网络配置器UI

``` shell
/usr/lib/vmware/bin/vmware-netcfg
```

VMWare 虚拟机常用的有两种配置：

`=== NAT 子网 ===`

网关（默认DNS Server）是 172.16.180.2（是 VMWare Server
虚拟化出来的），Windows 10 服务器采用固定 IP 172.16.180.3。

![](Net.png "Net.png")

目前 WIndows 10 Server 启用了 Open SSH 服务，内网ip 是 10.1.1.4，端口
22。

### Bridge Network

目前将 Win 10 加入子网 10.1.1.254，固定 ip 地址为 10.1.1.6，子网掩码
255.255.255.0，默认 DNS Server 和 网关为 10.1.1.254(管理节点内网 ip)，
在该网络中，计算节点，管理节点和 Win10 虚拟机彼此可以用 内网 ip
相互访问。 比如在管理节点中，通过下面的方式可ssh 登陆 Win10。

``` shell
ssh lab2c@10.1.1.4 # passwd: guest
```

Win10 设置桥接 Pulse Secure。

### TBSI Network

The institute IT department may change this without notice.

Wifi of TBSI-ZY: Tbsi\_12@34

TBSI 两个子网：10.8.15.\* 与 10.8.4.\* 彼此之间是连通的。也即在服务器
10.8.4.170 上可以ssh 登录 10.8.15 网段的机器。

李想存储服务器： 内网 ip 10.8.15.191 外网 ip 58.250.23.9，外网 ip
不可用。

学院 IIS/7.5 内网 ip 10.8.4.15

oa.sz.tsinghua.edu.cn：219.223.190.165

oracle 数据库服务器： 10.8.4.101 ssh 用户名 oracle。

``` shell
sqlplus "/as sysdba" 
select table_name from user_tables;
```

超微 10.8.4.171：80 端口用户名 ADMIN

10.8.4.210 mysql 用户名 root

10.8.4.105 ai.tbsi.edu.cn:10080 OA 登录页面

10.8.4.8:8080 identification management system

10.8.4.162 adminsion.tbsi.edu.cn

www.tbsi.edu.cn See [http://www.thinkphp.cn/code/5722.html
ThinkPHP安全性](http://www.thinkphp.cn/code/5722.html_ThinkPHP安全性 "wikilink")

10.8.4.130 弱口令用户：(刘伟锋)weifeng, anke, haitian jianing, lhanaf,
jinzhi, yujie

10.8.4.133: weak password user: wangdan

10.8.4.143 弱口令用户：chengwei, anke, jianing, suzhuo, tianyi, wangdan,
yaping, yujie, zhicheng

10.8.4.129 弱口令用户：chengwei, anke, jianing, suzhuo, tianyi, wangdan,
yaping, yujie, zhicheng

10.8.5.248 弱口令用户：dingjian

10.8.4.140 弱口令用户：anke, chengwei, zhicheng, jianing, haitian,
yujie, tianyi, wangyong, yaping, suzhuo, wangdan, dingjian, tanyang

10.8.4.141 弱口令用户：suzhuo

10.8.4.142 weak pass user: tianyi

10.8.5.200 weak pass users: wangyong

10.8.5.221 zhu-ty computer

10.8.5.127 dawei computer, username: blue

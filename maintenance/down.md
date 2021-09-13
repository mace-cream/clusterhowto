# 服务器宕机记录

## 2020/3/13
下午六时左右，管理员接到信息办来电，称有关政府部门拦截到了从服务器发出的挖矿病毒通信数据，致函信息办要求调查。之后管理员请求网关临时放行了攻击者IP以便调查，确实发现luis账户下存在占用资源极高的计划任务，之后立即终止相关进程，删除相关文件，更改luis账户的密码，病毒活动随之消失。此后对攻击路径的猜测为：初步确定攻击方式为SSH扫描。系统日志显示，通过某同学自用的反向代理服务，3月2日起存在大量的针对root和其他用户的恶意登录拒绝记录；3月10日攻击者疑似攻击弱口令普通用户luis成功并创建了病毒；3月10日起，存在大量该病毒因占用资源过多而被终止的记录。此后关闭了涉事内网穿透，重新确认了所有用户的密码安全等级，以防止类似事件再次发生。

## 2020/2/20
北京时间 14:00 左右管理服务器(10.8.6.22)宕机，这个时间是通过穿透代理查到的。该问题首先由李阳在 Users 微信群报出来(14:13)，多名同学反映问题确实存在，经测试 存储节点 10.8.6.21 也连不上，10.8.6.21 IPMI 也连不上，但 10.8.4.130 (2F 实验室服务器可以连上，赵丰尝试），初步断定是我方（2C）服务器集群全部挂掉，15.06 李阳决定亲自去机房重启服务器集群，15:50分赵丰在 Users 微信群发布服务器宕机通知。18点左右李阳
和学院IT某老师赶到机房，18:45 重启管理节点。各项测试本地正常，但仍无法远程 SSH 到服务器。19:20 线上咨询 Amax 工程师，初步断定是网线或者交换机的问题。20:30 通过将管理节点外网网线插到另一个实验室交换机上暂时解决远程连接的问题，从而得出 Amax 提供的外网交换机故障的结论。目前仍存在服务器不稳定的问题，可能是存
储节点外网网卡仍连接故障交换机的缘故。次日（2月21日）17:14 赵丰从管理节点系统日志发现通过IB网络连接 172.16.1.100（存储节点）经常连不上，可能是导致管理节点不正常的原因。通过使用备用存储节点暂时解决了这一问题，但原存储节点的数据暂时拿不到。2月22日下午3点左右，在 Amax 工程师的远程指导下，李阳前往机房，将原管理节点插到内网交换机的 IB 线换了一个插口，并把
管理节点接到别的实验室交换机上的以太网线重新插回到自己实验室的前置交换机上。测试各项指标正常。目前初步断定原管理节点插到内网交换机的 IB 线接口松动，以及前置交换机可能存在问题。

## 2020/1/5
由于电力检修，服务器集群于12:30左右正常关机。经核实，当天机房实际并未发生电力中断。15：30，在尝试重新启动服务器集群时，存储节点电源键失灵。随后管理节点和计算节点正常开机，赵丰同学临时挂载了其它存储源备用。次日，Amax工程师上门服务，对存储节点主板进行了未知操作后，电源键重新可用，存储节点顺利上线。

## 2020/4/13
this morning from 10:30am-12pm engineers will perform some testing and maintenance tasks on our server.  some network interruptions are expected. 现在我们换了一根网线，工程师说可能是以前的网线过长，如果有质量问题容易受电磁波干扰。。

## 2021/2/3
20.30 Weitao Tang report down of manage node

20.34 web access ok

21:00 call zhiyuan wu for remote assistant

0:30 restart the server

Next day, the engineer tries to find the reason

11:20, computing nodes return to normal

Afterwards: cluster suffer numerous down during February to March since this crash, with unknown reason. And everything seems to be OK after reboot. The AMAX engineer give his theory that it may be a storage unstable because of overheating. We decide to keep cabin door of our server open to alleviate the problem. It works, amazing.

## 2021/7/2
7/2 21:00 Power failure of iPark-C2 building, all connection lost.

7/5 14:00 Temporal Power supplement and cluster reboot. We only open bcm/storage/Node01 because IT refused further booting as concern of 'limited power', though we heard Electric Engineer said its safe. Also because of movement of institute network server, 10.8.4.170 no more works. We still can't access cluster.

7/9 17:00 和IT扯了几天皮，他们一直不给放新的IP，却推脱让我们找厂家，请出老师出马去问时却又称“不知道进展”。We have to move previous IPMI wire on Node05 (which use 10.8.6.0/24 network and not being influenced) to our cluster switch and use this as our new global interface. And cluster back to service after 7 days down.

7/26 Full recovery. Total shutdown time 24 days.
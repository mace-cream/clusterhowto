# Network Setting

## 1. External network 
We use fixed IP for all external interface. Here are some useful information (update: 2021/7/10):

Available IP pool: 10.8.6.10 - 10.8.6.30

Mask: 255.255.255.0

Gateway: 10.8.6.254

DNS: 10.8.2.200

## 2. How to Set External Network Parameters

Two options to change network parameters for bcm: 

(1) Temporary change: modify scripts in `/etc/sysconfig/network-scripts`. And use `systemctl restart network` to make it valid. This file will be reset by bright-view after reboot. 

(2) Permanent change: Check web interface of [bright-view] (https://10.8.6.22:8081/bright-view/#!/auth/login), modify (a). Network Tab (2nd Tab) -> Networks -> externalnet -> edit -> Settings, and (b). Devices Tab (5th Tab) -> Head node -> bcm -> Edit -> Settings -> Interfaces. Settings in (a) determines overall network parameter for cluster, while (b) determines setting for specific devices.

Storage Node is not governed by bright-view. It's located in `/etc/NetworkManager/system-connections/`
You can modify it with some Network Setting GUI or command line tool. Don't forget to restart the network interface before the new static
ip address takes effect.

## 3. IP Pool Status
Since we are using fixed IP setting, make sure there's no collision when you pick your favorite number.

| IP        | Usage                    |
| --------- | ------------------------ |
| 10.8.6.21 | Storage Node External IP |
| 10.8.6.22 | Manage Node External IP  |
| 10.8.6.20 | Storage Node IPMI        |
| 10.8.6.23 | Manage Node IPMI         |
| 10.8.6.14 | Node04 IPMI              |
| 10.8.6.15 | Node05 IPMI              |

## 4. Internal Network
We also have three Internal Network for cluster:

|Network|Description|
| --------- | ------------------------ |
|10.1.1.0/24|bright view management network|
|10.1.2.0/24|IPMI network for Node01-03|
|172.16.1.0/24|High speed NFS ib network|
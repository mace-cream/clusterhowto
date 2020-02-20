使用ssh登录的用户名和密码登录 [seafile cloud storage](http://10.8.4.170:8030/)。

## Service starting up
In the case where seafile and seahub services are down, we can reboot it manually by
```bash
cd /home/feng/seafile-server/seafile-server-7.0.5
bash seafile.sh start
bash seahub.sh start
```

## Advantages

* 微信电脑与手机互传文件有诸多限制，替代之。
* fast speed and large space
* mobile client support

## Use cases

1. Download the `seafile` mobile client from the Huawei Market.

2. Add our server and login use your ssh account.

![login](./images/seafile-android-1.jpg)

3. Upload your files from mobile to the server.

![upload](./images/seafile-android-2.jpg)

4. (optional) Download your files from desktop broswer client.
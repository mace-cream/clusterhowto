Simple Solution
---------------

-   If you are in lab2c, you can connect google and wikipedia since they
    are in the whitelist of TBSI vpn. The speed is very fast.
-   If you are not in lab2c, you can connect the lab2c server by
    official vpn of shenzhen tsinghua. With the help of remote desktop,
    you can connect google. See
    [http://10.8.4.170:88/yang/clusterhowto/blob/master/vnc.md
    vnc](http://10.8.4.170:88/yang/clusterhowto/blob/master/vnc.md_vnc "wikilink")
    on how to use remote desktop.

If you need to visit more blocked website, you need to do it by
yourself.

Prerequisite
------------

-   You need a server abroad which has a fixed public IP address and you
    can login through ssh.
-   You need to install the client software on your local device.

Shadowsocks How to
------------------

Shadowsocks has implementation in Python, Go, C and Rust. In my opinion,
C implementation has the best performance. The well-known
**shadowsocks-libev** is a cross-platform server or client software
implemented in C, and can be found at
[https://github.com/shadowsocks/shadowsocks-libev
shadowsocks-libev](https://github.com/shadowsocks/shadowsocks-libev_shadowsocks-libev "wikilink")
On different Operating Systems, **shadowsocks-libev** has pre-built
binaries, which can be installed by package manager.

Below we use Debian strech to install **shadowsocks-libev** and deploy
it as a shadowsocks server. And we install **shadowsocks-libev** as a
command line client on Debian buster. For Windows platform, a GUI client
is preferable, see [https://github.com/shadowsocks/shadowsocks-windows
shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows_shadowsocks-windows "wikilink")
for detail.

You can start \`ss-local\` as a service on client machine:

``` shell
sudo systemctl start shadowsocks-libev-local@config
```

### Server Configuration

After installation of **shadowsocks-libev**, you should

1. get the ip address of the virtual machine. For example, you can use
the following command

``` shell
hostname -I
```

2. edit the configuration files (located at
*/etc/shadowsocks-libev/config.json* ), put down your external ip
address instead of "3.113.5.96"

``` json
{
"server":["3.113.5.96"],
"mode":"tcp_only",
"server_port":8388,
"local_port":1080,
"password":"abc",
"timeout":60,
"plugin":"/home/admin/v2ray-plugin_linux_amd64",
"plugin_opts":"server",
"reuse_port":true,
"method":"chacha20-ietf-poly1305"
}
```

3. Notice that we use the plugin to enhance the transportation. It adds
the obfuscation feature. Server and Client should use the same plugin.
There are some choices of plugin but only one can be used. We use
[http://github.com/shadowsocks/v2ray-plugin
v2ray-plugin](http://github.com/shadowsocks/v2ray-plugin_v2ray-plugin "wikilink")
in our configuration, of which binaries for all platform can be
downloaded from GitHub.

4. The client shares the same configuration with the server, except that
on *plugin\_opts* entry is present. Another notation is that for client,
the daemon process uses **ss-local** instead of **ss-server**.

### Trouble shooting

You can start the server of client on the command line with *-f
path\_to\_config\_file -v* parameters. Also, you can check the system
log file for daemon process problem.

### Browser

I recommend to use Google Chrome to set the browser proxy, which is more
flexible than system proxy. However, since the chrome store is blocked.
You need to enable the system proxy first to install the plugin,
**SwitchyOmega**.

We use Debian buster client as an example. First you need to enable
system network proxy. Selecting socks proxy. Then open chrome to visit
[https://chrome.google.com/webstore/search/SwitchyOmega
SwitchyOmega](https://chrome.google.com/webstore/search/SwitchyOmega_SwitchyOmega "wikilink").
Since this web page has some static files to load. It may take some time
to open it. Then you can install SwitchyOmega directly from the web
page. The size of this extension is about 1 MB. Please wait patiently.

After installation, you can set the browser proxy and enable the auto
switch feature. The proxy is called *SOCKS* with address *127.0.0.1* and
port number 1080.

### High Availability

For some shadowsocks client, it is possible to configure multiple
servers for the purpose of high availability.

### Available client configuration

Currently there is one socks client on our manage node. First you need
to login to bcm manage node. Then check <kbd>
/etc/shadowsocks-libev/config.json </kbd> content. The binary of v2ray
can be downloaded using <kbd> wet </kbd> from the command line. Before
using <kbd> wet </kbd>, remember to set the environment variable of
https proxy to the local shadowsocks client.

### Android client

If you want to use Twitter, Telegram, Slack etc. You need to use a
client to traffic the route to your remote vpn server. For shadowsocks
solution you can install
[shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android)
and enable the corresponding plugin for better security. Then you can
configure the client to bypass the traffic for specific APPs.

### IOS client

Iphone only allows installing app from its own store. Besides, you need
an overseas account to download the vpn app. Recommended apps include
*Potatso Lite* and *Shadowrocket*. The former has some limitations, for
example, only browser is supported to use the proxy. The functionality
of the latter is better but it requires purchase in App store of overseas.
To buy *Shadowrocket* in such a case, you need an overseas account and an overseas credit card.

V2ray How to
------------

**V2ray** is the next generation of proxy software and can be regarded
as a superset of shadowsocks.

### Command line Client
The program `v2ray` can be used to start a server or client.
For backward compatibility, set the environment variable `V2RAY_VMESS_AEAD_FORCED=false`
on the server side if `alterid` is not equal to zero.

### GUI Client

`Qv2ray` is recommended since it is cross-platform. However, it is no
longer maintained.

### Iphone Client
It's known that only *Shadowrocket* works.

### Traffic counting
The default server program has the ability to count the traffic amount for each client users.
The configuration file needs to be modified.

### Trouble shooting
Change the loglevel to debug in the configuration file.
```JSON
"log": {
    "loglevel": "debug"
}
```
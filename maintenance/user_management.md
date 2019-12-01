集群中用户管理不同于普通单台linux 服务器，如果用 `useradd` 等命令只能在单机上建用户，使用LDAP 可以解决一个用户访问多台机器的问题。
目前服务器部分同学（2018级及之前）的账号存放在管理节点的 LDAP 数据库中，包括 NFS 的账号也在。

不在 LDAP 数据库中的同学账号无法ssh登录存储节点和管理节点 jupyter。

## Local user management
```
userdel username # preserve home
```

# Search
```
ldapsearch -x 'uid=weijiafeng'
```

# Reset Password
```
ldappasswd -s 123456 -W -D 'cn=root,dc=cm,dc=cluster' -x 'uid=weijiafeng,dc=cm,dc=cluster'
```
`-s` 参数后面跟新的密码
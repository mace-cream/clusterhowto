# this script is used to check whether username and password are
# the same for given ip and port

import socket
from ssh2.session import Session
from ssh2.exceptions import AuthenticationError

ip = '10.8.4.170'
port = 22
# userlist = ['lewenyuan','lianjing','riccardo','tanyang','tianzhou','ziyanzheng']
# userlist = ['wangbin','lirong','jielian','liangcheng','tianyu','hutianyu','jiarongli','anzhicheng','bunchalit','jackkuo','jinggewang',
#             'luis','jihongwang','lewenyuan','tanyang','ziyanzheng','yurunpeng']
userlist = []
for line in open('recore.txt','r'):
    userlist.append(line.replace('\n',''))
def ssh_login(user):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    sock.setblocking(1)
    session = Session()
    session.handshake(sock)
    try:
        session.userauth_password(user,user)
    except AuthenticationError:
        return
    print(user)

def ssh_login2(user):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    sock.setblocking(1)
    session = Session()
    session.handshake(sock)
    try:
        session.userauth_password(user,'password')
    except AuthenticationError:
        return
    print(user)

def ssh_login3(user):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    sock.setblocking(1)
    session = Session()
    session.handshake(sock)
    try:
        session.userauth_password(user,'123456')
    except AuthenticationError:
        return
    print(user)

if __name__ == '__main__':
    print('username------')
    for user in userlist:
        ssh_login(user)
    print('password-------')
    for user in userlist:
        ssh_login2(user)
    print('123456------')
    for user in userlist:
        ssh_login3(user)
    


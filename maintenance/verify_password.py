# this script is used to check whether username and password are
# the same for given ip and port
# module load anaconda2/py2
# python verify_password.py
import socket
from ssh2.session import Session
from ssh2.exceptions import AuthenticationError

ip = '10.8.4.170'
port = 22
userlist = ['lewenyuan','lianjing','riccardo','tanyang','tianzhou','ziyanzheng']

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

if __name__ == '__main__':
    for user in userlist:
        ssh_login(user)

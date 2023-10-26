import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
print("Host Name is:" + h_name)
print("Computer IP Address is:" + IP_addres)

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/", perm="elradfmwMT")
authorizer.add_anonymous("/")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("10.1.0.127", 21), handler)
server.serve_forever()

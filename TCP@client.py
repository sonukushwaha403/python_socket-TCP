import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.254.17",1234))
print(s.recv(1024))
s.send(b" this is again sonu from client side now")
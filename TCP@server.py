import socket
import threading
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip=""
port=1234
s.bind((ip,port))
s.listen()
def iiec(c,addr):
    print(addr)
    c.send(b"i am from server@sonu")
    data=c.recv(1024)
    print(data)

while True:
    c,addr=s.accept()
    t1=threading.Thread(target=iiec , args=(c,addr))
    t1.start()

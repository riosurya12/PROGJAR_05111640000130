import socket
import sys

s = socket.socket()
s.connect(("localhost",38000))
f = open ("file_1.pdf", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()

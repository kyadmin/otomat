#!/usr/bin/env python
import socket
import os,time
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('172.16.209.243',18888))
#f=open('aa','wb')
ss.sendall('wokao sile')
time.sleep(2)
ss.send('FOE')
data=ss.recv(1024)
print "server dafu %s"%data
ss.close()

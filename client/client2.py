#!/usr/bin/env python
import socket
import os,time,sys

data = "x" * 102400   #1MB of data
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('172.16.209.243',18888))
#f=open('aa','wb')

byteswritten = 0
while byteswritten < len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 1024,len(data))
    byteswritten += ss.send(data[startpos:endpos])
    #time.sleep(2)
    #ss.send('FOE')
    #data=ss.recv(1024)
    #print "server dafu %s"%data
    sys.stdout.write("Wrote %d bytes\r" % byteswritten)
    sys.stdout.flush()
ss.shutdown(1)

print "All data sent."
while True:
    buf = ss.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)

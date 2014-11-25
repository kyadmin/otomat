#!/usr/bin/env python
import socket
import os,time,sys

data = "=" * 10240000   #10MB of data
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('172.16.209.243',18888))
#ss.connect(('172.16.209.110',18888))
#f=open('aa','wb')

byteswritten = 0
while byteswritten < len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 8092,len(data))
    byteswritten += ss.send(data[startpos:endpos])
    time.sleep(0.1)
    data += ss.recv(8092)
    #ss.send('FOE')
    #print "server dafu %s"%data
    sys.stdout.write("Wrote %d bytes\r" % byteswritten)
    sys.stdout.flush()
ss.shutdown(1)

print "All data sent."
while True:
    buf = ss.recv(8092)
    if not len(buf):
        break
    sys.stdout.write(buf)

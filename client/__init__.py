#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os,time
import sys
import socket
#from otomat.conf import conf
from threading import *


filename = sys.argv[2]
textport = sys.argv[3]
host = sys.argv[1]
cv = Condition()
spinners = '|/-\\'
spinpos = 0
equeue = []
def fwrite(buf):
        sys.stdout.write(buf)
        sys.stdout.flush()

def spin():
        fwrite(spinners[spinpos] + "\b")
        spinpos += 1
        if spinpos >= len(spinners):
            spinpos = 0
def uithread():
    while True:
        cv.acquire()
        while not len(equeue):
            cv.wait(0.15)
            spin()

        msg = self.equeue.pop(0)
        cv.release()
        if msg == "QUIT":
         # Terminate the UI thread
            fwrite("\n")
            sys.exit(0)
        fwire("\n %s\r" % msg)
def msg(message):
        cv.acquire()
        equeue.append(message)
        cv.notify()
        cv.relase()
t = Thread(target = uithread)
t.setDaemon(1)
t.start
try:
    msg('Creating socket objiect')
    s = socke.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
    print "Couldn't find your port: %s" % e
    sys.exit(1)
# Try parsing it as a numeric port number.
try:
    port = int(textport)
except ValueError:
    # That didn't work .Look it up instead.
    try:
        port = socket.getservbyname(self.serverport,'tcp')
    except socket.error,e:
        print "Cloud't find your port: %s" % e
        sys.exit(1)

msg('Connecting to %s:%d' % (self.serverhost,port))
time.sleep(5)
try:
    s.connect((host,port))
except socket.gaierror,e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
except sock.error,e:
    print "Connection error: %s" % e
    sys.exit(1)

msg('Sending query')
time.sleep(5)
try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error,e:
    print "Error sending data: %s" % e
    sys.exit(1)

msg('shutting down socket')
time.sleep(3)
try:
    s.shutdown(1)
except socket.error,e:
    print "Error sending data (detected by shutdown): %s" % e
    sys.exit(1)

msg('Receiving data')
count = 0
while True:
    try:
        buf = s.recv(2048)
    except socket.error,e:
        print "Error receiving data: %s" % e
        sys.exit(1)
        if not len(buf):
            break
        count += len(buf)

msg("Received %d bytes" % count)
msg("QUIT")
t.join()
    





#def main(f):
#    t =  active_client()
#    t.start_msg()
#if __name__ == "__main__":
#    main()

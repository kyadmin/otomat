#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os,time
import sys
import socket
#from otomat.conf import conf
from threading import *


class active_client:
    def __init__(self,filename=None,insert=None):
        self.filename = filename
        cnf = conf.files_conf_check(self.filename)
        self.serverport = cnf.server_port() 
        self.serverhost =  cnf.server_host()
        self.clientport = cnf.client_port()
        self.clienthost = cnf.client_ip()
        self.insert = insert
        self.cv = condition()
        self.spinners = '|/-\\'
        self.spinpos = 0
        self.equeue = []
    def fwrite(self,buf):
        sys.stdout.write(buf)
        sys.stdout.flush()

    def spin(self):
        fwrite(spinners[self.spinpos] + "\b")
        spinpos += 1
        if spinpos >= len(spinners):
            spinpos = 0
    def uithread(self):
        while True:
            self.cv.acquire()
            while not len(self.equeue):
                self.cv.wait(0.15)
                spin()

            msg = self.equeue.pop(0)
            self.release()
            if msg == "QUIT":
                # Terminate the UI thread
                fwrite("\n")
                sys.exit(0)
            fwire("\n %s\r" % msg)
    def msg(self,message):
        self.cv.qcquire()
        self.equue.append(message)
        self.cv.notify()
        self.cv.relase()
    t = Thread(tagrget = uithread())
    t.setDaemon(1)
    t.start
    try:
        msg('Creating socket objiect')
        s = socke.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,e:
        print "Couldn't find your port: %s" % e
        sys.exit(1)
    # Try parsing it as a numeric port number

    #msg('Connecting to %s:%d' % (self.serverhost,self.serverport))
    msg('Connecting to %s:%d' % ("172.16.209.243",18888))
    time.sleep(5)
    try:
        #s.connect((self.serverhost,self.serverport))
        s.connect(("172.16.209.243",18888))
    except socket.gaierror,e:
        print "Address-related error connecting to server: %s" % e
        sys.exit(1)
    except sock.error,e:
        print "Connection error: %s" % e
        sys.exit(1)

    msg('Sending query')
    time.sleep(5)
    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % self.insert)
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
    





def main(f):
    t =  active_client(f,insert)
    t.server_receive()
if __name__ == "__main__":
    main("otomat.cnf","/")

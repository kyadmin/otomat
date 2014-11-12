#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os,time
import sys
import socket
from otomat.conf import conf


class active_server:
    def __init__(self,filename=None,insert=None):
        self.filename = filename
        cnf = conf.files_conf_check(self.filename)
        self.serverport = cnf.server_port() 
        self.serverhost =  cnf.server_host()
        self.clientport = cnf.client_port()
        self.clienthost = cnf.client_ip()
        self.insert = insert

    def server_receive(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.clienthost,int(self.clientport)))
        s.listen(2)
        s.connect((self.serverhost,int(self.serverport)))
        try:
            while True:
                conn,add=s.accept()
                '''
                注：服务器端一次只接收6个字节的数据.
                '''
                while True:
                    for f in self.insert:
                        s.sendall(f)
                        #s.send('EOF')
                        data=s.recv(1024)
                        print "server Dafu %s" %data
                    time.sleep(60)
                    s.close()
        except KeyboardInterrupt:
            print "you have CTRL+C,Now quit"
        s.close()

def main(f):
    t =  active_server(f)
    t.server_receive()
if __name__ == "__main__":
    main("otomat.cnf")

#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os
import sys
import socket
from otomat.conf import conf


class active_server:
    def __init__(self,filename=None):
        self.filename = filename
        cnf = conf.files_conf_check(self.filename)
        self.port = cnf.server_port() 
        self.ip =  cnf.server_ip()

    def server_receive(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.ip,int(self.port)))
        s.listen(2)
        try:
            while True:
                conn,add=s.accept()
                '''
                注：服务器端一次只接收6个字节的数据，我让读取进入循环，
                然后不断累加到data2中，当读取到EOF时，退出打印data2，
                当读取FOE时，退出打印data2，（EOF和FOE是客户端发送完数
                据时发送的结束符），当接收到CTRLC+C时，关闭socket
                '''
                while True:
                    data2=''
                    data1=conn.recv(6)
                    if data1=='EOF':
                        conn.send('hello clietn1')
                        break
                    if data1=='FOE':
                        conn.send('hello client2')
                        break
                    data2+=data1
                    print data2
                    
        except KeyboardInterrupt:
            print "you have CTRL+C,Now quit"
        s.close()

def main(f):
    t =  active_server(f)
    t.server_receive()
if __name__ == "__main__":
    main("otomat.cnf")

#!/usr/bin/python

"""
####################################################################
Program spider,version 0.01
This program will connect to a web server,send a request and waiting
to receive a reply,then print the reply out to standard output
####################################################################
"""
from socket import *

HOST = '192.168.1.1'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST,PORT)
User_Agent = 'Spider/0.01'
Version = 'HTTP/1.0'

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

data = 'Get / %s\r\nHost: %s\r\nUser_Agent: %s\r\n\r\n' %(Version,HOST,User_Agent)

#print data
tcpCliSock.send(data)
while True:
	data = tcpCliSock.recv(BUFSIZ)
	print data
	if not data:
		break
#print data
tcpCliSock.close()

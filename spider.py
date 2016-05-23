#!/usr/bin/python

"""
####################################################################
Program spider,version 0.01
This program will connect to a web server,send a request and waiting
to receive a reply,then print the reply out to standard output
####################################################################
"""
import sys
import string
from socket import *

nargv = len(sys.argv)
if nargv != 3:
	print 'Usage %s host port' %sys.argv[0]
	quit()
HOST = sys.argv[1]
PORT = string.atoi(sys.argv[2])
BUFSIZ = 1024
ADDR = (HOST,PORT)
User_Agent = 'Spider/0.01'
Version = 'HTTP/1.0'

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

data = 'Get / %s\r\nHost: %s\r\nUser_Agent: %s\r\n\r\n' %(Version,HOST,User_Agent)

tcpCliSock.send(data)
while True:
	data = tcpCliSock.recv(BUFSIZ)
	print data
	if not data:
		break
tcpCliSock.close()

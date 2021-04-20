#!/usr/bin/env python3
#Client machine
import socket

RHOST = '127.0.0.1'
RPORT = 1111
VAR = ['this','is','DATA']
SND_DATA = 'D A T A '.encode()
timeout = 2

C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
C_SOCK.settimeout(timeout)

try:
     C_SOCK.connect((RHOST, RPORT))
     print ("Connection successful.")
     for element in VAR:
          C_SOCK.send(SND_DATA)
     RCV_DATA = C_SOCK.recv(1024)
     print (RCV_DATA)
     C_SOCK.close()

except socket.error as e:
     print ("Connection failed")
     C_SOCK.close()

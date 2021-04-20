#!/usr/bin/env python3
#Client machine
import socket

FILE = open('names.txt', 'r')

RHOST = '127.0.0.1'
RPORT = 9000

SND_DATA = FILE.read().encode('utf-8')
timeout = 2

C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
C_SOCK.settimeout(timeout)

try:
     C_SOCK.connect((RHOST, RPORT))
     print ("Connection successful.")
     C_SOCK.send(SND_DATA)
     RCV_DATA = C_SOCK.recv(1526)
     print (RCV_DATA)
     C_SOCK.close()
     FILE.close()
except socket.error as e:
     print ("Connection failed")
     C_SOCK.close()
     FILE.close()

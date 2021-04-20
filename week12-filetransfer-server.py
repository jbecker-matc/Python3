#!/usr/bin/env python3
#Server machine
import socket

LHOST = ''
LPORT = 9000
RCV_DATA = ""


L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while(1):
     L_SOCK.listen(1)
     L_CONN, addr = L_SOCK.accept()
     print ('Connected by', addr)
     while 1:
               RCV_DATA = L_CONN.recv(1526)

               if not RCV_DATA: 
                    break
               RCV_FILE = RCV_DATA.decode('utf-8')
               FILE = open('newnames.txt','w')
               FILE.write(RCV_FILE)
               FILE.close()

     L_CONN.close()


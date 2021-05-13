#!/usr/bin/env python3

#The setup
import requests
import argparse
import bs4
import json
import socket

parser = argparse.ArgumentParser(description='Final exam parser')

parser.add_argument('-ip', dest='IPAddress', default='8.8.8.8', type=str, help='Enter IP address')

parser.add_argument('-f', dest='funcnum', default='1', type=int, help='Enter a simple integer 1-5')

URL = parser.parse_args()

print("Name: Jon Becker")
print("HTTP://"+str(URL.IPAddress)+"/q"+str(URL.funcnum))


#Function 1: get_response
if URL.funcnum == 1:
     func1 = requests.get("http://"+str(URL.IPAddress)+"/q"+str(URL.funcnum))
     print(f"Text: {func1.text[:250]}")

#Function 2: parse_string
if URL.funcnum == 2:
     func2 = requests.get("http://"+str(URL.IPAddress)+"/q"+str(URL.funcnum))
     func2soup = bs4.BeautifulSoup(func2.text, "html.parser")
     ele = func2soup.select('H3')
     eleslice = str(ele)
     print("Slice:", eleslice[7:49:3])

#Function 3: parse_header
if URL.funcnum == 3:
     func3 = requests.get("http://"+str(URL.IPAddress)+"/q"+str(URL.funcnum))
     ele3 = func3.headers
     print(ele3['MATC-HEADER'])

#Function 4: parse_json
if URL.funcnum == 4:
     func4 = requests.get("http://"+str(URL.IPAddress)+"/q"+str(URL.funcnum))
     func4soup = json.loads(func4.text)
     for key in func4soup:
           for key2 in func4soup[key]:
                if key2["title"] == "1984":
                     print(key2["author"])

#Function 5: socket_client
RHOST = str(URL.IPAddress)
timeout = 2
if URL.funcnum == 5:
     RPORTS = range(5000,6000)
     for seq in RPORTS:
          C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          C_SOCK.settimeout(timeout)

          try:
               C_SOCK.connect((RHOST,seq))
               print(f"Connection: {seq}::Port Open")
               C_SOCK.send("secret".encode('utf-8'))

               RCV_DATA = C_SOCK.recv(1024)
               C_SOCK.close()
               print(RCV_DATA.decode('utf-8'))
          except socket.error as e:
               C_SOCK.close

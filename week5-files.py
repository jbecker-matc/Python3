#!/usr/bin/env python3
"""
Usage: ./week5-files.py
"""

hFile=open("/etc/passwd")
strfiletext=hFile.read()

print(f"/etc/passwd is {len(strfiletext)} bytes long")
print("The len() function counts the bytes in a string a displays it as a number.")
print("Use strfiletext=hFile.read() to put the entire contents of a file in a single string.")
print("\n")

hFile=open("/etc/passwd")
listfiletext=hFile.readlines()

print(f"/etc/passwd is {len(listfiletext)} bytes long")
print("In other words, the len() function calculates the length of a string.")
print("Use listfiletext=hFile.readlines() to put the contents of a file into a list.")
print("\n")


count=0
varlist=[]

with open("/etc/passwd") as hFile:
     varlist=hFile.read(1)
     while len(varlist) < 3040:
          lengthInfo="{len(varlist)}"
          varlist.append(count)
          count=count+1
          print(varlist)
          varlist=hFile.readline()

print("Total: Count")

"""
I just couldn't figure the last one out. I tried a number of different possibilities,
some which gave me a good looking output but didn't calculate the total length. I worked on
this down to the wire, which is why it's a bit late.
"""

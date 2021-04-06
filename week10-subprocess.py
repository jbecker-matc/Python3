#!/usr/bin/env python3
import subprocess
#('ps -axco command')

myproc = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)
myproclist = myproc.stdout.decode().split('\n')

for element in myproclist:
     print(element)

print (len(myproclist[1::]))

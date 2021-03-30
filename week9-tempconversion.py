#!/usr/bin/env python3
"""
Converts temperature between Celsius and Fahrenheit, or vice versa
"""

from f2c import ftoc
from c2f import ctof

print ("Select a conversion: ","\n","1: Fahrenheit to Celsius","\n","2: Celsius to Fahrenheit")

input_conv = input("> ")

if input_conv == "1":
     usertempf = int(input("Enter temperature: "))
     print (ftoc(usertempf))

elif input_conv == "2":
     usertempc = int(input("Enter temperature: "))
     print (ctof(usertempc))

else:
     print ("Error: please retry.")

#!/usr/bin/env python3
"""
Demonstrates slicing and loops
Usage: ./week4-sequences.py
"""

varString = "Here is a nice string to slice"
varTuple = ( "Here", "is", "a", "nice", "tuple", "to", "slice" )
varList = [ "Here", "is", "a", "nice", "list", "to", "slice" ]

print ( 'a.', varString[3:],"\n"
'b.', varString[:3],"\n"
'c.', varString[3:13],"\n"
'd.', varString[0:29:2],"\n"
'e.', varString[::-1],"\n"
"\n"
'a.', varList[::-1],"\n"
'b.', varList[2::-1],"\n"
'c.', varList[2:4],"\n"
'd.', varList[0::3],"\n"
'e.', varList[1:],"\n" )
"\n"
for elements in varString:
     print(f"{elements}")

print ( "\n" )

for elements in varList:  
     print(f"{elements}")

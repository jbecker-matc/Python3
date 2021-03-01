#!/usr/bin/env python3
"""
Prints boolean examples
Usage ./week6-boolean.py
"""

print (bool(True and True)),"\n"
print (bool(False and True)),"\n"
print (bool(1==1 and 2==1)),"\n"
print (bool(0)),"\n"
print (bool("")),"\n"
print (bool(0.0)),"\n"
print (bool(not 0)),"\n"
print (bool("test"=="test")),"\n"
print (bool(1==1 or 2!=1)),"\n"
print (bool(True and 1==1)),"\n"
print (bool(False and 0!=0)),"\n"
print (bool(True or 1==1)),"\n"
print (bool("test"=="testing")),"\n"
print (bool(1!=0 and 2==1)),"\n"
print (bool("test" != "testing")),"\n"
print (bool("test" == 1)),"\n"
print (bool(1==1 and not("testing"==1 or 1==0))),"\n"
print (bool("chunky"=="bacon" and not(3==4 or 3==3))),"\n"
print (bool(3==3 and not ("testing" or "Pythong"=="Fun")))

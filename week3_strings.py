#!/usr/bin/env python3
"""
Demonstrates strings
Usage ./week3_strings.py
"""

varRed="Red"
varGreen="Green"
varBlue="Blue"
varName="Timmy"
varLoot=10.4516295

print (f"Hello {varName}"),"\n"

print (f"{varRed}-{varGreen}-{varBlue}"),"\n"

print (f"Is this {varGreen.lower()} or {varBlue.lower()}?"),"\n"

print (f"My name is {varName.upper()}"),"\n"

print (f"[{varRed:+^7}]"),"\n"

print (f"[{varGreen:=<7}]".casefold()),"\n"

print (f"[{varBlue:*>9}]"),"\n"

print (varBlue*10),"\n"

print (varLoot),"\n"

print (f"{varLoot: <.1f}"),"\n"

print (f"I have ${varLoot: <.2f}"),"\n"

print (f"[{varRed:$^10}][{varGreen:$^10}][{varBlue:$^10}]"),"\n"

print (f"[{varRed[::-1]: ^7}][{varGreen: ^9}][{varBlue[::-1]: ^8}]"),"\n"

print (f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]"),"\n"

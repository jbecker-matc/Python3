#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description="This is week11-argparse.py script")

#================================ Add Arguments =================================================

##Text
parser.add_argument('-m', dest='Basic', help='Enter some text')

##Integer
parser.add_argument('-i', '--integer', dest='varInt', metavar='[an integer]',
default=0, type=int, required=False, help='<required> Enter a simple integer')

##Floatparse
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=0.0,
type=float, required=False, help='Enter a simple Float')

##String
parser.add_argument('-s', '--string', dest='varStr', metavar='[a string]',
default='hello', type=str, required=False, help='Enter a simple String')

##List (space delimited set of Strings)
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+',
required=False, help='Enter a list of strings (space delimited)')

##Boolean
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true',
required=False, help='Toggle from default False to True')

parser.add_argument('-f', '--set-false', dest='bool_f', default=True, action='store_false', 
required=False, help='Toggle from default True to False')

##Version
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

#================================ Using the Parser =================================================

args = parser.parse_args()

if len(sys.argv) == 1:
     parser.print_help()
     exit(0)

print("Value of '-m': " + str(args.Basic))
print("Value of '-i': " + str(args.varInt))
print("Value of '-d': " + str(args.varFloat))
print("Value of '-s': " + str(args.varStr))
print("Value of '-t': " + str(args.bool_t))
print("Value of '-f': " + str(args.bool_f))

print("=== List ===",'\n',args.varList)
for arg in args.varList:
     print(arg)

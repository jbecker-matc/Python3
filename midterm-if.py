#!/usr/bin/env python3
#I can't figure out why it's reading 2431 lines instead of 2425
print ("Name: Jon Becker"),"\n"

Total = 0
linenumber = 0
with open("Midterm-if.txt", "r") as a:
     for line in a.readlines():
          if line != " ":
               linenumber += 1
          if line.find("gmeach18@ed.gov") >= 0:
               Total += linenumber
          elif line.find("248.253.63.149") >= 0:
               Total += linenumber
          elif line.find("Whiteland") >= 0:
               Total += linenumber
          elif line.find("80.222.19.190") >= 0:
               Total += linenumber
          elif line.find("Kayley") >= 0:
               Total += linenumber
          elif line.find("dcassyqw@microsoft.com") >= 0:
               Total += linenumber
a.close()

print (f"The total is: {Total}")

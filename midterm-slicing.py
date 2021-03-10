#!/usr/bin/env python3

"""
I know there are a lot of random comments in the script.
I wanted you to be able to see how I tested the output as I built this, so I left the commands in and commented them out.
"""

print ("Name: Jon Becker")

#Rips text to a list
midterm = open("slicing-file.txt","r")

slicethis = []
word = []
quote = []
for line in midterm:
     words = line.strip()
     wordlist = words.split()
     slicethis.append(wordlist)

midterm.close()

#print (slicethis)

#Slices list
a = slicethis[-3]
#print (slicethis[-3])
quote.append(slicethis[-3])

b = slicethis[2:5]
#print (slicethis[2:5])
quote.append(slicethis[2:5])

c = slicethis[-10:-16:-2]
#print (slicethis[-10:-16:-2])
quote.append(slicethis[-10:-16:-2])

d = slicethis[10:13]
#print (slicethis[10:13])
quote.append(slicethis[10:13])

e = slicethis[-19:-22:-1]
#print (slicethis[-19:-22:-1])
quote.append(slicethis[-19:-22:-1])

print (quote)

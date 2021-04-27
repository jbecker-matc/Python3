#!/usr/bin/env python3
import requests, bs4

res = requests.get('http://notpurple.com')
res.raise_for_status()
notpurple = bs4.BeautifulSoup(res.text, 'html.parser')
notelems = notpurple.select('title')
aelems = notpurple.select('a')

print ("notelems:", len(notelems))
print (notelems[0].getText())
print (str(notelems[0]), '\n')

print ("aelems:", len(aelems))
print (aelems[0].getText())
print (str(aelems[0]))
print (aelems[1].getText())
print (str(aelems[1]))


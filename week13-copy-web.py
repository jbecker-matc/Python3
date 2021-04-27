#!/usr/bin/env python3
import requests, webbrowser

response = requests.get("https://notpurple.com")

with open("my_web_file.html", "w") as hFile:
     hFile.write(response.text)

"""
I wanted the script to automatically open the copied page but ran into 
a permission error even after using chmod on both the script and the html file.
"""
#webbrowser.open('/home/kali/weeklyassignments-jbecker-matc/my_web_file.html')

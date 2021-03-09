#!/usr/bin/env python3

#Defines the FQDN dictionary
FQDN = {
     "domain1": "server1.testlab.com",
     "domain2": "server2.testlab.com",
     "domain3": "server3.testlab.com",
     "domain4": "server4.testlab.com",
     "domain5": "server5.testlab.com",
     "domain6": "server6.testlab.com"
}

#Defines FQDN to IP address mappings
IP = {
     "server1.testlab.com": "192.168.1.10",
     "server2.testlab.com": "192.168.1.11",
     "server3.testlab.com": "192.168.1.12",
     "server4.testlab.com": "192.168.1.13",
     "server5.testlab.com": "192.168.1.14",
     "server6.testlab.com": "192.168.1.15"
}

#lists all FQDNs
print ("Here are the FQDNs: ", FQDN.values()),

#Lists all IP Addresses
print ('-' * 10),
print ("Here are the IP addresses: ", IP.values())

#Lists all tuples
print ('-' * 10),
print ("Here are the full records: ", IP.items())

#Adds more tuples
IP["server7.testlab.com"] = "192.168.1.16"
IP["server8.testlab.com"] = "192.168.1.17"

#Tests for servers
print ('-' *10)

if FQDN.get("domain2", "server2.testlab.com"):
     print ("Server2 is contained in the dictionary")

search = FQDN.get("domain10", "server10.testlab.com")
if search == True:
     print ("Server10 is contained in the dictionary")
elif search != True:
     print ("Server10 is not contained in the dictionary")

#!/usr/bin/python

from pythonping import ping
import ipaddress

#Ask for user network/input
#input(str("Enter ip and prefix:"))

usr_network = input('Enter your ipaddress and prefix:')
network = ipaddress.ip_network(usr_network)

for addr in network.hosts():
    ping(str(addr), verbose=True)

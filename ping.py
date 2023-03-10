#!/usr/bin/python

from pythonping import ping
import ipaddress

#Ask for user network/input
#input(str("Enter ip and prefix:"))

network = ipaddress.ip_network('127.0.0.0/24')

for addr in network.hosts():
    ping(str(addr), verbose=True)

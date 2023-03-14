#!/usr/bin/python

from pythonping import ping
import ipaddress


usr_network = input('Enter your ipaddress and prefix:')
network = ipaddress.ip_network(usr_network)

for addr in network.hosts():
    ping(str(addr), verbose=True)

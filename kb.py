# -*- coding: utf-8 -*-

#---------------#
#delosemre.xyz  #
#kernelblog.org #________
#delosemre@delosemre.xyz#
#delosemre@outlook.com  #
#twitter.com/delosemre  #
#-----------------------#

import os
import sys, traceback
import argparse
import time
import httplib
import subprocess
import re, urllib2
import socket
import urllib,sys,json
import telnetlib
import glob
import random
import Queue 
import threading
import requests
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep




print("")
print("""
    
 _  __                    _ ____  _             
| |/ /___ _ __ _ __   ___| | __ )| | ___   __ _ 
| ' // _ \ '__| '_ \ / _ \ |  _ \| |/ _ \ / _` |
| . \  __/ |  | | | |  __/ | |_) | | (_) | (_| |
|_|\_\___|_|  |_| |_|\___|_|____/|_|\___/ \__, |
                                          |___/ .org
Deneyimsizler İçin Bir Penetrasyon Aracı

	
	KernelBlog.org
	Forum.kernelblog.org
	---
	KernelBlog devepoler team
	Kernelblog geliştirici ekibi
      """)
print("")

#giriş kısmı

kullanici = raw_input("    [ > ] Kullanıcı Adı Giriniz : ")
time.sleep(0.5)

#kullanıcı sorgusu

print("")
print("    [ + ] Hoşgeldin " + " " + kullanici) 
print("")
time.sleep(1)

#menü

print("")

menu = """
\033[1;91m
     )                          (                
  ( /(                   (   (  )\ )             
  )\()) (  (           ( )\( )\(()/(      (  (   
|((_)\ ))\ )(   (     ))((_)((_)/(_)) (   )\))(  
|_ ((_)((_|()\  )\ ) /((_)((_)_(_))   )\ ((_))\  
| |/ (_))  ((_)_(_/((_))| || _ ) |   ((_) (()(_) 
  ' </ -_)| '_| ' \)) -_) || _ \ |__/ _ \/ _` |  
 _|\_\___||_| |_||_|\___|_||___/____\___/\__, |  
                                         |___/   
                                     \033[1;m
          Seçenekler     	  
    \033[1;93m                       		         
    1-) SQL İnjection				      
    2-) Admin Panel Bulucu                     
    3-) Basit Bilgi Toplayıcı
    4-) Site Tarama
    5-) Terminali Temizle
    6-) Sistemi GÜncelle
    7-) Çık   \033[1;m                 
     """
    
print(menu)

#komut girdisi

time.sleep(0.5)
print("")
secim = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")
print("")

#seçenekler

if secim =="1":
		print ("------------")
		print ("Başlatılıyor")
		print ("------------")
		time.sleep(0.5)
		cmd1=os.system ("python diger/sqli.py")


if secim == "2":
		print """
		-------------------------------
		Başlatılıyor Admin Panel Bulucu 
		-------------------------------
		"""
		time.sleep(0.5)
		cmd1 = os.system ("perl diger/finder.pl")




if secim == "3":
		print """
		----------------------------------
		Basit Bilgi Toplayıcı Başlatılıyor 
		----------------------------------
		"""
		time.sleep(0.5)
		cmd1 = os.system ("python diger/dog.py")




if secim == "4":
		print ("--------------------------------------------")
		print ("Site Tarama İşlemi Uniscan İle Yapılacaktır.")
		print ("Uniscan Başlatılıyor")
		print ("--------------------------------------------")
		time.sleep(0.5)
		url = raw_input('Tarama Yapılacak Site: ')
		cmd1 = os.system ('uniscan -u' +url+' -qweds')




if secim == "5":
        cmd1 = os.system ("clear")
        print ("--------------")
        print ("Terminal Temiz")
        print ("--------------")



if secim == "6":
		print ("----------------------------------")
		print ("     SİSTEMİ GÜNCELLEME")
		print ("----------------------------------")
		cmd1 = os.system ("sudo apt-get update")
		cmd1 = os.system ("sudo apt-get upgrade")
		cmd1 = os.system ("sudo apt-get dist-upgrade")



if secim == "7":
		print ("    Güle Güle")
		sys.exit()
		 
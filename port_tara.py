#!/bin/avr/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAYICI TASSAKLI")

print("""

1)Normal Port Tarama
2)Servis ve Versiyon Tarama
3)Isletim Sistemi Tarama

""")

islemno = raw_input("Islem Numarasi Giriniz: ")

if(islemno=="1"):
        hedefip = raw_input("Hedef IP Giriniz: ")
        os.system("nmap " + hedefip)
elif(islemno=="2"):
        hedefip = raw_input("Hedef IP Giriniz: ")
        os.system("nmap -sS -sV "+ hedefip)
elif(islemno=="3"):
          hedefip = raw_input("Hedef IP Giriniz: ")
          os.system("nmap -0 "+ hedefip)
elif:
          print("Oyle Bir Secenek Bulunmamaktadir.")

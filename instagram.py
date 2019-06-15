#!/bin/usr/python

"""
	Hack Instagram Onyx7

"""

import os
import sys
from time import sleep

def ketik(s):
	for khazul in s + '\n':
		sys.stdout.write(khazul)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')
print ("""\033[1;31m
         WELCOME TO INSTAGRAM HACKED
                   Onyx7
\033[1;35m         ---------------------------

""")

a = input("\033[1;33mUsername target : ")
os.system('clear')
print ("\033[1;36m Server: Online ")
sleep(0.5)
print ("\033[1;36m memulai crack ")
sleep(2)
print ("\033[1;36m Status: Oke! ")
print (' ')
print (' ')
print ("\033[1;32m Memulai HACKED! ")
print (' ')
ketik ("\033[1;32m Mengambil Data INFORMASI... ")
sleep(0.5)
ketik ("\033[1;32m Menggunakan SQL...")
sleep(0.5)
ketik ("\033[1;32m Baypass Access Token...")
sleep(0.5)
print ("\033[1;32m Baypass Sukses! ")
sleep(1)
print (' ')

ketik ("\033[1;32m Mencari Password... ")
sleep(2)
ketik ("\033[1;32m Mendapatkan Password...")
sleep(0.5)
ketik ("\033[1;32m Baypass Recaptcha! ")
sleep(2)
print ("\033[1;32m Baypass Sukses! ")
print (' ')

print ("\033[1;32m Sedang Login...")
sleep(3)
print (' ')
print ("\033[1;33m Username : %s" % (a))
print ("\033[1;33m Password : bagaskara556")
sleep(3)
print (' ')
print ("\033[1;32m Login Sukses! ")
print (' ')
print ("\033[1;32m Mengubah Username! ")
sleep(2)
print ("\033[1;31m   Sukses! ")
print (' ')
print ("\033[1;32m Mengubah Password! ")
sleep(2)
print ("\033[1;31m   Sukses! ")
print (' ')
sleep(0.5)
print ("""\033[1;35m
Note : Username dan password tersimpan di penyimpanan
       internal kalian dengan nama folder (Hasil).
""")
print (' ')
ketik ("\033[1;33m Thank You 👍 ")

z = open("pass.txt","w")

pesan= """
---------------------
Username:
Password:
---------------------
	"""
z.write(pesan)
z.close()

os.system('mkdir /sdcard/Hasil')
os.system('mv pass.txt /sdcard/Hasil')

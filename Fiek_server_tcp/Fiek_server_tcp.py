#Albion Burrniku
#180714100040
#Rrjetat Kompjuterike   #Prof:Blerim Rexha   #Ass:Haxhi Lajqi

import socket
import threading
import _thread
from socket import gethostname
import time
import random
import math
import sys
import string

# IPADRESA
def IPADDRESS(IP):
    return IP[0]

# PORTI
def PORT(porti):
    return porti[1]

# BASHKETINGELLORE
def BASHKETINGELLORE(text):
    i = 0
    n = 0
    while i < len(text):
        if text[i] in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
            n += 1
        i += 1
    return n
#ZANORE
def ZANORE(text):
    i = 0
    n = 0
    while i < len(text):
        if text[i] in 'aeiouyAEIOUY':
            n += 1
        i += 1
    return n

#REVERSE 
def REVERSE(text):
    return text[::-1]

#PALINDROME
def PALINDROME(text):
    rev = REVERSE(text)
    if(text==rev):
      return "Eshte Palindrom"
    return "Nuk eshte Palindrom"

# KOHA
def TIME():
    t = str(time.ctime(time.time()))
    return t

# LOJA
def GAME():
    array = []
    for i in range(5):
        array.append(random.randint(1, 35))
    return array

#GCF
def GCF(n1,n2):
  if n1>n2:
     n1, n2 = n2, n1
  for i in range(n1,0,-1):
      if n1%i==0 and n2%i==0:
          return i

# KONVERTIMI
def CONVERT(option, nr):
    option=str(option).upper()
    if (option == "CMTOINCH"):
        return int(nr)/2.54

    elif (option == "INCHTOCM"):
        return int(nr)*2.54

    elif (option == "KMTOMILES"):
        return int(nr)/1.609

    elif (option == "MILETOKM"):
        return int(nr)*1.609

    else:
        return("Duhet te zgjidhni njeren nga opcionet : CMTOINCH, INCHTOCM , KMTOMILES, MILETOKM")

# ~~~* Metodat shtese *~~~
def MESATARJA(nr1, nr2):
    rez = (nr1+nr2) / 2
    return rez
 

try:
        serverPort=13000
        serverName='localhost'
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error as e:
        print("Error ne krijimin e socket "+str(e))

try:
        s.bind((serverName,serverPort))
except socket.error as m:
        print("Error: " + m)

print('---------------------------------------')
print('Serveri eshte startuar ne localhost ne portin: ' + str(serverPort))
print('Serveri eshte duke pritur per ndonje kerkese')     
print('---------------------------------------\n')


while True:
       message,address=s.recvfrom(128)
       
       option=message.decode()
       print("Kerkesa "+str(option)+" u pranua nga IP: "+str(address[0])+" ne Portin : "+str(address[1]))

       if(option == 'IPADDRESS'):
                data = "Pergjigjia: Ip e klientit eshte : "+str(IPADDRESS(address))
                s.sendto(data.encode(),address)
                
       elif(option == 'PORT'):
                data = "Pergjigjia: Numri i portit te klientit eshte : " + str(PORT(address))
                s.sendto(data.encode(),address)

       elif(option == 'COUNT'):
                data1 , address= s.recvfrom(128)
                data2 = str(BASHKETINGELLORE(data1.decode()))
                data3 = str(ZANORE(data1.decode()))
                data="Pergjigjia: Teksti i pranuar përmban " + data3 +" zanore dhe "+ data2 +" bashkëtingëllore"
                s.sendto(data.encode(),address)

       elif(option== 'REVERSE'):
                data1 , address= s.recvfrom(128)
                data = REVERSE(data1.decode())
                s.sendto(data.encode(),address)

       elif(option == 'PALINDROME'):
                data , address= s.recvfrom(128)
                data1 = str(PALINDROME(data.decode()))
                s.sendto(data1.encode(),address)

       elif(option == 'TIME'):
                data = str(TIME())
                s.sendto(data.encode(),address)

       elif(option == 'GAME'):
                data = str(GAME())
                s.sendto(data.encode(),address)

       elif(option == 'GCF'):
                n1 , address= s.recvfrom(128)
                n2 , address= s.recvfrom(128)
                data ="Pergjigjia: GCF eshte: " + str(GCF(int(n1.decode()),int(n2.decode())))
                s.sendto(data.encode(),address)

       elif(option == 'CONVERT'):
                m , address= s.recvfrom(128)
                nr , address= s.recvfrom(128)
                data = str(CONVERT(m.decode(),nr.decode()))
                s.sendto(data.encode(),address)

       elif(option == 'MESATARJA'):
                nr1 , address=s.recvfrom(128)
                nr2 , address=s.recvfrom(128)
                data = str(CONVERT(nr1.decode(),nr2.decode()))
                s.sendto(data.encode(),address)

      



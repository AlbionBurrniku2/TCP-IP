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

print("Deshironi ta ndryshoni serverin dhe portin ?")
p=input().upper()
if(p=='PO'):
    print("Sheno emrin e serverit: ")
    serverName=input().lower()
    print("Sheno numrin e portit: ")
    serverPort1=input()
    serverPort=int(serverPort1)
else:
  serverName='localhost'
  serverPort=13000
s=(serverName,serverPort)
try:
    clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error as e:
   print("Error gjate krijimit te Client Socket: "+str(e))

while True:
    option=input("\nOperacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF,\
    CONVERT,MESATARJA, SHKEPUT(per shkeputjen e lidhjes)?").upper()
    clientSocket.sendto(option.encode(),s)
    
    if(option == 'IPADDRESS'):
        r, address = clientSocket.recvfrom(128)
        print(r.decode())

    elif(option == 'PORT'):
        r, address = clientSocket.recvfrom(128)
        print(r.decode())
    
    elif(option == 'COUNT'):
        text = input("Teksti? :")
        clientSocket.sendto(text.encode(),s)
        n,address = clientSocket.recvfrom(128)
        print(str(n.decode()))
    

    elif(option == 'REVERSE'):
        text = input("Sheno fjalen : ")
        clientSocket.sendto(text.encode(),s)
        n,address = clientSocket.recvfrom(128)
        print("Pergjigjia: "+ n.decode())
         
    elif(option == 'PALINDROME'):
        text = input("Sheno fjalen : ")
        clientSocket.sendto(text.encode(),s)
        n,address = clientSocket.recvfrom(128)
        print("Pergjigjia: "+ n.decode())

    elif(option == 'TIME'):
        r,address = clientSocket.recvfrom(128)
        print(r.decode())

    elif(option == 'GAME'):
        r,address = clientSocket.recvfrom(128)
        print(r.decode())

    elif(option == 'GCF'):
        n1 = input("Sheno numrin e pare: ")
        n2 = input("Sheno numrin e dyte: ")
        clientSocket.sendto(n1.encode(),s)
        clientSocket.sendto(n2.encode(),s)
        r,address = clientSocket.recvfrom(128)
        print(r.decode())

    elif(option == 'CONVERT'):
       
        data = "Ne cka deshironi ta konvertoni  numrin tuaj ?  (CMTOINCH , INCHTOCM , KMTOMILES , MILETOKM)"  
        print(data)    
        option = input()
        nr = input("Sheno nje numer :")
        clientSocket.sendto(option.encode(),s)
        clientSocket.sendto(nr.encode(),s)
        r,address = clientSocket.recvfrom(128)
        print(r.decode())

    elif(option == 'MESATARJA'):
                nr1=input("Jepni vleren per nr 1")
                nr2=input("jepni vleren per nr 2")
                clientSocket.sendto(nr1.encode(),s)
                clientSocket.sendto(nr2.encode(),s)
                data = str((nr1+nr2)/2)
                data,address = clientSocket.recvfrom(128)
                print(data.decode())

    


    

    elif(option =='SHKEPUT'):
            break
    else:
        print("\n Gabim ! Sheno njeren nga opcionet")
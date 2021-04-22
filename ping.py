#!/usr/bin/python3

import os
from multiprocessing import Process

def obtienePing (cPing):
    resp = os.popen(cPing).read()+"--"
    if resp != "--":
        ipValidadas.append(resp)

def f(start, stop, composicionIp):
    for i in range(start, stop):
        comandoPing = ""
        comandoPing= "ping -c 1 "+composicionIp[0]+"."+composicionIp[1]+"."+composicionIp[2]+"."+str(i+1)+" | grep ttl"
        obtienePing(comandoPing)
        print ("TIPO 255.255.255.X ANALIZANDO IP: "+composicionIp[0]+"."+composicionIp[1]+"."+composicionIp[2]+"."+str(i+1))

def hacerPin():
    tem = dirIP[0]
    composicionIp = tem.split(".")
    comandoPing = ""
    if typOcteto == 8:
        for i in range(254):
            for j in range(254):
                for k in range(254):
                    comandoPing = ""
                    comandoPing= "ping -c 1 "+composicionIp[0]+"."+str(i+1)+"."+str(j+1)+"."+str(k+1)+" | grep ttl"
                    obtienePing(comandoPing)
                    os.system("clear")
                    print ("RED DE TIPO 255.X.X.X ANALIZANDO IP: "+composicionIp[0]+"."+str(i+1)+"."+str(j+1)+"."+str(k+1))
    elif typOcteto == 16:
        for i in range(254):
            for j in range(254):
                comandoPing = ""
                comandoPing= "ping -c 1 "+composicionIp[0]+"."+composicionIp[1]+"."+str(i+1)+"."+str(j+1)+" | grep ttl"
                obtienePing(comandoPing)
                os.system("clear")
                print ("RED 255.255.X.X ANALIZANDO IP: "+composicionIp[0]+"."+composicionIp[1]+"."+str(i+1)+"."+str(j+1))
    else:
        p1 = Process(target=f, args=(0,51, composicionIp))
        p2 = Process(target=f, args=(52,101, composicionIp))
        p3 = Process(target=f, args=(102,153, composicionIp))
        p4 = Process(target=f, args=(154,203, composicionIp))
        p5 = Process(target=f, args=(204,254, composicionIp))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()

ipValidadas = []

comandoIP = "ip addr | grep inet | grep brd"
obtieneIP = os.popen(comandoIP).read()
listaIP = obtieneIP.split("\n")
dirIni = 0
dirFin = 0
listaIP.pop(len(listaIP)-1)
dirIP = []
typOcteto = 0
for i in listaIP:
    dirIni = i.find("inet")+5
    dirFin = i.find("brd")-4
    temp = i[dirIni:dirFin]
    dirIP.append(temp)
    dirIni = dirFin+1
    dirFin = dirIni+2
    typOcteto = int(i[dirIni:dirFin])
hacerPin()
print("Se encontraron:", len(ipValidadas))
for j in ipValidadas:
    print(j)
print("El programa ha concludio sus procesos.")
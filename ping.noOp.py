#!/usr/bin/python3

import os

def obtienePing (cPing):
    resp = os.popen(cPing).read()+"--"
    if resp != "--":
        ipValidadas.append(resp)


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
                    print ("SE ANALIZARA UNA RED DE TIPO 255.X.X.X \n ANALIZANDO IP: "+composicionIp[0]+"."+str(i+1)+"."+str(j+1)+"."+str(k+1))
    elif typOcteto == 16:
        for i in range(254):
            for j in range(254):
                comandoPing = ""
                comandoPing= "ping -c 1 "+composicionIp[0]+"."+composicionIp[1]+"."+str(i+1)+"."+str(j+1)+" | grep ttl"
                obtienePing(comandoPing)
                os.system("clear")
                print ("SE ANALIZARA UNA RED DE TIPO 255.255.X.X \n ANALIZANDO IP: "+composicionIp[0]+"."+composicionIp[1]+"."+str(i+1)+"."+str(j+1))
    else:
        for i in range(254):
            comandoPing = ""
            comandoPing= "ping -c 1 "+composicionIp[0]+"."+composicionIp[1]+"."+composicionIp[2]+"."+str(i+1)+" | grep ttl"
            obtienePing(comandoPing)
            os.system("clear")
            print ("SE ANALIZARA UNA RED DE TIPO 255.255.255.X \n ANALIZANDO IP: "+composicionIp[0]+"."+composicionIp[1]+"."+composicionIp[2]+"."+str(i+1))


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
for j in ipValidadas:
    print(j)
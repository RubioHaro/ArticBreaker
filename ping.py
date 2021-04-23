#!/usr/bin/python3

import os
import threading

def getPing (ping_command, parsed_ip):
    response = os.popen(ping_command).read() + "--"
    if response != "--":
        answered_ips.append(parsed_ip)

def pingTypeC(start, stop, ip):
    for i in range(start, stop):
        ping_command= "ping -c 1 "+ ip[0]+"."+ip[1]+"."+ip[2]+"."+str(i+1)+" | grep ttl"
        parsed_ip =  ip[0]+"."+ip[1]+"."+ip[2]+"."+str(i+1)
        getPing(ping_command, parsed_ip)
        print ("ping to:" + parsed_ip)

def Ping():
    tem = ip_dir[0]
    ip = tem.split(".")
    if type != 8 and type != 8:

        ## Timing 2.39m 5 processes Original time: 13.13m lineal
        x1 = threading.Thread(target=pingTypeC,args=(0,51, ip,)) #Generar hilo
        x2 = threading.Thread(target=pingTypeC,args=(52,101, ip,)) #Generar hilo
        x3 = threading.Thread(target=pingTypeC,args=(102,153, ip,)) #Generar hilo
        x4 = threading.Thread(target=pingTypeC,args=(154,203, ip,)) #Generar hilo
        x5 = threading.Thread(target=pingTypeC,args=(204,254, ip,)) #Generar hilo
        
        x1.start()
        x2.start()
        x3.start()
        x4.start()
        x5.start()

        x1.join()
        x2.join()
        x3.join()
        x4.join()
        x5.join()
    else:
        print("The program only works for 255.255.255.x address type")

answered_ips = []

ip_list = os.popen("ip addr | grep inet | grep brd").read().split("\n")
init_dir = 0
end_dir = 0
ip_list.pop(len(ip_list)-1)
ip_dir = []
type = 0
for i in ip_list:
    init_dir = i.find("inet")+5
    end_dir = i.find("brd")-4
    temporal_var = i[init_dir:end_dir]
    ip_dir.append(temporal_var)
    init_dir = end_dir + 1
    end_dir = init_dir + 2
    type = int(i[init_dir:end_dir])
Ping()
print(len(answered_ips), " ips founded!")

for j in answered_ips:
    print(j)

import paramiko
import getpass

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for j in answered_ips:
    starParamiko(j,ssh_client)

print("The program has exited.")

## PARAMIKO MODULE
def starParamiko(host, ssh_client):
    print("ArticBraker: Initializing paramiko ssh connection")
    print('hostname:', host)
    host = input()
    print('Enter your username:')
    user = input()

    try:
        p = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        print('requesting access.')

    ssh_client.connect(hostname=host, username=user,password=p)
    print("connected")


    try:
        ftp_client=ssh_client.open_sftp()
        ArchivoEnviado = "/home/jazmin/Desktop/backupenviado.py"
        ftp_client.put('/home/jazmin/ArticBreaker/backup.py',ArchivoEnviado) ## de donde va a donde llega 
        ftp_client.close()
        try:
            stdin,stdout,stderr=ssh_client.exec_command("python3 "+ArchivoEnviado)
            print(stdout.readlines())
            print(stderr.readlines())
        except:
            print("Python3 error")
    except:
        print("FTP Error")
    


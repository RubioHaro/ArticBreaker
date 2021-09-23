## working with py3
import os, sys, subprocess

def generarRespaldo(type, base_route, backup_route):
    print("Buscando Archivos "+ type +"\n")
    comandoPDF = "find "+ base_route +" -name *." + type
    salida = os.popen(comandoPDF).read()
    print("Salida:\n", salida)
    print("Busqueda de PDF finalizada\n")

    print("Generando Respaldo\n")
    lines = salida.splitlines()

    destino = backup_route + type +"/"
    dir_command = "mkdir " + destino
    salida = os.popen(dir_command)

    while lines:
        origen =lines.pop() 
        print ("copiando: " + origen)
        copy_command = "cp " + origen + " " +  destino 
        print(copy_command)
        salida_copia = os.popen(copy_command).read()
        print("Salida:\n", salida_copia)
        pass

    print ("Respaldo de " + type + " generado")


backup_route = "/home/eagle/Escritorio/"
generarRespaldo("mp4",base_route="/home/eagle",backup_route="/home/eagle/Escritorio/")
generarRespaldo("jpeg",base_route="/home/eagle",backup_route="/home/eagle/Escritorio/")

print("comprimiendo archivo")
comando = "tar czf back.tar.gz "+ backup_route+ "/mp4 "+ backup_route+ "/pdf "+ backup_route+ "/jpeg"
salida_compresion = os.popen(comando).read()
print("Salida:\n", salida_compresion)
print("Backup completo!")
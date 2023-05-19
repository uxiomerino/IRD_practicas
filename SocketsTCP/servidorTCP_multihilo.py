# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:51:49 2021

@author: uxiom
"""


import sys
import socket
import threading

def multihilo(dirCliente,conexion):
    try:
        timeout=300
        conexion.settimeout(timeout)
        mensaje=conexion.recv(4096)
        print('Recibido {} de {}'.format(mensaje.decode('UTF-8'), dirCliente))
        print("Volvendo a enviar {} a mensaxe ao cliente".format(mensaje.decode('UTF-8'), dirCliente))
        conexion.send(mensaje)
    except socket.timeout:
        print("{} segundos sen recibir nada".format(timeout))
    except:
        print("{} error en hilo".format(sys.exc_info()[0]))
    finally:
        conexion.close()

def main():
    try:
        #Creamos o socket TCP
        socketServidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        #Lemos os argumentos
        puerto=int(sys.argv[1])
    
        #Asociamos o socket a un porto e direccion
        print("Iniciando en {}".format(puerto))
        socketServidor.bind(("", puerto))
    
        #Establecemos un timeout
        timeout=300
        socketServidor.settimeout(timeout)
    
        #Poñemos o servidor en modo escoita
        socketServidor.listen()
        
        while True:
            print("Esperando por unha conexión")
            conexion, dirCliente = socketServidor.accept()
            threading.Thread(target=multihilo, args=(dirCliente, conexion)).start()
    except socket.timeout:
        print("{} segundos sen recibir nada".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
    finally:
        socketServidor.close()

if __name__=="__main__":
    main()
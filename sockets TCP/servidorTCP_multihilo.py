1# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:51:49 2021

@author: Lucan
"""

import sys
import socket
import threading

def multihilo(dirCliente,conexion):
    mensaje=conexion.recv(4096)
    print('Recibido {} de {}'.format(mensaje.decode('UTF-8'), dirCliente))
    if mensaje:
        print("Volviendo a enviar el mensaje al cliente")
        conexion.send(mensaje)
    conexion.close()

def main():
    try:
        while True:
            #Se crea el socket TCP
            socketServidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
            #Se leen los argumentos
            puerto=int(sys.argv[1])
        
            #Se asocia el socket a un puerto y direccion
            print("Iniciando en {}".format(puerto))
            socketServidor.bind(("", puerto))
        
            #Se establece un timeout
            timeout=300
            socketServidor.settimeout(timeout)
        
            #Se pone el servidor en modo escucha
            socketServidor.listen(1)
            
            print("Esperando por una conexión")
            conexion, dirCliente = socketServidor.accept()
            threading.Thread(target=multihilo, args=(dirCliente, conexion)).start()
    except socket.timeout:
        print("{} segundos sin recibir nada".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
    finally:
        socketServidor.close()

if __name__=="__main__":
    main()
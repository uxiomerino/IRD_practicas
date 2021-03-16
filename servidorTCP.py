# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:51:49 2021

@author: Lucan
"""

import sys
import socket

def main():
    while True:
        #Se crea el socket TCP
        socketServidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        #Se leen los argumentos
        puerto=int(sys.argv[1])
        maquina=sys.argv[2]
        
        #Se asocia el socket a un puerto y direccion
        dirDestino= (maquina, puerto)
        print("Iniciando en {}:{}".format(maquina, puerto))
        socketServidor.bind(dirDestino)
        
        #Se establece un timeout
        timeout=300 
        socketServidor.settimeout(timeout)
        
        #Se pone el servidor en modo escucha
        socketServidor.listen(1)

        print("Esperando por una conexión")
        conexion, dirCliente = socketServidor.accept()
        try:
            print("Conexión de", dirCliente)
            mensaje=conexion.recv(4096)
            print('Recibido {}'.format(mensaje.decode('UTF-8')))
            if mensaje:
                print("Volviendo a enviar el mensaje al cliente")
                conexion.send(mensaje)
            conexion.close()
        except socket.timeout:
            print("{} segundos sin recibir nada".format(timeout))
        except:
            print("Error: {}".format(sys.exc_info()[0]))
        finally:
            socketServidor.close()

if __name__=="__main__":
    main()
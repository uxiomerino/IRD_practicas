# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:51:49 2021

@author: uxiom
"""

import sys
import socket

def main():
    if len(sys.argv) != 3: 
        print("Formato ServidorTCP <puerto>") 
        sys.exit()
    try:
        
        #Creamos o socket TCP
        socketServidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        #Lemos os argumentos
        puerto=int(sys.argv[1])
        maquina=sys.argv[2]
        
        #Asociamos o socket a un porto e direccion
        dirDestino= (maquina, puerto)
        print("Iniciando en {}: {}".format(maquina, puerto))
        socketServidor.bind(dirDestino)

        #Establecemos un timeout
        timeout=300 
        socketServidor.settimeout(timeout)
    
        #Poñemos o servidor en modo escoita
        socketServidor.listen()

        while True:
            try:
                print("Esperando por unha conexión")
                conexion, dirCliente = socketServidor.accept()
                conexion.settimeout(timeout)
                print("Conexión de", dirCliente)
                mensaje=conexion.recv(4096)
                print('Recibido {}'.format(mensaje.decode('UTF-8')))
                print("Volvendo a enviar a mensaxe ao cliente")
                
                conexion.send(mensaje)
            except socket.timeout:
                print("{} segundos sin recibir nada".format(timeout))
            except:
                print("{} error en hilo".format(sys.exc_info()[0]))
            finally:
                conexion.close()
    except socket.timeout:
        print("{} segundos sin recibir nada".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
    finally:
        socketServidor.close()

if __name__=="__main__":
    main()
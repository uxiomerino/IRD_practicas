# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:01:19 2021

@author: uxiom
"""
 
import sys
import socket


def main():
    if len(sys.argv) != 4:
        print("Formato ClienteTCP <maquina> <puerto> <mensaje>")
        sys.exit()
        
    try:
        #Creamos o Socket TCP
        socketCliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Asignamos o timeout de 300 segundos ao socket
        timeout=300 
        socketCliente.settimeout(timeout)
        
        #Lemos os argumentos
        maquina = sys.argv[1]
        puerto= int(sys.argv[2])
        mensaje = sys.argv[3]
        dirDestino = (maquina, puerto)
        
        #Conectamos o socket ao servidor
        socketCliente.connect(dirDestino)


        #Enviamos a mensaxe
        print("Enviando mensaje: {} a {}: {}".format(mensaje, maquina, puerto))
        socketCliente.send(mensaje.encode('UTF-8'))
        
        #Enviamos a respuesta
        print("Esperando para recibir respuesta.")
        mensajeEco, a = socketCliente.recvfrom(len(mensaje))
        print("CLIENTE: Recibido {} de {}:{}".format(mensaje, maquina, puerto))
    
    #Introducimos as excepcions
    except socket.timeout:
        print("{} segundos sin recibir nada".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
    finally:
        socketCliente.close()
if __name__=="__main__":
    main()
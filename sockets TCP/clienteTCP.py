# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:01:19 2021

@author: Lucan
"""

#Se importan las librerías a ejecutar
import sys
import socket

#Se define el programa a ejecutar
def main():
    if len(sys.argv) != 4:
        print("Formato ClienteTCP <maquina> <puerto> <mensaje>")
        sys.exit()
        
    try:
        #Se crea un Socket TCP
        socketCliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Se asigna un timeout de 300 segundos al socket
        timeout=300 
        socketCliente.settimeout(timeout)
        
        #Se leen los argumentos
        maquina = sys.argv[1]
        puerto= int(sys.argv[2])
        mensaje = sys.argv[3]
        dirDestino = (maquina, puerto)
        
        #Se conecta el socket al servidor
        socketCliente.connect(dirDestino)


        #Se envía el mensaje
        print("Enviando mensaje: {} a {}:{}".format(mensaje, maquina, puerto))
        socketCliente.send(mensaje.encode('UTF-8'))
        
        #Se recibe la respuesta
        print("Esperando para recibir respuesta.")
        mensajeEco, a = socketCliente.recvfrom(len(mensaje))
        print("CLIENTE: Recibido {} de {}:{}".format(mensaje, maquina, puerto))
    
    #Se introducen las excepciones
    except socket.timeout:
        print("{} segundos sin recibir nada".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
    finally:
        socketCliente.close()
if __name__=="__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:54:43 2021

@author: uxiom
"""

import sys
import socket
import threading
import os
import datetime

def contenttype(file):
    if file.endswith('.txt'):
        return 'text/plain'
    elif file.endswith('.html'):
        return 'text/html'
    elif file.endswith('.gif'):
        return 'image/gif'
    elif file.endswith('.jpeg') or file.endswith('.jpg'):
        return 'image/jpeg'
    else:
        return 'application/octet-stream'
    
def hilo(scliente):
    try:
        mensaje=scliente.recv(4096).decode('UTF-8').split('\n')
        peticion= mensaje[0].split(' ')
        print(peticion)
        fecha=str(datetime.date.today())
        
        if len(peticion) !=3 or peticion[0] not in ['GET', 'HEAD']:
            linea_error=("HTTP/1.1 400 Bad Request" + "\n")
            linea_fecha=('Date: {}'.format(fecha) + '\n')
            linea_servidor=('Server: uxiom, ' + 'localhost'+'\n')
            scliente.send((linea_error + linea_fecha + linea_servidor).encode('UTF-8'))
        elif os.path.exists('data'+ peticion[1]) ==False:
            linea_error=("HTTP/1.1 404 Not Found" + "\n")
            linea_fecha=('Date: {}'.format(fecha)+ '\n')
            linea_servidor=('Server: uxiom, '+ 'localhost'+ '\n')
            scliente.send((linea_error + linea_fecha + linea_servidor).encode('UTF-8'))
        else:
            ficheiro = 'data'+ peticion[1]
            URL='data'+peticion[1]
            if peticion[0]== 'GET':
                if URL.endswith('.txt') or URL.endswith('html'):
                    with open(ficheiro, 'r') as f:
                        content = f.read()
                        linea_error=("HTTP/1.1 200 OK"+ "\n")
                        linea_fecha=('Date: {}'.format(fecha)+'\n')
                        linea_servidor=('Server: uxiom, '+'localhost'+'\n')
                        linea_longitud=('Content-Length: '+str(os.path.getsize(ficheiro))+ '\n')
                        linea_tipo=('Content-Type: '+ str(contenttype(ficheiro))+ '\n')
                        linea_modificacion=('Last-Modified: '+ (datetime.datetime.fromtimestamp(os.path.getmtime(ficheiro)).strftime('%a, %d %b %Y %H:%M:%S %Z'))+'\n')
                        scliente.send((linea_error + linea_fecha + linea_servidor + linea_longitud + linea_tipo + linea_modificacion + content).encode('UTF-8'))
                        
                elif URL.endswith('.gif') or URL.endswith('.jpeg') or URL.endswith('.jpg'):
                    with open(ficheiro, 'rb') as f:
                        content = f.read()
                        linea_error=("HTTP/1.1 200 OK"+ "\n")
                        linea_fecha=('Date: {}'.format(fecha)+'\n')
                        linea_servidor=('Server: uxiom, '+'localhost'+'\n')
                        linea_longitud=('Content-Length: '+str(os.path.getsize(ficheiro))+ '\n')
                        linea_tipo=('Content-Type: '+ str(contenttype(ficheiro))+ '\n')
                        linea_modificacion=('Last-Modified: '+ (datetime.datetime.fromtimestamp(os.path.getmtime(ficheiro)).strftime('%a, %d %b %Y %H:%M:%S %Z'))+'\n')
                        scliente.send((linea_error + linea_fecha + linea_servidor + linea_longitud + linea_tipo + linea_modificacion + content).encode('UTF-8'))
                        
                else:
                    with open(ficheiro, 'r') as f:
                        content = f.read()
                        linea_error=("HTTP/1.1 200 OK"+ "\n")
                        linea_fecha=('Date: {}'.format(fecha)+'\n')
                        linea_servidor=('Server: uxiom, '+'localhost'+'\n')
                        linea_longitud=('Content-Length: '+str(os.path.getsize(ficheiro))+ '\n')
                        linea_tipo=('Content-Type: '+ str(contenttype(ficheiro))+ '\n')
                        linea_modificacion=('Last-Modified: '+ (datetime.datetime.fromtimestamp(os.path.getmtime(ficheiro)).strftime('%a, %d %b %Y %H:%M:%S %Z'))+'\n')
                        scliente.send((linea_fecha + linea_servidor + linea_longitud + linea_tipo + linea_modificacion + content).encode('UTF-8'))
            elif peticion[0]== 'HEAD':
                if URL.endswith('.txt') or URL.endswith('.html'):
                    with open(ficheiro, 'r') as f:
                        content = f.read
                        linea_error=("HTTP/1.1 200 OK"+ "\n")
                        linea_fecha=('Date: {}'.format(fecha)+'\n')
                        linea_servidor=('Server: uxiom, '+'localhost'+'\n')
                        linea_longitud=('Content-Length: '+str(os.path.getsize(ficheiro))+ '\n')
                        linea_tipo=('Content-Type: '+ str(contenttype(ficheiro))+ '\n')
                        linea_modificacion=('Last-Modified: '+ str(datetime.datetime.fromtimestamp(os.path.getmtime(ficheiro)).strftime('%a, %d %b %Y %H:%M:%S %Z'))+'\n')
                        scliente.send((linea_fecha + linea_servidor + linea_longitud + linea_tipo + linea_modificacion).encode('UTF-8'))
                elif URL.endswith('.jpg') or URL.endswith('.jpeg') or URL.endswith('.gif'):
                   with open(ficheiro, 'rb') as f:
                        content = f.read()
                        linea_error=("HTTP/1.1 200 OK"+ "\n")
                        linea_fecha=('Date: {}'.format(fecha)+'\n')
                        linea_servidor=('Server: uxiom, '+'localhost'+'\n')
                        linea_longitud=('Content-Length: '+str(os.path.getsize(ficheiro))+ '\n')
                        linea_tipo=('Content-Type: '+ str(contenttype(ficheiro))+ '\n')
                        linea_modificacion=('Last-Modified: '+ (datetime.datetime.fromtimestamp(os.path.getmtime(ficheiro)).strftime('%a, %d %b %Y %H:%M:%S %Z'))+ '\n')
                        scliente.send((linea_fecha + linea_servidor + linea_longitud + linea_tipo + linea_modificacion).encode('UTF-8'))
                else:
                    with open(ficheiro, 'r') as f:
                        content = f.read
                        linea_error=("HTTP/1.1 200 OK"+ "\n")
                        linea_fecha=('Date: {}'.format(fecha)+'\n')
                        linea_servidor=('Server: uxiom, '+'localhost'+'\n')
                        linea_longitud=('Content-Length: '+str(os.path.getsize(ficheiro))+ '\n')
                        linea_tipo=('Content-Type: '+ str(contenttype(ficheiro))+ '\n')
                        linea_modificacion=('Last-Modified: '+ str(datetime.datetime.fromtimestamp(os.path.getmtime(ficheiro)).strftime('%a, %d %b %Y %H:%M:%S %Z'))+'\n')
                        scliente.send((linea_fecha + linea_servidor + linea_longitud + linea_tipo + linea_modificacion).encode('UTF-8'))
    except:
        linea_error = ("HTTP/1.1 400 Bad Request" + "\n")
        linea_fecha = ('Date: {}'.format(fecha)+'\n')
        linea_servidor=('Server: uxiom, '+'localhost'+'\n')
        scliente.send=((linea_error + linea_fecha + linea_servidor).encode('UTF-8'))
    finally:
        scliente.close()
    
def main():
    if len(sys.argv)!=2:
        print('Formato ServidorTCPMultihilo {puerto}')
        sys.exit()
    try:
        puerto = int(sys.argv[1])
        socketServer=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketServer.bind(('localhost', puerto))
        socketServer.settimeout(300)
        socketServer.listen(5)
        while True :
            socketCliente, address = socketServer.accept()
            threading.Thread(target=hilo, args=(socketCliente,)).start()
    except socket.timeout:
        print('300 segundos sin recibir nada.')
    except: 
        print('Error: ', sys.exc_info()[0])
        raise
    finally:
        socketServer.close()
        
if __name__ == "__main__":
    main()

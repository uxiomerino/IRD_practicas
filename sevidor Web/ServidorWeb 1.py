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
    mensaje=scliente.recv(4096).decode('UTF-8').split('\n')
    peticion= mensaje[0].split()
    print(peticion)
    fecha=str(datetime.date.today())
    
    if len(peticion) !=3 or peticion[0] not in ['GET', 'HEAD']:
        print('400 Bad Request')
        scliente.send(str("HTTP/1.1 400 Bad Request" + "\r\n").encode('UTF-8'))
        scliente.send(str('Date: {}'.format(fecha) + '\r\n').encode())
        scliente.send(str('Server: uxiom, ' + 'localhost'+'\r\n\r\n').encode())
    
    elif not os.path.exists('data'+ peticion[1]):
        print('404 Not Found')
        scliente.send(str("HTTP/1.1 404 Not Found" + "\r\n").encode('UTF-8'))
        scliente.send(str('Date: {}'.format(fecha)+ '\r\n').encode())
        scliente.send(str('Server: uxiom, '+ 'localhost'+ '\r\n\r\n').encode())
        
    else:
        ficheiro = 'data'+ peticion[1]
        print('200 OK')
        scliente.send(str("HTTP/1.1 200 OK"+ "\r\n").encode('UTF-8'))
        scliente.send(str('Date: {}'.format(fecha)+'\r\n').encode())
        scliente.send(str('Server: uxiom, '+'localhost'+'\r\n').encode())
        scliente.send(str('Content-Length: '+str(os.path.getsize(ficheiro))+ '\r\n').encode())
        scliente.send(str('Content-Type: '+ str(contenttype(ficheiro))+ '\r\n').encode())
        scliente.send(str('Last-Modified: '+ str(datetime.datetime.fromtimestamp(os.path.getmtime(ficheiro)).strftime('%a, %d %b %Y %H:%M:%S %Z'))+'\r\n\r\n').encode())
        if peticion[0]== 'GET':
            with open(ficheiro, 'rb') as f:
                fContent = f.read()
                scliente.send(fContent)
        
            
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

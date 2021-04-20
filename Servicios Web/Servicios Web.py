# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:22:07 2021

@author: uxiom
"""
import requests
from bs4 import BeautifulSoup
#import gmg
#from gmg import plotMap


url= requests.get("https://irdgcdinfo.data.blog/ayuntamientos/")
direccion= url.content
parser= BeautifulSoup(direccion,"html.parser")


lista1=[]
lista2=[]
for elemento in parser.find_all("tr"):
    for elemento in parser.find_all("th"):
        element=elemento.text
        if element.isdecimal()==True:
            lista1.append(element)
           
        else:
            if element == "Nome do concello" or element == "Identificador":
                pass
            else:
                lista2.append(element)
lista8=[]
c=0
while c<313:
    for x in range(len(lista1)):
        x=0
        identificador = lista1[c]
        concello = lista2[c]
    
    print(identificador, concello)
        
    vtiempo=requests.get("http://servizos.meteogalicia.gal/rss/predicion/jsonPredConcellos.action?idConc="+identificador )
    tiempo= vtiempo.json()
    predicion_tiempo= tiempo['predConcello']['listaPredDiaConcello'][0]['ceo']['manha']
    

    codpred=requests.get("https://irdgcdinfo.data.blog/codigos/")
    codigo=codpred.content
    codigoparse=BeautifulSoup(codigo, "html.parser")
    lista3=[]
    for elemento in codigoparse.find_all("tr"):
        for elemento in codigoparse.find_all("th"):
            elemento=elemento.text
            if elemento.isdecimal()==True:
                pass
            elif elemento == "Valor numérico" or elemento== "Descrición do estado do ceo" or elemento=="Non dispoñible":
                pass
            else:
                lista3.append(elemento)
    for i in range(len(lista3)):
        i=predicion_tiempo-100
        prediccionceo=lista3[i]
    print(prediccionceo)


    coordenadasconcello= {
            'key': 'b8fb3471f4b042',
            'q': concello ,
            'format': 'xml'
                }
    bcoordenadas=requests.get("https://us1.locationiq.com/v1/search.php", params= coordenadasconcello)
    bcoordenadas1= bcoordenadas.text
    parseo= BeautifulSoup(bcoordenadas1, 'lxml')
    lista4=[]
    lista5=[]
    lista6=[]
    for elemento in parseo.find_all("place"):
        important= elemento['importance']
        lat= elemento['lat']
        lon=elemento['lon']
        lista4.append(important)
        lista5.append(lat)
        lista6.append(lon)
     
    for i in range(len(lista4)):
        coordenadas=lista4[0]
        
    for i in range(len(lista5)):
        latitud=lista5[0]
    
    for i in range(len(lista6)):
        longitud=lista6[0]
    
    print('Coordenadas', latitud,  longitud) 
    coords1=float(longitud)
    coords2=float(latitud)
    coords3=(coords1,coords2)
    lista7=(predicion_tiempo, coords3)
    lista8.append(lista7)
    c+=1
    
plotMap(points= lista8)

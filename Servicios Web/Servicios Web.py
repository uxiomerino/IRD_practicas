# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:22:07 2021

@author: uxiom
"""
import requests
from bs4 import BeautifulSoup
import gmg
#from gmg import plotMap



url = requests.get("https://irdgcdinfo.data.blog/ayuntamientos/")
contenido = url.content
parser = BeautifulSoup(contenido,"html.parser")


listacódigos=[]
listaconcellos=[]

for elemento in parser.find_all("tr"):
    
    for elemento in parser.find_all("th"):
        
        elemento=elemento.text
        if elemento.isdecimal()==True:
            listacódigos.append(elemento)           
        else:
            if elemento == "Nome do concello" or elemento == "Identificador":
                pass
            else:
                listaconcellos.append(elemento)
                
                
puntos=[]
t=0


for x in range(len(listacódigos)):
    x=0
    identificador = listacódigos[t]
    concello = listaconcellos[t]

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
    predicionceo=lista3[i]
    
print(predicionceo)


coordenadasconcello= {
        'key': 'b8fb3471f4b042',
        'q': concello ,
        'format': 'xml'
            }

bcoordenadas = requests.get("https://us1.locationiq.com/v1/search.php", params = coordenadasconcello)
   
bcoordenadas1= bcoordenadas.text

parseo= BeautifulSoup(bcoordenadas1, 'lxml')

listacoords=[]
listalat=[]
listalon=[]
   
for elemento in parseo.find_all("place"):
    important= elemento['importance']
    lat= elemento['lat']
    lon=elemento['lon']
    listacoords.append(important)
    listalat.append(lat)
    listalon.append(lon)
 
for i in range(len(listacoords)):
    coordenadas=listacoords[0]
    
for i in range(len(listalat)):
    latitud=listalat[0]

for i in range(len(listalon)):
    longitud=listalon[0]

print('Coordenadas', latitud,  longitud) 

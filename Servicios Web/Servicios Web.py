# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:22:07 2021

@author: uxiom
"""
import requests
from bs4 import BeautifulSoup
import gmg
from gmg import plotMap



url = requests.get("https://irdgcdinfo.data.blog/ayuntamientos/")
direccion = url.content
parser = BeautifulSoup(direccion,"html.parser")


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
while t<313:
    
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

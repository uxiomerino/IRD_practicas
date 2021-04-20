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

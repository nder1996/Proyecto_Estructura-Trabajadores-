# -*- coding: utf-8 -*-

import string
import re
import os


def Salida_Archivo(Linea): # Validacion Texto a Diccionario
  Data="";D_V="";Lista=[]
  for i in range(len(Linea)):
    if Linea[i].isdigit()==True:
      Data = Data + Linea[i]    
    if Linea[i]=="-":
      Lista.append(Data)
      Data=""
    if re.search('[A-Za-z]',Linea[i])!=None:
      Data = Data + Linea[i]
    if Linea[i]==" ":
       Data = Data+" "
  return Lista


Lista = []
Lista = Salida_Archivo("1081827159-11081827158-Arevalo Madrid-Andersons-")

print(Lista[2])




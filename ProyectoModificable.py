import string
import re
import os


Votantes=[];Lider_V=[]


def BaseD(DatosV):
    Votantes = open("/C:\Users\a\Desktop\PEstructura/filename.txt", "w")

def ValidadorC(Variable,Tipo):
    Busq = re.search(r'[\d]',Variable)
    if Tipo==1:
       if Busq==None:
        os.system ("cls")
        print("------------------------------------------------") 
        print("Ingrese Solo Numeros Para Llenar Este Campo")
        print("----------------------------------------------\n") 
        IngresarD()
    if Tipo==0:
        if Busq!=None:
          os.system ("cls")
          print("----------------------------------------------") 
          print("Ingrese Solo Letras Para Llenar Este Campo")
          print("--------------------------------------------\n") 
          IngresarD()

def GuardarD(Nombre,Apellido,Cedula,Cedula_l):
  DatosV.append(Nombre);DatosV.append(Apellido);DatosV.append(Cedula);DatosV.append(Cedula_l)  

def MostrarD(Datosv):
    print("\nNombre               : ",Votantes[0]);print("\nApellido             : ",Votantes[1]);print("\n# De Cedula          : ",Votantes[2]);print("\n# Cedula De Su Lider : ",Votantes[3])
    print("\n")


def IngresarD():    
   Nombre  = input("\nIngrese Su Nombre    : ")
   ValidadorC(Nombre,0);
   Apellido= input("\nIngrese Su Apellido  : ")
   ValidadorC(Apellido,0);
   Cedula = input("\nIngrese Su # Cedula  : ")
   ValidadorC(Cedula,1);
   Cedula_l= input("\nIngrese El # Cedula De Su Lider : ")
   ValidadorC(Cedula_l,1);
   GuardarD(Nombre,Apellido,Cedula,Cedula_l)
   


BaseD()
import string
import pdb
import re
import os


Votantes=[];L_V=[];

def BaseD(DatosV,DatosL):
   try:
       Votantes = open("DVotantes.txt", "a+")
       Lugar    = open("DLugar.txt", "a+")
       Votantes.write("%s\n"%(DatosV))
       Lugar.write("%s\n"%(DatosL))
       Votantes.close()
       Lugar.close()
   except:
     print("Error Al Llenar Los Datos Al Archivo")

def InvBase():
   linea="";i=0
   DatosV = open("DVotantes.txt","r")
   DatosL = open("DLugar.txt","r")
   try:
      for linea in DatosV.readlines():
         TData(linea,"",0,2,0)
      DatosV.close()
      linea=""
      for linea in DatosL.readlines():
         TData(linea,"",0,2,0)
      DatosL.close()
   except:
      """
          print("--------------------------") 
          print("No Hay Datos Disponibles")
          print("--------------------------\n") 
      """

def TData(L_Data,Data,i,a,j):
      for j in range(4):
         while L_Data[i]!="-":
           if i>=a:
              Data=Data+L_Data[i]
           i+=1
         if L_Data[i]=="-":
          Votantes.append(Data)
          Data=""
          a = a+1 ; i = i+5

def D_Comprobar(L_Data,Data,Bandera):
   i=1;Max=int(len(Votantes)/4)
   for i in range(Max):
      if Data == Votantes[i]:
            return True
            break
      i+=4
   return False
          
def ValidadorC(Variable,Tipo):
 if Tipo==1:
      if Variable.isdigit()==False:
         os.system ("cls")
         print("----------------------------------------------------------------") 
         print("Ingrese Solo Numeros [DEL 0 HASTA EL 9] Para Llenar Este Campo")
         print("----------------------------------------------------------------\n") 
         IngresarD()
 if Tipo==0:
      i=0;  
      for i in range(len(Variable)):
         if re.search( "[A-Za-z]",Variable[i])==None:
            os.system ("cls")
            print("----------------------------------------------------------------") 
            print("Ingrese Solo Letras [DE LA A HASTA EL Z] Para Llenar Este Campo")
            print("----------------------------------------------------------------\n") 
            IngresarD()

def GuardarD(Nombre,Apellido,Cedula,Cedula_l,Ciudad_V,Lugar_V,Mesa_V,Puesto_V,DatosV,DatosL):
  Nombre=Nombre+"-";Apellido=Apellido+"-";Cedula=Cedula+"-";Cedula_l=Cedula_l+"-";Ciudad_V=Ciudad_V+"-";Lugar_V=Lugar_V+"-";Mesa_V=Mesa_V+"-";Puesto_V=Puesto_V+"-"
  DatosV.append(Cedula);DatosV.append(Cedula_l);DatosV.append(Apellido);DatosV.append(Nombre);DatosV.append(Nombre);
  DatosL.append(Cedula);DatosL.append(Lugar_V);DatosL.append(Puesto_V);DatosL.append(Mesa_V);DatosL.append(Mesa_V);
  BaseD(DatosV,DatosL) 

def MostrarD():
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    print("Nombre               : ",Votantes[3]);print("\nApellido             : ",Votantes[4]);print("\n# De Cedula          : ",Votantes[0]);print("\n# Cedula De Su Lider : ",Votantes[1])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")

def BuscarV(Cedula):
   try:
      Votantes = open("DVotantes.txt","r");c=0
      for linea in Votantes.readline():
         print("#: ",c," ",linea)
         c+=1
      Votantes.close()
   except:
      print("Error Al Buscar Los Datos Al Archivo") 

def IngresarD():    
   DatosV=[];DatosL=[];Bandera=True
   Cedula = input("\nIngrese Su # Cedula  : ")
   Cedula = Cedula.replace(" ", "");ValidadorC(Cedula,1)
   if D_Comprobar(Votantes,Cedula,Bandera)==False:
      Nombre    = input("\nIngrese Su Nombre    : ")
      S_Espacio = Nombre.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio=""
      Apellido  = input("\nIngrese Su Apellido  : ")
      S_Espacio = Apellido.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio=""
      Cedula_l  = input("\nIngrese El # Cedula De Su Lider : ")
      Cedula_l  = Cedula_l.replace(" ", "");ValidadorC(Cedula_l,1);
      Ciudad_V  = input("\nIngrese Su Ciudad Que Le Corresponde : ")
      S_Espacio = Ciudad_V.replace(" ", "");ValidadorC(S_Espacio,0);
      Lugar_V   = input("\nIngrese Su Lugar De Votacion : ")
      S_Espacio = Lugar_V.replace(" ", "");ValidadorC(S_Espacio,0);
      Mesa_V    = input("\nIngrese El # De la Mesa Correspondiente : ");ValidadorC(Mesa_V,1);
      Puesto_V  = input("\nIngrese El # Del Puesto Correspondiente : ");ValidadorC(Puesto_V,1);
      GuardarD(Nombre,Apellido,Cedula,Cedula_l,Ciudad_V,Lugar_V,Mesa_V,Puesto_V,DatosV,DatosL)
   else:
      os.system ("cls")
      print("-----------------------------------------------------------") 
      print("Usuario Ya Registrado , Por Favor Ingrese Otro # De Cedula")
      print("----------------------------------------------------------\n") 
      IngresarD()
   


InvBase()

IngresarD()



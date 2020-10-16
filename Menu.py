import string
import re
import os
import sys


D1_Votantes = dict() ; Votantes_D = [] 

def Inv_BaseD():
    V1="" ; Lista = []  
    try:
        V1 = open("DVotantes.txt",'r');
        Data="";linea=""; 
        for linea in V1.read():   
           if linea!="-" or linea!="\n" or linea!=" ":
               if (re.search( "[A-Za-z]",linea)!=None) or (linea.isnumeric()==True):
                  Data = Data + linea
           if linea==" ":
              if Data!="":
                 Lista.append(Data)
                 Data = ""
           if linea=="*":
              Lista.append("*") 
        V1.close()
        return Lista;
    except FileNotFoundError:
        print("---------------------------") 
        print("No Hay Registros Existentes")
        print("---------------------------\n")
     
def BaseD_L():
    Datos_V = [];
    Datos_V = Inv_BaseD()
    if Datos_V!=None:
        i = None; j = 0 ;Votantes=[];Data = ""; 
        for i in Datos_V:
            if i != "*" and j!=2 and j!=3:
                Votantes.append(i)
            elif j==2 or j==3:
                if j==2:
                    Data = i +" "
                if j==3:
                    Data = Data + i
                    Votantes.append(Data)
                    Data=""
            if i=="*":
               j=-1
            j+=1
        return Votantes  
    
def BaseD_Dicc():
    Data = BaseD_L()
       Data = "" ; a = 0 ;i=0
       while i<int(len(Data)/4):
        a=i*4;
        #print("Cedula : ",Data[a]," Inf -> ",Data[a+1:a+4])
        D1_Votantes[Data[a]] = Data[a+1:a+4]
        i+=1
   for i in D1_Votantes.keys():
      print ("Cedula : ",i, 'Datos - Inf -> : ', D1_Votantes[i])

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

def IngresarD():
   BaseD_Dicc()
  # Cedula = input("\nIngrese Su # Cedula  : ")
   ValidadorC(Cedula,1)
   if D1_Votantes.has_key(Cedula)==False:
       print("Hola_Mundo")
   #if D1_Votantes.has_key(Cedula)==False or D1_Votantes.has_key(Cedula)==None:
  #    Nombre    = input("\nIngrese Su Nombre    : ")
  #    S_Espacio = Nombre.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Nombre=Q_Espacio(Nombre)
  #    Apellido  = input("\nIngrese Su Apellido  : ")
  #    S_Espacio = Apellido.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Apellido=Q_Espacio(Apellido)
  #    Cedula_l  = input("\nIngrese El # Cedula De Su Lider : ")
  #    Cedula_l  = Cedula_l.replace(" ", "");ValidadorC(Cedula_l,1);
  #    Ciudad_V  = input("\nIngrese Su Ciudad Que Le Corresponde : ")
  #    S_Espacio = Ciudad_V.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Ciudad_V=Q_Espacio(Ciudad_V)
  #    Lugar_V   = input("\nIngrese Su Lugar De Votacion : ")
  #    S_Espacio = Lugar_V.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Lugar_V=Q_Espacio(Lugar_V)
  #    Mesa_V    = input("\nIngrese El # De la Mesa Correspondiente : ");ValidadorC(Mesa_V,1);
  #    Puesto_V  = input("\nIngrese El # Del Puesto Correspondiente : ");ValidadorC(Puesto_V,1);
  #    GuardarD(Nombre,Apellido,Cedula,Cedula_l,Ciudad_V,Lugar_V,Mesa_V,Puesto_V)
  ## else:
   #   os.system ("cls")
   #   sys.stdout.flush()
   #   print("-----------------------------------------------------------") 
   #   print("Usuario Ya Registrado , Por Favor Ingrese Otro # De Cedula")
   #   print("----------------------------------------------------------\n")     
    
def Menu():
    Opcion = ""
    print ("\n");
    print ("______ SISTEMA DE VOTACION _________");
    print ("\t  Selecciona una opción:\n")
    print ("1 -> Registrar Votante")
    print ("2 -> Registrar Lider De Votacion")
    print ("3 -> Modificar Datos Del Lider   De Votacion")
    print ("4 -> Modificar Datos Del Votante")
    print ("5 -> Eliminar Datos Del Votante")
    print ("6 -> Eliminar Datos Del Lider De Votacion")
    print ("7 -> Salir")
    print ("\n");
    Opcion = input("Ingrese El Numero Correspondiente Para Continuar : ")
        

 


IngresarD()
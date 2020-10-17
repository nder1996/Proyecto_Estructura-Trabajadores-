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
       Data = "" ; Data = BaseD_L()
       a = 0 ;i=0
       if Data!=None:
          while i<int(len(Data)/4):
            a=i*4;
            D1_Votantes[Data[a]] = Data[a+1:a+4]
            i+=1

def GuardarDicc(Nombre,Apellido,Cedula,Cedula_l,Ciudad_V,Lugar_V,Mesa_V,Puesto_V):
  Votantes_D = []; Votantes_L =[];
  Votantes_D.append(Cedula);Votantes_D.append(Cedula_l);Votantes_D.append(Apellido);Votantes_D.append(Nombre);
  D1_Votantes[Votantes_D[0]] = Votantes_D[1:4]
  Votantes_D.clear()
  #Votantes_D = Cedula + " - " + Cedula_l + " - " + Apellido + " - " + Nombre +   " * "
  #Votantes_L = Cedula + " - " + Lugar_V +  " - " + Puesto_V + " - " + Mesa_V   + " - " + Ciudad_V + " * "
  #BaseD(Votantes_D,Votantes_L)

def ValidadorC(Variable,Tipo):
 if Tipo==1:
      if Variable.isdigit()==False:
         os.system ("cls")
         print("\n")
         print("----------------------------------------------------------------") 
         print("Ingrese Solo Numeros [DEL 0 HASTA EL 9] Para Llenar Este Campo")
         print("----------------------------------------------------------------\n") 
         IngresarD()
 if Tipo==0:
      i=0;  
      for i in range(len(Variable)):
         if re.search( "[A-Za-z]",Variable[i])==None:
            os.system ("cls")
            print("\n")
            print("----------------------------------------------------------------") 
            print("Ingrese Solo Letras [DE LA A HASTA EL Z] Para Llenar Este Campo")
            print("----------------------------------------------------------------\n") 
            IngresarD()

def Q_Espacio(Letra):  
   L1 = Letra.find(" ")+1
   L2 = (Letra.count(" ")+L1)-1
   if Letra.count(" ")>1:
      N1 = Letra[0:L1]; N2 = Letra[L2:len(Letra)]
      Letra=""; 
      Letra = N1+N2
   return Letra

def IngresarD():
   BaseD_Dicc()
   print("\n")
   Cedula = input("\nIngrese Su # Cedula  : ")
   ValidadorC(Cedula,1)
   Encontrado = Cedula in D1_Votantes
   if Encontrado == False:
      Nombre    = input("\nIngrese Su Nombre    : ");Prueba = Nombre.replace(" ", "")
      Nombre=Q_Espacio(Nombre);ValidadorC(Prueba,0) ; Prueba = ""
      Apellido  = input("\nIngrese Su Apellido  : ");Prueba = Apellido.replace(" ", "")
      Apellido=Q_Espacio(Apellido);ValidadorC(Prueba,0); 
      Cedula_l  = str(input("\nIngrese El # Cedula De Su Lider : "))
      Cedula_l  = ValidadorC(Cedula_l,1);
      print("CEDULA DEL LIDER : ",Cedula_l,"\n");Prueba = ""
      Ciudad_V  = input("\nIngrese Su Ciudad Que Le Corresponde : ");Prueba = Ciudad_V.replace(" ", "")
      Ciudad_V=Q_Espacio(Ciudad_V);ValidadorC(Prueba,0)  
      Lugar_V   = input("\nIngrese Su Lugar De Votacion : ");Prueba = ""
      ValidadorC(Prueba,0);Lugar_V=Q_Espacio(Lugar_V);Prueba = Lugar_V.replace(" ", "")
      Mesa_V    = input("\nIngrese El # De la Mesa Correspondiente : ");ValidadorC(Mesa_V,1);
      Puesto_V  = input("\nIngrese El # Del Puesto Correspondiente : ");ValidadorC(Puesto_V,1);
      GuardarDicc(Nombre,Apellido,str(Cedula),str(Cedula_l),Ciudad_V,Lugar_V,str(Mesa_V),str(Puesto_V))
   else:
       print("-----------------------------------------------------------") 
       print("Usuario Ya Registrado , Por Favor Ingrese Otro # De Cedula")
       print("----------------------------------------------------------\n")
       IngresarD()



def BaseD(DatosV,DatosL):
   DatosV=DatosV+'\n';DatosL=DatosL+'\n'
   try:
       Votantes = open("DVotantes.txt","a+")
       Lugar    = open("DLugar.txt","a+")
       Votantes.write(DatosV)
       Lugar.write(DatosL)
       Votantes.close()
       Lugar.close()
   except:
     print("Error Al Llenar Los Datos Al Archivo")

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



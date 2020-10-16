import string
import sys
import re
import os


Votantes=[];L_V=[];

D1_Votantes = dict();



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

def Inv_BaseD(Lista):  
    V1= "";Data="";linea=""; V1 = open("DVotantes.txt",'r');
    try:
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
        return Lista
    except:
          print("--------------------------") 
          print("No Hay Datos Disponibles")
          print("--------------------------\n") 
          
def BaseD_L():
    i = None; j = 0
    Datos_V = []; Data = ""; Datos_V = Inv_BaseD(Datos_V) ; Votantes=[]
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
    Data = ""  ; Data = BaseD_L() ; a = 0 ;i=0
    while i<int(len(Data)/4):
       a=i*4;  
       print("Cedula : ",Data[a]," Inf -> ",Data[a+1:a+4])
       i+=1

      

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

def Q_Espacio(Letra):  
   L1 = Letra.find(" ")+1
   L2 = (Letra.count(" ")+L1)-1
   if Letra.count(" ")>1:
      N1 = Letra[0:L1]; N2 = Letra[L2:len(Letra)]
      Letra=""; 
      Letra = N1+N2
   return Letra

def GuardarD(Nombre,Apellido,Cedula,Cedula_l,Ciudad_V,Lugar_V,Mesa_V,Puesto_V):
  Votantes_D = ""; Votantes_L ="";
  Votantes_D = Cedula + " - " + Cedula_l + " - " + Apellido + " - " + Nombre +   " * "
  Votantes_L = Cedula + " - " + Lugar_V +  " - " + Puesto_V + " - " + Mesa_V   + " - " + Ciudad_V + " * "
  BaseD(Votantes_D,Votantes_L) 
  
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
   Bandera=True;
   Cedula = input("\nIngrese Su # Cedula  : ")
   Cedula = Cedula.replace(" ", "");ValidadorC(Cedula,1)
   if D_Comprobar(Votantes,Cedula,Bandera)==False:
      Nombre    = input("\nIngrese Su Nombre    : ")
      S_Espacio = Nombre.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Nombre=Q_Espacio(Nombre)
      Apellido  = input("\nIngrese Su Apellido  : ")
      S_Espacio = Apellido.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Apellido=Q_Espacio(Apellido)
      Cedula_l  = input("\nIngrese El # Cedula De Su Lider : ")
      Cedula_l  = Cedula_l.replace(" ", "");ValidadorC(Cedula_l,1);
      Ciudad_V  = input("\nIngrese Su Ciudad Que Le Corresponde : ")
      S_Espacio = Ciudad_V.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Ciudad_V=Q_Espacio(Ciudad_V)
      Lugar_V   = input("\nIngrese Su Lugar De Votacion : ")
      S_Espacio = Lugar_V.replace(" ", "");ValidadorC(S_Espacio,0);S_Espacio="";Lugar_V=Q_Espacio(Lugar_V)
      Mesa_V    = input("\nIngrese El # De la Mesa Correspondiente : ");ValidadorC(Mesa_V,1);
      Puesto_V  = input("\nIngrese El # Del Puesto Correspondiente : ");ValidadorC(Puesto_V,1);
      GuardarD(Nombre,Apellido,Cedula,Cedula_l,Ciudad_V,Lugar_V,Mesa_V,Puesto_V)
   else:
      os.system ("cls")
      sys.stdout.flush()
      print("-----------------------------------------------------------") 
      print("Usuario Ya Registrado , Por Favor Ingrese Otro # De Cedula")
      print("----------------------------------------------------------\n") 
      
   


print("VOTANTES : ",BaseD_L)

IngresarD()



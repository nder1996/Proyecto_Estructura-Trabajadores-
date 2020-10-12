import string
import re
import os


Votantes=[];Lugar_V=[];

def BaseD(DatosV):
   #Si Hay Algun Error
   #except NameError:
   try:
       Votantes = open("DVotantes.txt", "a+")
       Votantes.write("%s\n"%(DatosV))
       Votantes.close()
   except:
     print("Error Al Llenar Los Datos Al Archivo")

def InvBase():
    try:
      linea="";i=0
      DatosV = open("DVotantes.txt","r")
      print("\n")
      for linea in DatosV.readlines():
         TData(linea,"",0,2,0)
      DatosV.close()
    except:
      print("Error Al Almacenar Los Datos Al Archivo")
      
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
    Busq1 = re.search(r'[\d]',Variable)
    #Busq2 = re.search(r'[\d]',Variable)
    #[A-Z]'
    if Tipo==1:
       if Busq1==None:
        os.system ("cls")
        print("------------------------------------------------") 
        print("Ingrese Solo Numeros Para Llenar Este Campo")
        print("----------------------------------------------\n") 
        IngresarD()
    if Tipo==0:
        if Busq1!=None:
          os.system ("cls")
          print("----------------------------------------------") 
          print("Ingrese Solo Letras Para Llenar Este Campo")
          print("--------------------------------------------\n") 
          IngresarD()

def GuardarD(Nombre,Apellido,Cedula,Cedula_l,DatosV):
  Nombre=Nombre+"-";Apellido=Apellido+"-";Cedula=Cedula+"-";Cedula_l=Cedula_l+"-"
  DatosV.append(Cedula);DatosV.append(Cedula_l);DatosV.append(Apellido);DatosV.append(Nombre);
  print("DATOS DE VOTANTE : ",DatosV);
  BaseD(DatosV) 

def MostrarD():
    print("\nNombre               : ",Votantes[0]);print("\nApellido             : ",Votantes[1]);print("\n# De Cedula          : ",Votantes[2]);print("\n# Cedula De Su Lider : ",Votantes[3])
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
   DatosV=[];Bandera=True
   Cedula = input("\nIngrese Su # Cedula  : ")
   Cedula = Cedula.replace(" ", "");ValidadorC(Cedula,1)
   if D_Comprobar(Votantes,Cedula,Bandera)==False:
      Nombre  = input("\nIngrese Su Nombre    : ")
      ValidadorC(Nombre,0);
      Apellido= input("\nIngrese Su Apellido  : ")
      ValidadorC(Apellido,0);
      Cedula_l= input("\nIngrese El # Cedula De Su Lider : ")
      Cedula_l= Cedula_l.replace(" ", "");ValidadorC(Cedula_l,1);
      Lugar_v = input("\n Ingrese Su Lugar De Votacion : ")
      
      GuardarD(Nombre,Apellido,Cedula,Cedula_l)
   else:
      os.system ("cls")
      print("-----------------------------------------------------------") 
      print("Usuario Ya Registrado , Por Favor Ingrese Otro # De Cedula")
      print("----------------------------------------------------------\n") 
      IngresarD()
   
   
InvBase()
IngresarD()



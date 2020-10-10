import random
import string
import re
import os



def Validador(Num):
  if len(Num)==1:
   Busq = re.match(r'[\d]',Num)
   if Busq!=None:
    Jugar()
   else: 
     os.system ("cls")
     print("---------------------------") 
     print("Ingrese Solo Un Numero")
     print("---------------------------\n") 
     Jugar()
  else:
    os.system ("cls")
    print("---------------------------")  
    print("Ingrese Solo Un Numero")
    print("---------------------------\n") 
    Jugar()

def TirarDados(): 
   a=0;b=6;d=0
   for j in range (2):
       c=random.randint(0,6)
       print("Este es el numero que arrojo el dados  : ",c)
       d+=c
   print("Este es el acumulado de los numeros arrojado por los dado : " , d)

def Jugar():
    i=0
    while i>=0 or i==-1:
      TirarDados()   
      print("\n¿Desea tirar los dados?,ingrese cualquier numero para seguir jugando")
      Num=input("De lo contrario puede ingresar el numero -1 : ")
      Validador(Num)



Jugar()


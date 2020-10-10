import random
import re
import string
import os



def Validador(Num):
  if len(Num)==1:
   Busq = re.match(r'[\d]',Num)
   if Busq!=None:
    Jugar([1,2,3,4,5,6],[],0)
   else: 
     os.system ("cls")
     print("---------------------------") 
     print("Ingrese Solo Un Numero")
     print("---------------------------\n") 
     Jugar([1,2,3,4,5,6],[],0)
  else:
    os.system ("cls")
    print("---------------------------")  
    print("Ingrese Solo Un Numero")
    print("---------------------------\n") 
    Jugar([1,2,3,4,5,6],[],0)



def TirarDados(List,Relist):
   c=0;d=0;b=(len(List))-1
   for j in range (2):
     c=random.randint(0,b)
     print("Este es el numero que arrojo el dados  : ",List[c])
     d+=List[c];
     b=b-1
     Relist.append(List[c])
     List.pop(c)
   print("Este es el acumulado de los numeros arrojado por los dado : " , d)



def Jugar(List,Relist,i):
   while i>=0 or i==-1:   
      if len(List)==0:
        List=[1,2,3,4,5,6]
      TirarDados(List,[])
      print("\n¿Desea tirar los dados?,ingrese cualquier numero para seguir jugando")
      Num=input("De lo contrario puede ingresar el numero -1 : ")
      Validador(Num)
  

Jugar([1,2,3,4,5,6],[],0)
  




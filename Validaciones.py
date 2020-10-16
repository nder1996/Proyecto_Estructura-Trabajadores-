import string
import re
import os
import sys



D1_Votantes = dict();




def Inv_BaseD(Lista):  
    V1= "";Data="";linea=""; V1 = open("Prueba.txt",'r');
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
    #print("LEN : ",len(Data)/4)
    while i<int(len(Data)/4):
       a=i*4;  
       #D1_Votantes[Data[a]] = Data[a+1:a+4]
       #print("Cedula : ",Data[a]," Inf -> ",Data[a+1:a+4])
       #print("{i} : ",i," {a} : ",a," {a+1} :",a+1," {a+4} :",a+4)
       i+=1
       
       
BaseD_Dicc()

os.system("cls")

#for i in D1_Votantes.keys():
 #   print ("Cedula : ",i, 'Datos - Inf -> : ', D1_Votantes[i])
 
 
Lista = []

Lista.append("1");Lista.append("2");Lista.append("3");

print(type(Lista.index("0")))



       




  
    
    
    


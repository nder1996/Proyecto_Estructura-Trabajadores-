import re
import string

"""

#Solo Letras
Letras     = input("\nIngrese Su Nombre    : ")
Busq_Letra = re.search (r'[\d]',Letras)
#Solo Numeros
Numeros      = input("\nIngrese Su Cedula    : ")
Busq_Numero = re.search (r'[\d]',Numeros)


if Busq_Letra==None:
    print("Es Una Letra")
if Busq_Numero!=None:
   print("Es Una Numero") 

"""

"""
print("\n")
hola="['1081827159', '0000012345', 'ANDERSONS', 'AREVALO MADRID']"

print(hola.split(sep=' " ' , maxsplit=4))
print(" : ",hola[0])
print("\n")
"""





original = "EXAMPLE"
removed = original.replace("M", "")
print(removed)

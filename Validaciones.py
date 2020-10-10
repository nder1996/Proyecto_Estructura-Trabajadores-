import re
import string



#Solo Letras
Letras     = input("\nIngrese Su Nombre    : ")
Busq_Letra = re.search (r'[\d]',Letras)
#Solo Numeros
Numeros      = input("\nIngrese Su Cedula    : ")
Busq_Numero = re.search (r'[\d]',Numeros)


if Busq_Letra==None:
    print("Es Una Letra")
else:
   print("Es Una Numero") 



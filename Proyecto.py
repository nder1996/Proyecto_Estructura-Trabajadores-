class Nodo:
   def __init__(self,Cedula=None,Nombre=None,Apellido=None,Cedula_l=None,izq=None,der=None):
        self.Nombre   = Nombre
        self.Apellido = Apellido
        self.Cedula   = Cedula
        self.Cedula_l = Cedula_l
        self.izq      = izq
        self.der      = der

class Arbol:
    def _init_(self):
        self.Raiz = None
    def ObtenerRaiz(self):
        return self.Raiz


def Agregar(self,Cedula,Nombre,Apellido,Cedula_l):
    if self.Raiz == None:
      self.Raiz = Nodo(Cedula,Nombre,Apellido,Cedula_l)
    else:
      self.AgregarT(Cedula,Nombre,Apellido,Cedula_l)

def AgregarT(self,Tnodo,Cedula,Nombre,Apellido,Cedula_l):
    if Cedula<Tnodo.Cedula:
        if Tnodo.izq!=None:
            self.AgregarT(Cedula,Nombre,Apellido,Cedula_l,Tnodo.izq)
        else:
            Tnodo.izq=Nodo(Cedula,Nombre,Apellido,Cedula_l)
    else:
        if nodo.der!=None:
            self.AgregarT(Cedula,Nombre,Apellido,Cedula_l,Tnodo.der)
        else:
            Tnodo.der=Nodo(Cedula,Nombre,Apellido,Cedula_l)    

def Vtrabajador(self,Tnodo):
    if Tnodo!=None:
        print("Datos Del Trabajador \n")
        Print("Cedula           : ",str(Tnodo.Cedula))
        Print("Nombre           : ",str(Tnodo.Nombre))
        Print("Apellido         : ",str(Tnodo.Apellido))
        Print("Cedula Del Lider : ",str(Tnodo.Cedula_l))
        if Tnodo.izq!=None:
          self.Vtrabajador(Tnodo.izq)
        if Tnodo.der!=None:
          self.Vtrabajador(Tnodo.der)  

def Itrabjador(self):
   if self.Raiz!=None:
       self.Vtrabajador(self.Raiz)

def IngresarDatos():
  Nombre   = input("Ingrese Su Nombre   : ")
  Apellido = input("Ingrese Su Apellido : ")
  Cedula   = input("Ingrese Su Cedula   : ") 
  Cedula_l = input("Ingrese Su Cedula_l : ")
  AgregarT(Tnodo,Cedula,Nombre,Apellido,Cedula_l)
  



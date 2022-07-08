#Codigo hecho por Benjamin Parraguez
class Listas():
    def __init__(self, arreglo):
     self.arreglo = arreglo

    def funcionmenor(self=[]):
     menor=self.arreglo[0]
     for i in range(0,len(self.arreglo)):
          if (menor>=self.arreglo[i]):
             menor=self.arreglo[i]
     return menor

    def moda(self=[]):
     ca=1
     lista_modas = []
     for i in self.arreglo:
        c=0
        for j in self.arreglo:
            if i==j:
                c+=1
        if c>ca:
            ca=c
            moda=i
     if ca==1:
        return "Lista vacia o sin elementos repetidos"
     return moda
     
    def jugador_al_azar(self=[]):
     import random
     i=0
     can= int(input("ingrese cantidad de personas"))
     lista=[]
     elejido=random.randint(0,can-1)
     for i in range(can):
         a=input("ingrese nombre\t")
         lista.append(a)
     return lista[elejido]
    
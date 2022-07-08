#Hecho por Benjamin Parraguez
#Estructuras de las piramides sacadas de google

class Piramide():
    def __init__(self,altura,simbolo):
        self.altura = altura
        self.simbolo= simbolo

    def piramide_normal(self): 
       for i in range(self.altura):
            print (' '*(self.altura-i-1) + self.simbolo*(2*i+1))

class Invertir(Piramide):
    
    def piramide_invertida(self):
         for i in range(self.altura,0,-1):
             print(self.simbolo*i)


class Estirar(Piramide):
    def piramide_estirada(self):
        for i in range(self.altura):
             print(' '*(self.altura+i-1)+self.simbolo*(2*i+1))


p1 = Piramide(20,"$")
p2 = Invertir(20,"#")
p3 = Estirar(20,"%")
print(p1.piramide_normal())
print("-----------------------")
print(p2.piramide_invertida())
print("-----------------------")
print(p3.piramide_estirada())
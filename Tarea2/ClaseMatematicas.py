#Codigo hecho por Benjamin Parraguez

class Matematicas():
    import math
    def __init__(self, numero):
        self.numero = int(numero)

    def Base_Elevado(self, numero2):
        a = pow(self.numero, numero2)
        return str(a)

    def mcd(self, a):
        x = self.numero
        resto = 0
        while(x > 0):
            resto = x
            x = a % x
            a = resto
        return a

    def Fibo(self):  # Muestra los N primeros elementos de la serie de Fibonacci
        n1 = 0
        n2 = 1
        for i in range(0, self.numero, 1):
            n1 = n2 - n1
            n2 = n2 + n1
            print(n1)
        return True

    def esPrimo(self):
        x = self.numero
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
            if x % i != 0:
                return True
        return True

    def factorial_numero(self):
         fact = 1
         for num in range(2, self.numero + 1):
             fact *= num
         return fact
         
    def pitagoras(self,c1,a):  #función que calcula hip de tri. rec. ingresamos ambos catetos y el ángulo entre estos
         if (a== 90 and c1 != 0 and self.numero!= 0):
            hip = math.sqrt(pow(c1,2)+pow(self.numero,2))
            print (hip)
         else:
            print ("no es un triangulo rectángulo\n")

    def numeros_pares_hasta(self):
         lista=[]
         for i in range (2,(self.numero+1),2):
             lista.append(i)
         return lista

    def suma(self):
     x = self.numero
     s = x*(x+1)/2
     print("La suma es = ", s)
    
    def sumatoria(self, m):
     sumatorio = 0
     for i in range(self.numero, m+1):
         sumatorio += i
         print (sumatorio)
         return (sumatorio)

    def valorabsoluto(self):
     x = self.numero
     if x >= 0:
        return x
     else:
        return -x

    def promedio(self):
     x = self.numero
     x = int(input ("Ingrese la cantidad de numeros"))
     i = 0
     sumatotal = 0
     while x > i:
          N = int(input("Ingrese el numero"))
          sumatotal= (sumatotal + N)
          i= i + 1
          media= sumatotal/x
          print(media)

    def AreaPerimetroCuadrilatero(self, l2):
     x = self.numero
     Area = x * l2
     Perimetro = (2 * x) + (2 * l2)

     if (x == l2):
        print("El area del cuadrado es: ", Area)
        print("El perimetro del cuadrado es: ", Perimetro)

     else:
        print("El area del rectangulo es: ", Area)
        print("El perimetro del rectangulo es: ", Perimetro)

    def raiz(self):
     import math
     A=int(input("ingrese el numero al que quiere sacar raiz: "))
     if (A>=0):
         B=math.sqrt(A)
         print("el resultado es :", B)     
     else:
         print("error")

    def divisible_por(self):
     x = self.numero
     b = []
     cont = 1
     for i in range(x):
       if x%cont == 0:
         b.append(cont)
       cont = cont+1
     print("El número " + str(x) + " es divisible por: ")
     for j in range(len(b)):
       print(b[j])

    def valortotal(self, descuento):
     x = self.numero
     valortotal = x - (x * descuento / 100)
     return valortotal

    def temperatura (self):
     x = self.numero
     kelvin= x+273.15
     far=(x*9/5)+32
     print(f"{x} °C equivale a {kelvin:} K y a {far:} °F")
     return 
    
    def Num_Fel(self): 
     comp=[]
     l = len(self.numero)
     suma=0
     i=0
     t=0
     k=0
     while(t!=1):
       if (t==2):
         l = len(str(suma))
         str1=str(suma)
         suma=0
         i=0
         while (i < l):
            o=int(str1[i])
            v= o**2
            suma= v + suma
            i=i+1
         if (i==l):
            if (suma==1):
              print ("Es un numero Feliz sonrisa")
              return 1
            else:
               for j in comp:
                 if (j==suma):
                     print("No es un numero Feliz triste")
                     return 0
            t=2
            k=k+1
            comp.append(suma)
            break

    def  dado (self):
     import random
     x = self.numero
     resultado=[]
     for i in range(0,x):
         resultado.append(random.randint(1, 6))
         return resultado
    
    def fun_triangulo(self):
     x = self.numero
     print("¿Qué es una función triángulo?")
     print("Tomemos el número", x , "como ejemplo:")
     for i in range (x):
         if i == (x - 1):
             print(x)
             break
     print(x,"^",end=" ")
     print("La función triángulo es una iteración de exponenciales") 

    def velocidad(self):
     x = self.numero
     ms = (x*5/18)
     print("La velocidad ",x,"km/h es igual a ",ms,"m/s")
     return(ms)   

    def area_triangulo(self,h):
     print("Cual es la base y la altura del triangulo?",self.numero,h)
     area=(self.numero*h)/2
     return (area)

    def factorizacion(self):
     x = self.numero
     list=[]
     i=2
     while i <= x:
         if x%i == 0:
             list.append(i)
             x=(x/i)
             i=2
         else:
             i=i+1
     return list
    
    def area_perimtro(self):

     area= math.pi*self.numero**2
     perim= math.pi*2*self.numero
     print("El area es: ",area)
     print("El perimetro es: ",perim)

    def ramo(self,t,p):
     x = self.numero
     t = (t*x)/100
     p = (p*(100-x))/100
     n = p+t
     if(n >= 40):
         print("Pasaste el ramo!! con nota",n )
     else:
         print("No pasaste el ramo triste")

    def interesc(self):
     i=float(input("Ingrese la tasa de interes:"))
     C=int(input("Ingrese su capital inicial:"))
     n=int(input("Ingrese numero de periodos:"))
     print("Tu capital final será de:")
     CF=C*(1+i)**n
     CT=round(CF)
     return CT

    def demoratiempo(self):
     km = int(input("Ingrese la distancia de recorrido [Km]:"))
     kmh = int(input("Ingrese la velocidad a la que va [Km/h]:"))
     t = km/kmh
     print("su tiempo será: ", t, " horas")
     return t
    
    def calculanewton (self):
     print("ingresa la masa y aceleracion del objeto y te dire cuanto Newtons tiene")
     m= int(input("ingresa la masa del objeto"))
     a= int(input("ingresa la aceleracion del objeto"))
     z=m*a
     print("el objeto posee una cantidad de newtons igual a: ")
     return z


p1 = Matematicas(5)

print(p1.temperatura)
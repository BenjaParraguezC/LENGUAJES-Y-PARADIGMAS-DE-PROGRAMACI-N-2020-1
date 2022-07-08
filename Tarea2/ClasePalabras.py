#Codigo hecho por Benjamin Parraguez
class Palabras:
    def __init__(self, palabra):
        self.palabra = str(palabra)


    def is_palindromo(self):
        x = self.palabra
        x = x.replace(" ", "")
        for i in range(len(x)//2):
            if x[i] != x[-1-i]:
                return False
        return True

    def mirror_word(self):
     x = self.palabra
     h=""
     for i in range(len(x)):
         h+= x[-1-i]
     return h

    def check_vouls(self):
     x = self.palabra
     x = x.upper()
     vouls = ["A", "E", "I", "O","U"]
     count = 0
 
     for c in x:
         if c in vouls:
             count += 1
     print(count)

    def ordenarascii(self):
         x = self.palabra
         largo = len(x)
         numeros_ordenados = []
    # se crea una lista "numeros_ordenados" con los caracteres de "palabra"
         for i in range (largo):
             numeros_ordenados.append(ord(x[i]))
    # se ordenan los números por ascii
         for j in range (largo):
             for i in range (largo-1): 
                 letra1 = numeros_ordenados[i]
                 letra2 = numeros_ordenados[i+1]
                 if (letra1 < letra2):
                     numeros_ordenados[i] = letra1
                     numeros_ordenados[i+1] = letra2
                     if (letra1 > letra2):
                             numeros_ordenados[i] = letra2
                             numeros_ordenados[i+1] = letra1
         letras_ordenadas = []
         for i in range (largo):
              letras_ordenadas.append(chr(numeros_ordenados[i])) 
              x = ''.join(letras_ordenadas)
         return(x)

    def leetifier(self): #Convierte texto a l33t code
         x = self.palabra
         cambios = [('a','4'),('b','8'),('e','3'),('g','6'),('l','1'),('o','0'),('s','5'),('t','7'),('z','2')]
         nuevo = x.lower()
         for original,leet in cambios:
             nuevo = nuevo.replace(original,leet)
         return nuevo
    
    def anagram(self):
         x = self.palabra
         x=list(x)
         anagram=list(x)
         random=[13,2,19,5,3,7,18,0,14,1,16,12,8,9,10,11,6,4,15,17,20]
         lenght=len(x)
         j=-1
         num=1000
         for i in range(lenght):
             while num>lenght:
                 j=j+1
                 num=random[j]
                 anagram[i]=x[num]
                 num=1000
         return str(anagram)

    def ostia_tio(self):
         x = self.palabra
         x = x.replace("s","z")
         x = x.replace("S","Z")
         x = x.lower()
         x = x.capitalize()
         print(x)

    def repiteletra(self,letra):
         contador= 0
         x = self.palabra
         for i in x:
             if i == letra:
                 contador = contador+1
             return contador
         x = input("ingrese su texto")
         letra = input("escoja una letra")
         contador =repiteletra(x,letra)
         print("se repite: ",contador," veces.")
         
    def palabra_encryp(self):
         x = self.palabra
         vocal="aeiou"
         salida="4310*"
         cambio=x.maketrans(vocal,salida)
         print(x.translate(cambio))
         return x
from itertools import cycle

#Benjamin Parraguez

class Carnetidentidad():

        def __init__(self, rut, verificador):
            self.rut = rut
            self.verificador = verificador

        def Digitoverificador(self): ##Metodo sacado de internet
             value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(self.rut).zfill(8), '32765432')])%11
             a= {10: 'K', 11: '0'}.get(value, str(value)) 
             if (a==self.verificador):
                 print("RUT Valido")
             else:
                 raise Exception("Rut Invalido, Pruebe otra vez")


p1 = Carnetidentidad(20296814,"7") #Rut,digito verificador
print(p1.Digitoverificador())

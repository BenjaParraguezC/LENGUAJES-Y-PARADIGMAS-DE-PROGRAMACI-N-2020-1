#Codigo hecho por Benjamin Parraguez
class Otros():
    def __init__(self, diferente):
        self.diferente = diferente

    def amor(self):
        import random
        x = random.randint(1, 10)
        print("Ingresa un numero del 1 al 10 para saber si te ama")
        num = int(input())
        if (num == x):
             print("Que suerte! Te ama")
        else:
             print("Que pena. No te ama :c")

    def cronometro24h(self):
        import time
        for hora in range (0,24):
            for minuto in range (0,60):
                for seg in range (0,60):
                    if (hora<10 and minuto<10 and seg<10):
                        print ("0",hora,":0",minuto,":0",seg)
                        time.sleep(1)
                    continue
                if (hora<10 and minuto>9 and seg<10):
                    print ("0",hora,":",minuto,":0",seg)
                    time.sleep(1)
                    continue
                if (hora<10 and minuto<10 and seg>9):
                    print ("0",hora,":0",minuto,":",seg)
                    time.sleep(1)
                    continue
                if (hora<10 and minuto>9 and seg>9):
                    print ("0",hora,":",minuto,":",seg)
                    time.sleep(1)
                    continue
                if (hora>9 and minuto<10 and seg<10):
                    print (hora,":0",minuto,":0",seg)
                    time.sleep(1)
                    continue
                if (hora>9 and minuto>9 and seg<10):
                    print (hora,":",minuto,":0",seg)
                    time.sleep(1)
                    continue
                if (hora>9 and minuto<10 and seg>9):
                    print (hora,":0",minuto,":",seg)
                    time.sleep(1)
                    continue
                if (hora>9 and minuto>9 and seg>9):
                    print (hora,":",minuto,":",seg)
                    time.sleep(1)
                    continue

    def IMC (self,altura):
        coef=self.diferente/(altura**2)
        resultados=("Peso inferior al normal", "Normal", "Peso superior al normal", "Sobrepeso", "Jabba the Hutt")
        if coef >=100: 
            return resultados[4]
        elif coef>=30: 
            return resultados[3]
        elif coef>=25: 
            return resultados[2]
        elif coef>=18.5: 
            return resultados[1]
        elif coef>=0: 
            return resultados[0]
    
    def ip_clase(self):
        self.diferente = ["A", "B", "C", "D", "E"]
        ip = (ip.split('.'))
        ip = bin(int(ip[0]))[2:].zfill(8)
        c = 0
        for i in range(len(ip)):
            if ip[i] == "1":
                c += 1
            else:
                break
        return(self.diferente[c])
    
    def verificaRUT(self):
        x = self.diferente
        posiblesdig = ['0','1','2','3','4','5','6','7','8','9','k','K']
        rutwdig = ''
        dig = ''
        j = 2
        suma = 0
        for i in range(len(x)):
            if i == (len(x) - 1):
             dig = x[i].lower()
             break
        if x[i] in posiblesdig:
            rutwdig += x[i]
        for i in range((len(rutwdig) - 1), -1, -1):
            suma += int(rutwdig[i])*j
            if j == 7:
                j = 2
            else:
                j += 1
        realdig = 11 - int(suma%11)
        if realdig == 11:
            tocomp = '0'
        elif realdig == 10:
            tocomp = 'k'
        else: 
            tocomp = str(realdig)
        if tocomp == dig:
            return True
        else:
            return False

    def tasametabolica(self, peso, altura, edad, ejercicio):
        if (self.diferente == 1):
            tmb = (peso*10) + (6.25*altura) - (5*edad) + 5
            tmb = tmb*ejercicio

        if (self.diferente == 2):
            tmb = (peso*10) + (6.25*altura) - (5*edad) - 161
            tmb = tmb*ejercicio

        print("tu tasa metabólica basal es de", tmb, "calorías")
        return tmb

    def horoscopo_maldito(self):
        import random
        x = self.diferente.lower()
    
        if(x == "leo"):
            leidas_estelares_Le = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","Deje de ser tan orgulloso", "Ruge mucho muerde poco"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Le)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
 
        elif(x == "sagitario"):
            leidas_estelares_Sa = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","tienes el brazo derecho mas fuerte que el izquierdo", "igual y la cuarentena no te hizo nada", "dejese de aventuras que hay cuarentena"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Sa)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
        elif(x == "aries"):
            leidas_estelares_Ar = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","Cuidado con los Tauros, son peligrosos","UFFF hoy estamos mal", "mejor pregunta el horoscopo de tu signo lunar"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Ar)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
        elif(x == "cancer"):
            leidas_estelares_Ca = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","tu signo zodiacal representa lo que eres para la sociedad, un cancer", "te va a dar una enfermedad relacionada con tu signo, cancer", "Prepare to crab rave"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Ca)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
        elif(x == "escorpio"):
            leidas_estelares_Es = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra", "preguntale a Pedro Engel","bajale 3 cambios altoke","Dejate de dramas", "Ponte detrás Braum!"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Es)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
    
    
        elif(x == "piscis"):
            leidas_estelares_Pi = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","The cow level is a lie","acabas de conocer a alguien, ITS A TRAP", "alejate de las personas logicas, son demasiado racionales para ti"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Pi)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
 
        elif(x == "geminis"):
            leidas_estelares_Ge = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","vas a ser decepcionado","Ni Pedrito Engel Sabria decirte que wea", "te ocurrira algo bueno"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Ge)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
    
        elif(x == "libra"):
            leidas_estelares_Li = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","La balanza se inclinara a tu favor","la balanza se inclinara a tu contra", "la balanza es una construccion social, no te lo creas","eres 2.2 kg"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Li)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
 
        elif(x == "acuario"):
            leidas_estelares_Ac = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","igual tu amig@ del mismo sexo esta ric@", "En vola sale cachita","Pa que me preguntas a mi, buscalo en google"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Ac)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
        
        elif(x == "capricornio"):
            leidas_estelares_Cp = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","te ira mejor que al caballero del zodiaco","cuidado con esos cuernos papu","se dice que Virgo esta diciendo cosas a tu espalda *emoji de ojos*"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Cp)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
        
    
        elif(x == "virgo"):
            leidas_estelares_Vi = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","preguntale a Pedro Engel","ah! virgo! debes ver anime","Preguntale a la de Fairytail"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Vi)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
    
    
        elif(x == "tauro"):
            leidas_estelares_Ta = ["que nos vaiga bien",
            "te ganaste un completo",
            "ta caro el kilo de guagua",
            "uff de esto no hablamos", "nose mira afuera",
            "ni se te ocurra","TIME TO SMASH","The cow level is a lie"]
        
            Tuhoroscopo = random.choice(leidas_estelares_Ta)
        
            print("Segun las lecturas de las estrellas, Enhorabuena Tu horoscopo %s dice que:\n %s "% (x,Tuhoroscopo))
        
            return(Tuhoroscopo)
 
        else:
            Tuhoroscopo = "nada"
            print ("no escribiste nada relevante para las estrellas")
            return (Tuhoroscopo)
    
from Diarios import emol
from Diarios import latercera
from Twitter import twitter
from time import sleep

print("¿Que tema desea buscar dentro de twitter, emol y la tercera?")

busqueda = input()

twitt = twitter(busqueda)
x = twitt.texto
hora_twitter = twitt.fecha

sleep(5)

emol = emol(busqueda)
titular_emol = emol.titulo

sleep(5)

la_tercera = latercera(x)
titular_latercera = la_tercera.titulo
hora_latercera = la_tercera.fecha

sleep(5)


comparacion_noticia = lambda titular_emol , titular_latercera: print("Existe la misma noticia en el diario Emol y en el diario La Tercera") if titular_emol == titular_latercera else print("No existe la misma noticia en Emol y La Tercera")

comparacion_noticia(titular_latercera , titular_emol)

comparacion_hora_twitter_vs_diario = lambda hora_twitter , hora_latercera: print("La fecha de subida de la notica en twitter es : ", hora_twitter , "\ny la hora de subida en el diario es :", hora_latercera)

comparacion_hora_twitter_vs_diario(hora_twitter , hora_latercera)



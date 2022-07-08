Benjamin Parraguez - Seccion 1 - Lenguaje y paradigmas de la programacion - 2020/1


Tarea6_BenjaminParraguez incluye 2 funciones las cuales son:

Sort: sort de una lista a traves del paradigma funcional

Merge_sort: sort de una lista a traves del algoritmo de merge sort, a traves de un paradigma tradicional. (sacado de Geeks4Geeks)

Ambas funciones ocupan la misma lista.

He decidido ocupar ambos ordenamientos como medio de comparacion para ejemplificar debido a:

1.- Ahorrar recurso humano al momento de ejemplificar ambos casos.

2- Encuentro que a simple vista se pueden apreciar las diferencias entre las funciones.

Ahora bien, vamos al caso:

En nuestro primer ordenamiento via paradigma funcional, tenemos que el ordenamiento esta realizado simplemente en 7 lineas, utilizando la recursividad como base y en lo posible, no utilizar los ciclos en exceso.

Mientras que en nuestro ordenamiento Merge_sort, tenemos que subdide las listas hasta tener un punto que es incapaz de seguir, para despues al proceder al ordenamiento. Finalmente podemos notar que en su elaboracion ha tomado 19 lineas en ser creado.

Describiendo ambos puntos, quisiera hacer enfasis en porque la programacion funcional en nuestro caso es muchisimo mejor que la manera tradicional, los cuales son:

1.- Debuggeo de codigo y testeo: al tener menos lineas que proceden en su funcionamiento, es muchisimo mas facil analizar los puntos criticos del programa, como a su vez, correr el programa, si lo comparamos con la manera tradicional, tendriamos que 
una mayor cantidad de lineas de codigo  para el debuggeo, es decir, nuestras probabilidades de encontrar un error aunque sea muy diminuto, nos consumira mucho mas tiempo y recurso humano para su solucion.

2.- No-asignacion de variables: al no asignar variables tanto locales como  globales, permite que no exista una mutabilidad, esto quiere decir que, en cualquier parte de nuestro codigo no hay una reasignacion que nos pueda "complicar" en el momento de manejar variables. Esto podemos ver claramente en merge_sort, donde se asignan variables de Left y right, donde al momento de ejecutar el ordenamiento se aplica recursividad, a simple vista esto nos puede resultar bastante engorroso y probablemente en su desarrollo pueda causar bastantes dolores de cabeza.

3.- Recursividad: La principal forma en que la programacion funcional es mucho mejor que la programacion tradicional, es a traves de la recursividad, en ambitos de calculos matematicos, la ejecucion de una recursividad implica ahorrar tiempo y costos de produccion, por ende, el desarrollo de una formula para obtener un resultado es muchisimo mas facil implementarlo en paradigma funcional que un paradigma imperativo.

Concluyendo, tenemos que los paradigmas funcionales son sumamente importantes en ambitos de desarrollo con enfoques matematicos, no obstante, su implementacion resulta ser bastante engorrosa y por ende, hay casos donde se deciden por tomar el camino del paradigma imperativo.





Benjamin Parraguez
Seccion 1
Lenguaje y Paradigmas de la programacion
2020/1






## Proyecto: WebScrapping.

El proyecto, permite hacer webscraping entre 3 sitios webs(latercera.com, emol.com y twitter.com), esto nos permite obtener informacion sobre los articulos, como el el titulo de la noticia, su autor y fecha o hora, entre otros.

## Pre-requisitos
Debe tener instalado Google Chrome Navegador Web.
Debe tener instalada una biblioteca de Python, para obternetlas debe ingresar el siguiente comando en el cmd de windowns.

- pip install selenium

Selenium es una biblioteca que nos permite hacer webscraping sin APIs, contiene una serie de funciones que nos ayudan a sacar informacion copiando los "Xpath", esta informacion puede ser procesada e imprimida por pantalla. 

## Usando el programa de WebScrapping
Abrir el archivo comprimido ZIP y descomprimirlo en una carpeta.
Abrir la carpeta en donde se descomprimieron los archivos .py con un IDE de preferencia.
Buscar el archivo main.py y correr el archivo en la consola de comando (darle play).
En el terminal aparece un mensaje pidiendole ingresar una palabra, ingrese la palabra que desea que el programa busque en los sitios.
Para probar el programa le recomendamos probarlo con la palabra "coronavirus" que fue la que utilizamos y sabemos que tiene resultados en todas las paginas.

>IMPORTANTE< : una vez iniciado el programa debe maximizar las pestanas y/o ventanas de Google Chrome que se abran, luego puede usarlas miminizadas, pero en primera instancia deben ir siendo maximizadas.
El programa iniciara sesion en twitter con una cuenta entregada por nosotros, puesta en el codigo.
el webdriver debe estar en la misma carpeta que los archivos .py al momento de correr el programa.
Emol no publica noticias en twitter por lo tanto no pudimos sacar informacion relevante de su pagina de twitter.

## Diarios.py

Cuenta con dos funciones, latercera y emol, las cuales se encargan de realizar la busqueda y extraccion dentro de las paginas respectivas, esto lo hace con la biblioteca selenium, buscando los "Xpath" de los elementos de las paginas.
Mientras que para la funcion emol, posee una leve pero gran diferencia a la hora de filtrar la busqueda, que se enfoca en buscar solamente noticias de la misma página y no de otros sitios asociados a ella (véase Soy Chile, el mercurio, entre otras), 
por lo que el funcionamiento consta de identificar todos los links y buscar al cual esta vinculado a emol (autor emol), y posteriormente, realizar click al enlace y proceder al scrap de la noticia.

## Twitter.py

El archivo contiene una clase, la cual contendra la informacion extraida de twitter, tambien contiene una funcion llamada twitter la que se encarga de conseguir la informacion para luego ser guardada en un objeto y retornada.

## main.py

En este archivo se llaman las funciones creadas anteriormente en Twitter.py y en Diarios.py para que nos entreguen los objetos y asi trabajar con atributos de cada objeto para luego compararlos funcionalmente, en el programa se compara:

1.- Si existe la misma noticia en emol y la tercera
2.- La diferencia de hora entre la subida de la noticia de la tercera en twitter vs la hora de subida en la pagina de la tercera 


## Contribudores

- Tomas Castelblanco
- Cristobal Nazar
- Benjamin Parraguez
- Cristobal Uriarte


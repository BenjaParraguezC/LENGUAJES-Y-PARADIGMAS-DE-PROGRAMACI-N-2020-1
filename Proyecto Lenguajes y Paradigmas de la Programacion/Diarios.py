from selenium import webdriver 
from time import sleep  

class Noticia:
    def __init__ (self, titulo, autor, fecha):
        self.titulo=titulo
        self.autor= autor
        self.fecha= fecha
        

    def __str__(self):
        return '{}\n {}\n ({})\n '.format(self.titulo, self.autor, self.fecha)    

    def entrega_info_latercera(self):
        print("INFORMACION LA TERCERA")
        print("=====================")
        print("El titulo de la noticia es: ", self.titulo )
        print("El autor de la noticia es: ", self.autor)
        print("La hora de publicacion fue: ", self.fecha)
        print("=====================")  

    def entrega_info_emol(self):
        print("INFORMACION EMOL")
        print("=====================")
        print("El titulo de la noticia es: ", self.titulo )
        print("El autor de la noticia es: ", self.autor)
        print("La hora de publicacion fue: ", self.fecha)
        print("=====================") 


def latercera(titu):   
    driver = webdriver.Chrome('./chromedriver.exe')
    link= "https://www.latercera.com/search/?q=" + titu
    buscador_tercera = link

    driver.get(buscador_tercera)
    sleep(25)

    primer_link = driver.find_element_by_xpath('//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a/b[2]')
    primer_link.click()
    sleep(4)

    driver.switch_to.window(driver.window_handles[1])

    x = driver.current_url

    driver.get(x)
    sleep(25)
    

    titular = driver.find_element_by_xpath ('//*[@id="fusion-app"]/section/article/header/div/div[1]/h1/div')
    titular1=titular.text
    autor = driver.find_element_by_xpath('//*[@id="fusion-app"]/section/article/header/div/div[2]/div/div/div/a/small')
    autor1= autor.text
    hora  =  driver.find_element_by_xpath('//*[@id="fusion-app"]/section/article/header/div/div[2]/div/time/small/b')
    hora1 = hora.text

    latercera= Noticia(titular1,autor1, hora1)

    latercera.entrega_info_latercera()

    return latercera
 

def emol(busqueda):

    driver = webdriver.Chrome('./chromedriver.exe')

    driver.get('https://www.emol.com')
    sleep(13)

    buscador = driver.find_element_by_xpath ('//*[@id="frase_busqueda"]')
    buscador.send_keys(busqueda) 

    search = driver.find_element_by_xpath('//*[@id="ucHomePage_cuHeader_cuBuscador_logoLupa"]')
    search.click()
    sleep(3)

    Primera_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[0].text
    Segunda_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[1].text
    Tercera_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[2].text
    Cuarta_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[3].text
    Quinta_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[4].text
    Sexta_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[5].text
    Septima_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[6].text
    Octava_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[7].text
    Novena_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[8].text
    Decima_noticia = driver.find_elements_by_xpath('//*[@id="linkNombreSitio"]')[9].text

    #filtramos

    if (Primera_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[0].click()
        sleep(3)

    elif (Segunda_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[1].click()
        sleep(3)

    elif (Tercera_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[2].click()
        sleep(3)

    elif (Cuarta_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[3].click()
        sleep(3)

    elif (Quinta_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[4].click()
        sleep(3)

    elif (Sexta_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[5].click()
        sleep(3)

    elif (Septima_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[6].click()
        sleep(3)

    elif (Octava_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[7].click()
        sleep(3)

    elif (Novena_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[8].click()
        sleep(3)

    elif (Decima_noticia == "Emol"):

        noticias1 = driver.find_elements_by_xpath('//*[@id="LinkNoticia"]')[9].click()
        sleep(3)


    driver.switch_to.window(driver.window_handles[1])

    x =driver.current_url

    driver.get(x)

    titular = driver.find_element_by_xpath ('//*[@id="cuDetalle_cuTitular_tituloNoticia"]')
    titular1=titular.text
    hora = driver.find_element_by_xpath ('//*[@id="barra-agencias-info"]/div[1]')
    hora1 = hora.text
    autor = driver.find_element_by_xpath ('//*[@id="barra-agencias-info"]/div[1]/a')
    autor1= autor.text
    #contenido = driver.find_element_by_xpath ('//*[@id="cuDetalle_cuTexto_textoNoticia"]').text

    emol= Noticia(titular1,autor1, hora1)
    #metodo de la clase noticia
    emol.entrega_info_emol()

    return emol








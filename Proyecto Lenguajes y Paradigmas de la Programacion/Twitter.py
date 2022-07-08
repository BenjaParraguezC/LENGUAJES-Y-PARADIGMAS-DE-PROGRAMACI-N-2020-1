from selenium import webdriver 
from time import sleep  

class Twitter:
    def __init__ (self,  usuario, fecha, texto):
        self.usuario= usuario
        self.fecha=fecha
        self.texto=texto
        

    def __str__(self):
        return '{}\n {}\n {}\n '.format(self.usuario,self.fecha, self.texto )    

    def entrega_info(self):
        print("INFORMACION TWITTER")
        print("=====================")
        print("El usuario que hizo el twitt fue: ", self.usuario)
        print("El post se hizo: ", self.fecha)
        print("El twitt es: ", self.texto)   
        print("=====================")

def twitter(busqueda):
    driver = webdriver.Chrome('./chromedriver.exe')

    driver.get('https://twitter.com/login')
    sleep(3)


    login= driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
    login.send_keys('tomasbenja.nazaruriarte@gmail.com')

    password=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
    password.send_keys('infomancos123')

    boton_iniciar_sesion=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
    boton_iniciar_sesion.click()

    def gethashtagURL(hashtagname):
        return "https://twitter.com/search?q=" + hashtagname+ "&src=trend_click"


    driver.get(gethashtagURL(busqueda))
    sleep(10)

    seguidos =driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/label[3]/div[2]/input')
    seguidos.click()
    sleep(4)


    info= driver.find_element_by_tag_name('article')
    info_1=info.text
    arreglo_articulo=(info_1.split('\n'))

    if(arreglo_articulo[4][1]=="@"):
        aux= arreglo_articulo[5]
        nuevo_arreglo=aux.split(' ')

        l=len(nuevo_arreglo)

        nuevo_arreglo.pop(l-1)
        titu=" ".join(nuevo_arreglo)

    else:
        aux= arreglo_articulo[4]
        nuevo_arreglo=aux.split(' ')

        l=len(nuevo_arreglo)

        nuevo_arreglo.pop(l-1)
        titu=" ".join(nuevo_arreglo)

    twitt= Twitter(arreglo_articulo[1], arreglo_articulo[3], titu) 

    twitt.entrega_info()
    return twitt




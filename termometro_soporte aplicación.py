import pygame, sys
from pygame.locals import*

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F': #si voy a convertir a F
            resultado = grados * 9/5 +32
        elif toUnidad == 'C':
            resultado = (grados - 32) *5/9
        else:
            resultado = grados
        
        return "{:10.2f}".format(resultado)
            
        
class Selector():
    #va a tener un atributo: en F o C. Y un método: el clic para cambiar.
    __tipoUnidad = None
    
    def __init__(self, unidad="C"):
        self.__customes =[]#creamos lista de disfraces y se la asignamos.
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad
        
    def Selector:
        
        if self.__tipoUnidad == 'F':
            return self.__customes[0]
        else:
            return self.__customes[1]
    def custome(self):
        if self.__tipoUnidad == 'F':
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    
    def change(self, event):
            if self.__tipoUnidad == 'F':
                self.__tipoUnidad = 'C'
            else:
                self.__tipoUnidad = 'F'
    
    def unidad(self):#es un getter, te da el tipo de unidad en el que está.
        return self.__tipoUnidad
                
        

class NumberInput():
   #ponemos el atributo valor del termómetro privado y le damos una posición y un tamaño:
    __value = 0 #tenemos que tener estos valores siempre iguales: value y strValue. Lo necesitamos pasar a cadena porque RENDER SÓLO RENDERIZA CADENAS.
    __strValue = ""
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0
   
    def __init__(self, value=0):
       #creamos la fuente con la que cogemos el número de la temperatura. La creamos como privada.
       self.__font = pygame.font.SysFonft("Arial", 24)
       self.value(value) #Llamamos a un método que he creado, que está dentro de mi clase y Python lo ha tenido que leer ya.
       
       #Creamos un método para renderizar el texto

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0): #unicode nos da el contenido de la tecla, también se podría haber puesto event.unicode in '0123456789'
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointsCount += 1
                
            elif event.key == K_BACKSPACE:
                if self.__straValue[-1] == '.':
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[0:-1] #Nos devuelve toda la cadena menos la última posición (-1)
                self.value(self.__strValue)
                

    def render(self): #Render SOLO RENDERIZA CADENAS.
    #creamos una variable de trabajo. Va a haber el recuadro de entrada de datos y el recuadro donde metes el número.
       textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
       #Creamos el rectángulo puramente gráfico:
       rect = textBlock.get_rect()
       #Al rectángulo le informamos la posición y le damos un tamaño:
       rect.left = self.__position[0]
       rect.top = self.__position[1]
       rect.size = self.__size
       
       '''
       #Tengo que devolver lo que necesito para pintarlo. Lo hago con un diccionario:
       return {
               "fondo": rect,
               "texto": textBlock
           }
           '''
       
        #Tengo que devolver lo que necesito para pintarlo. Lo hago con una tupla:
       return (rect, textBlock)
       
   #Tenemos que crearnos los getter y setter de nuestros atributos privados:    
    def value(self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = float(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass #Si produce un error, voy a pasar. Lo ideal sería poner un mensaje controlado. Lo dejamos para más adelante.
    
    def width(self, val=None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass

    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
      
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass

    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass

    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
      
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass        


class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203))
        
        self.termometro = Termometro() #He creado una instancia de termómetro y se la asigno.
        #Creamos la entrada de datos en el recuadro.
        self.entrada = NumberInput()
        #Creamos especificaciones de nuestro control de entrada:
        self.entrada.pos ((106, 58))
        self.entrada.size ((133,28))
                
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir8grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                
                self.selector.on_event(event)
                    
            #Pintamos el fondo de pantalla:
            self.__screen.fill((244, 236, 203))
            
                    
            #Pintamos el termómetro en su posición:
            self.__screen.blit(self.termometro.custome, (50, 34))
            
            #Pintamos el cuadro de texto
            text = self.entrada.render()# Obtenemos rectángulo blanco y foto de texto y lo asignamos a text.
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) #Creamos el rectángulo blanco con sus datos (posición y tamaño) text[0].
            self.__screen.blit(text[1], self.entrada.pos()) #Cojo el texto del cuadro de texto, que está en lo que devuelve la variable render.
                                                        #Doble paréntesis porque es un getter.
                        
            #Pintamos el selector:
            self.__screen.blit(self.selector.custome(), (112, 153))
            
            pygame.display.flip()
                
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()
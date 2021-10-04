
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import os, sys, time, commands
import pygame
from pygame.locals import *


# revisar par ocultar en mouse
#pygame.mouse.set_visible(bool) # invisible


#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

#--- Para Ventana grafica
DEBUG_Teclado = 1 # 0: ventana minimizada # 1: FULLSCREEN
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 480
win_pos_x=350
win_pos_y=100


#--- Para Dormir proceso de pintar y eventos
MIN_T_Espera = 0.06
MAX_T_Espera = 3


#--- Para graficar
Link_Fondo_1        = "/home/pi/Firmware/img/keypad-fondo.png"
Link_Fondo_2        = "/home/pi/Firmware/img/Keypad-Borrar_Amarillo.png"
Link_Denegado       = "/home/pi/Firmware/img/denegado.png"
Link_Permitido      = "/home/pi/Firmware/img/permitido.png"
Link_Per_Derecha    = "/home/pi/Firmware/img/derecha.png"
Link_Alerta         = "/home/pi/Firmware/img/alerta2.png"







#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------
#--- Para Dormir proceso de pintar y eventos
T_Espera = MIN_T_Espera
NO_even=0


#--- Para graficar
Fondo_1 =''
Fondo_2 =''
Denegado =''
Permitido =''
Per_Derecha =''
Per_Izquierda =''

#--- Fuentes de texto
Fuente_1 = ''#pygame.font.SysFont("Arial", 40)
Fuente_2 = ''#pygame.font.SysFont("Arial", 20)
Alerta = ''















#-------------------------------------------------------
#----               Funciones                       ----
#-------------------------------------------------------



# *****-----------------------------------------------------------
# *****Funciones para dormir el proceso de pintade y de eventos
def Dormir_procesos():
    global T_Espera
    global MIN_T_Espera
    global NO_even
    NO_even= NO_even + 1
    if NO_even>=100:
        NO_even=0
        T_Espera = T_Espera + 0.1
        if T_Espera >= MAX_T_Espera:
            T_Espera = MAX_T_Espera
# *****------
def Tiempo_Espara_Proceso():
    global T_Espera
    time.sleep(T_Espera)
# *****------
def Reset_Tiempo_proceso():
    global T_Espera
    #print 'Evento:'+ str(T_Espera)
    T_Espera = MIN_T_Espera
# *****------
# *****-----------------------------------------------------------





# *****-----------------------------------------------------------
# *****Funciones dibujos de pygame
# *****------

def Pintar_fondo(a):
    global Fondo_1
    global Fondo_2

    if a == 1 : screen.blit(Fondo_1, (0, 0))
    if a == 2 : screen.blit(Fondo_2, (0, 0))
# *****------
def Pintar_Estado_Usuario(Texto):
    global Denegado
    global Permitido
    global Per_Derecha
    global Per_Izquierda

    if Texto != 'Denegar'           : pygame.draw.rect(screen,(255,255,255),[20,5,285,465])
    if Texto == 'Denegar'           : screen.blit(Denegado, (-20, 70))
    if Texto == 'Permitido'         : screen.blit(Permitido, (20, 100))
    if Texto == 'Per_Derecha'       : screen.blit(Per_Derecha, (20, 100))
    if Texto == 'Per_Izquierda'     : screen.blit(Per_Izquierda, (20, 100))
# *****------
def Pintar_Estado_Red(x, Texto):
    # 'sin_eth' 'con_eth' 'sin_wif' 'con_wif'
    if Texto == 'sin_eth'           : Estados_Red(x, 0, 0) # sin ethernet
    elif Texto == 'con_eth'           : Estados_Red(x, 1, 0) # con ethernet
    elif Texto == 'sin_wif'           : Estados_Red(x, 0, 1) # sin wifi
    elif Texto == 'con_wif'           : Estados_Red(x, 1, 1) # con wifi

def Estados_Red(x1, Relleno, Tipo_comec):

    pygame.draw.circle(screen,(32,112,164),(5+(10)*x1, 475),5,Relleno)
    if Tipo_comec == 1 :    pygame.draw.line(screen,(0,0,0),(0+(10)*x1 , 475) ,(8+(10)*x1 , 475))


def Pintar_Status_Red(red):
    for x1 in range(int(red[0])):
        conec= red[1+x1*2]+ red[2+x1*2]
        #print conec +' '+ str(x1)
        if conec == 'ED' :  Pintar_Estado_Red(x1, 'sin_eth')    #Azul oscura ethernet desconectado
        elif conec == 'EC' : Pintar_Estado_Red(x1, 'con_eth')    #Azul claro ethernet conectado
        elif conec == 'WD' : Pintar_Estado_Red(x1, 'sin_wif')    #Azul oscura wifi desconectado
        elif conec == 'WC' : Pintar_Estado_Red(x1, 'con_wif')    #Azul claro wifi conectado

# *****------

def Pintar_mensaje( x, y, texto):
    global Fuente_1

    pygame.draw.rect(screen,(32,112,164), (x,y-10, 245, 250))
    fuente = Fuente_1
    texto_en_lineas = texto.split('\n') # ejemplo: convierte "hola \n mundo" en ["hola ", " mundo"
    for linea in texto_en_lineas:
        nueva = fuente.render(linea, 1, (0,0,0))
        screen.blit(nueva, (x, y))
        y += nueva.get_height()

def Pintar_Alerta():
    global Alerta
    screen.blit(Alerta, (0,0))

def Pintar_Display(Texto_Display):
    global Fuente_1
    fuente = Fuente_2
    mensaje = fuente.render(Texto_Display, 1, (255, 255, 255))
    screen.blit(mensaje, (40, 10))


def Inicializaciones_Graficas():
    global Fondo_1
    global Fondo_2
    global Link_Fondo_1
    global Link_Fondo_2
    global Denegado
    global Link_Denegado
    global Permitido
    global Link_Permitido
    global Per_Derecha
    global Link_Per_Derecha
    global Per_Izquierda
    global Fuente_1
    global Fuente_2
    global Alerta
    global Link_Alerta

    Fuente_1 = pygame.font.SysFont("Arial", 20)
    Fuente_2 = pygame.font.SysFont("Arial", 40)
    Fondo_1       = pygame.image.load(Link_Fondo_1).convert()
    Fondo_2       = pygame.image.load(Link_Fondo_2).convert()
    Denegado      = pygame.image.load(Link_Denegado).convert_alpha()
    Denegado      = pygame.transform.scale(Denegado,(330,310))
    Permitido     = pygame.image.load(Link_Permitido).convert_alpha()
    Per_Derecha   = pygame.image.load(Link_Per_Derecha).convert_alpha()
    Per_Derecha   = pygame.transform.scale(Per_Derecha,(290,290))
    Per_Izquierda = pygame.transform.rotate(Per_Derecha,180)
    Alerta        = pygame.image.load(Link_Alerta).convert_alpha()
# *****------



















#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
pygame.init()

#-----      Configuracion de ventana   --------
if DEBUG_Teclado == 0:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (win_pos_x, win_pos_y)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
else:
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#----------------------------------------------




#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

#Pintar_Estado_Usuario('Denegar') #'Denegar', 'Permitido' , 'Per_Derecha' 'Per_Izquierda'
#Pintar_Estado_Red(0, 'sin_eth') # 'sin_eth' 'con_eth' 'sin_wif' 'con_wif'
#Pintar_mensaje( 38, 70, "Hola") #cuadro azul
#Pintar_Display("Anderson") #
#Pintar_Alerta() #avisos : El QR ya se proceso, retire su celular

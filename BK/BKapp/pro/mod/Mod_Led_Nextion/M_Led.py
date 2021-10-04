#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
# Es independiente por que se ejecuta en Python 3.5
#-------------------------------------------------------

import digitalio
from board import *
import time, os
import neopixel
import threading

#from lib.Lib_File import *
#import lib
#lib.Lib_File

#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------
COM_LED = '/home/pi/Firmware/db/Command/Led/Com_Led.txt'

PIXEL_PIN = D21#D21             #pin de control
num_pixels = 10#8#10             #Numero de pixels
num_medio = int(num_pixels/2)   #Mitad de pixel
Led_int=120                     #Intensidad luminica
ORDER = neopixel.RGB            #Pixel color channel order

DELAY = 500

pixel = neopixel.NeoPixel(PIXEL_PIN, num_pixels, pixel_order=ORDER)

Comando_Antes = 0
Salir_hilo = 0
#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------

#-----------------------------------------------------------
#----      Funciones para el manejo de los led     ----
#-----------------------------------------------------------
def Color(Nombre,ID):
    global num_medio
    global Led_int

    COLOR = (0, 0, 0)
    mitad=0
    if 'Verde' == Nombre:       COLOR = ( Led_int, 0, 0)
    elif 'Azul' == Nombre:      COLOR = ( 0, 0, Led_int)
    elif 'Negro' == Nombre:     COLOR = ( 0, 0, 0)
    elif 'Rojo' == Nombre:      COLOR = ( 0, Led_int, 0)
    elif 'Amarillo' == Nombre:  COLOR = ( Led_int, Led_int, 0)
    elif 'Blanco' == Nombre:    COLOR = ( Led_int, Led_int, Led_int)
    else :                      COLOR = ( 0, 0, 0)

    if ID == 1: mitad=num_medio
    for j in range(num_medio):
        pixel[j+mitad] = COLOR

#-----------------------------------------------------------
def Ejecutar_Comando(CL_Estados):
    if CL_Estados == '0':	#Estado Inicial
            Color('Azul',1)
            Color('Azul',0)
    elif	CL_Estados == '1':	#blink
            Color('Amarillo',1)
            Color('Amarillo',0)
    elif	CL_Estados == '2':	#blink
            Color('Blanco',1)
            Color('Blanco',0)
    elif	CL_Estados == '3':	#Entrar
            Color('Verde',1)
            Color('Negro',0)
    elif	CL_Estados == '4':	#Salir
            Color('Negro',1)
            Color('Verde',0)
    elif	CL_Estados == '5':	#Sin Acceso
            Color('Rojo',1)
            Color('Rojo',0)
    elif	CL_Estados == '6':	#blink
            Color('Rojo',1)
            Color('Rojo',0)
    elif	CL_Estados == '7':	#Usuario digita Rut sin internet
            Color('Amarillo',1)
            Color('Amarillo',0)
    elif	CL_Estados == '8':	#Usuario digita Rut con internet
            Color('Blanco',1)
            Color('Blanco',0)
    else :						#No definido
            Color('Negro',1)
            Color('Negro',0)

#---------------------------------------------------------
def Borrar_Comando_Led():
    global COM_LED
    arch = COM_LED #'/home/pi/Firmware/db/Status/Estado_Led.txt' #Get_archivo(a)
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write("")
        archivo.close()
#-------------------------------------------------------
def Leer_Comando():
    global COM_LED
    arch = COM_LED #'/home/pi/Firmware/db/Status/Estado_Led.txt' #Get_archivo(a)
    mensaje = ""
    if os.path.exists(arch):
        f = open (arch,'r')
        mensaje = f.read()
        #print(mensaje)
        f.close()
        return mensaje
    else:
        return mensaje
#-------------------------------------------------------
def Blink():
    global Comando_Antes
    global Salir_hilo
    global DELAY
    #print ('Activar Hilo')
    #print (Comando_Antes)
    contador = 0
    while (True):
        time.sleep(0.0001)
        #print (contador)
        contador = contador + 1
        if contador == 1:   # and contador <= 20 :
            #print (Comando_Antes)
            Ejecutar_Comando(Comando_Antes)
        if contador == int(DELAY/2):    Ejecutar_Comando('n')
        if contador >= DELAY:           contador =0
        if Salir_hilo == 0:             break;
    #print ('Salir del hilo')

#-------------------------------------------------------
def Activar_Hilo_Comando():
    global B_Hilo_Comado
    #print ('Activar Hilo')
    if B_Hilo_Comado.isAlive() is False:
        B_Hilo_Comado = threading.Thread(target=Blink)#, args=(0,))
        B_Hilo_Comado.start()

def Eventos_Led():
    global Comando_Antes
    global Salir_hilo

    while (True):
        time.sleep(0.05)
        Comando =Leer_Comando()
        if Comando != '':
            if Comando != Comando_Antes :
                #print (Comando)
                Salir_hilo = 0
                Comando_Antes = Comando
                if Comando == '6' or Comando == '1' or Comando == '2':
                    Salir_hilo = 1
                    Activar_Hilo_Comando()
                else :
                    Ejecutar_Comando(Comando)
                Borrar_Comando_Led()


#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
Color('Azul',1)
Color('Amarillo',0)
B_Hilo_Comado   = threading.Thread(target=Blink)#, args=(0,))

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------


#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

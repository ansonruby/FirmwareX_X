#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import os
import time

import RPi.GPIO as GPIO #Libreria Python GPIO

#-----------------------------------------------------------
#                       CONSTANTES
#-----------------------------------------------------------
# Rutas para el control y comandos del sonido
FIRM            = '/home/pi/Firmware/'                      # Ruta Firmware
COMMA           = 'db/Command/'                             # Rutas comandos
COM_BUZZER      = FIRM + COMMA + 'Buzzer/Com_Buzzer.txt'    # Archivo de comandos

Pin_Buzzer      = 7                                         # Pin de salida de Buzzer
Tiempo_sonido   = 0.05                                       # Tiempo minimo de activacion

#-----------------------------------------------------------
#-----------------------------------------------------------
#----      Funciones para de usua general               ----
#-----------------------------------------------------------
#-----------------------------------------------------------

#-------------------------------------------------------
#----      Funciones para el manejo de archivos     ----
#-------------------------------------------------------
def Clear_File(arch):                                       # Borrar un archivo y revicion si existe
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write("")
        archivo.close()

#-------------------------------------------------------
def Get_File(arch):                                         # Leer un archivo y revicion si existe
    mensaje = ""
    if os.path.exists(arch):
        f = open (arch,'r')
        mensaje = f.read()
        #print(mensaje)
        f.close()
        return mensaje
    else:
        return mensaje                                      # ? es necesario colocar una vandera si no esta?

#-------------------------------------------------------



#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------

Dato_Antes = '0'                                            # Estado antes del comando
#-----------------------------------------------------------
#----      Funciones para el manejo del buzzer     ----
#-----------------------------------------------------------

def sonido(Rango):                                           # Funcion para Activar sonido

    global CC_Pin
    GPIO.output(Pin_Buzzer, GPIO.HIGH)
    time.sleep(Rango)
    GPIO.output(Pin_Buzzer, GPIO.LOW)

#-----------------------------------------------------------
def Control_Sonidos_Por_Archivo():                          # Seleccion de sonido

    global Tiempo_sonido
    global Dato_Antes
    Dato = Get_File(COM_BUZZER)
    if len(Dato) >= 1 :
        Clear_File(COM_BUZZER)
        if      (Dato =='0'): sonido(Tiempo_sonido*1)
        elif    (Dato =='1'): sonido(Tiempo_sonido*2)
        elif    (Dato =='2'): sonido(Tiempo_sonido*3)
        elif    (Dato =='3'): sonido(Tiempo_sonido*4)
        elif    (Dato =='4'): sonido(Tiempo_sonido*5)

#-----------------------------------------------------------
def Ciclo_Buzzer():
    while (True):
        time.sleep(0.1)                # 0.05
        Control_Sonidos_Por_Archivo()

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

GPIO.setmode (GPIO.BOARD)
GPIO.setup(Pin_Buzzer, GPIO.OUT)
#-----------------------------------------------------------
#               Pruebas de funcionamiento
#-----------------------------------------------------------

#sonido(0.05*5)
#Ciclo_Buzzer()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
# sonido(Rango):
# Control_Sonidos_Por_Archivo():

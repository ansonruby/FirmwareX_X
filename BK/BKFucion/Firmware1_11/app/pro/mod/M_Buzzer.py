#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
from lib.Lib_File import *  # importar con los mismos nombres
#from lib.L_Archivos import *  # importar con los mismos nombres
import time
import RPi.GPIO as GPIO #Libreria Python GPIO
#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

Pin_Buzzer =  7         #   Pin de salida de Buzzer
Tiempo_sonido = 500     #   Tiempo minimo de activacion
#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#Get_Sonido          = Leer_Archivo
#Delate_Sonido       = Borrar_Archivo
#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------

Dato_Antes = '0'
contador=0
#-----------------------------------------------------------
#----      Funciones para el manejo del buzzer     ----
#-----------------------------------------------------------

def sonido(Rango):

    global CC_Pin
    for CT_m in range(Rango):
        GPIO.output(Pin_Buzzer, GPIO.HIGH)
    GPIO.output(Pin_Buzzer, GPIO.LOW)

#-----------------------------------------------------------
def Control_Sonidos_Por_Archivo():

    global Tiempo_sonido
    global Dato_Antes
    global contador
    if Get_File(COM_BUZZER) != Dato_Antes :
        Dato_Antes = Get_File(COM_BUZZER)
        #print 'cambio' + Dato_Antes
        Clear_File(COM_BUZZER)
        if      (Dato_Antes =='0'): sonido(Tiempo_sonido*1)
        elif    (Dato_Antes =='1'): sonido(Tiempo_sonido*2)
        elif    (Dato_Antes =='2'): sonido(Tiempo_sonido*3)
        elif    (Dato_Antes =='3'): sonido(Tiempo_sonido*4)

#-----------------------------------------------------------
def Ciclo_Buzzer():
    while (True):
        time.sleep(0.05)
        Control_Sonidos_Por_Archivo()

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

GPIO.setmode (GPIO.BOARD)
GPIO.setup(Pin_Buzzer, GPIO.OUT)
#-----------------------------------------------------------
#               Pruebas de funcionamiento
#-----------------------------------------------------------

#sonido(500)
#Ciclo_Buzzer()


#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
# sonido(Rango):
# Control_Sonidos_Por_Archivo():

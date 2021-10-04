
import commands
import sys
import time
import RPi.GPIO as GPIO #Libreria Python GPIO
import threading

import lib.Control_Torniquete
import lib.Control_Archivos


Entrar                  = lib.Control_Torniquete.Entrar
Salir                   = lib.Control_Torniquete.Salir

Leer_Estado             = lib.Control_Archivos.Leer_Estado
Escrivir_Estados        = lib.Control_Archivos.Escrivir_Estados



GPIO.setmode (GPIO.BOARD)
CC_Pin_Seguridad =  36 #8sin fuentee #3 para la sinta de seguridad
GPIO.setup(CC_Pin_Seguridad, GPIO.IN)
a = '0'
b = '0'
Status_Hilo_activo =0



Estados = '6' #estados del dispositivos para visualizar en los leds
Estados_Antes = '0'

def Cambio_Estado_Led(Es):

    global Estados
    Estados = Es
    Led_Estados()


def Led_Estados():

    global Estados
    global Estados_Antes

    if Estados_Antes != Estados:
        Estados_Antes = Estados
        Escrivir_Estados(Estados,3)
        Escrivir_Estados(Estados,10)

#-----------------------------------------------------------
def Get_Switch():
        b= str(GPIO.input(CC_Pin_Seguridad))
        return b

#-----------------------------------------------------------
def Eventos_Boton_Salida():
    global Status_Hilo_activo
    a= Get_Switch() #GPIO.input(CC_Pin_UPS)
    #print 'Buttom:'+str(a)
    if Get_Switch() == '1' and Status_Hilo_activo == 0:
        Activar_Hilos_Boton()

#-----------------------------------------------------------
def Activar_Hilos_Boton():
    global Boton_Activo
    global Status_Hilo_activo

    if Boton_Activo.isAlive() is False:
        Boton_Activo = threading.Thread(target=Proceso_Salir_Por_Boton)#, args=(0,))
        Boton_Activo.start()
        Status_Hilo_activo = 1
        #print 'Activado'

#-----------------------------------------------------------
def Proceso_Salir_Por_Boton():
    global Status_Hilo_activo

    #activasion de salida Direc_Torniquete
    if Leer_Estado(13) == 'D':
        Cambio_Estado_Led('3')
        Entrar()
    else :
        Cambio_Estado_Led('4')
        Salir()

    Cambio_Estado_Led('0')  #volver a estado de inicio
    #print 'fin ciclo del rele'
    #enviar estado de aforos

    #esperar que lo suelten
    while 1:
        time.sleep(0.05)
        if Get_Switch() == '0':
            #print 'stop'
            break
    Status_Hilo_activo = 0


#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
Boton_Activo   = threading.Thread(target=Proceso_Salir_Por_Boton)#, args=(0,))
#H_S_QR  = threading.Thread(target=P_Servidor_QR)#,  args=(0,))



#se deve utilizar uuna memoria permanente
"""
print 'hola'
while (True):

        time.sleep(0.05)
        Eventos_Boton_Salida()
"""

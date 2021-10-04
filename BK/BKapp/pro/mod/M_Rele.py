# -*- coding: utf-8 -*-
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import time

import RPi.GPIO as GPIO #Libreria Python GPIO
import threading

from lib.Lib_File import *  # importar con los mismos nombres
from lib.Setting import *  # importar con los mismos nombres
#from lib.L_Tiempo import *  # importar con los mismos nombres
#from lib.L_Archivos import *  # importar con los mismos nombres
#from M_Inf_Dispositivo import *  # importar con los mismos nombres
#import time


#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

#        Entrada, Salida de los relevos
Rele =   [37,38]        #16, 19 #[21,23]

#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------


#-----------------------------------------------------------
#----      Funciones para el manejo de los relevos     ----
#-----------------------------------------------------------
def Actividad_Rele(Direccion):
    global Rele
    Tiempo_Rele =int(Get_File(CONF_TIEM_RELE))
    GPIO.output(Rele[Direccion], GPIO.LOW)
    time.sleep(Tiempo_Rele)
    GPIO.output(Rele[Direccion], GPIO.HIGH)

#-----------------------------------------------------------
def Comando_Rele(Direccion):
    Tiempo_Rele =int(Get_File(CONF_TIEM_RELE))
    Clear_File(COM_TX_RELE)
    if Direccion == 0:      Set_File(COM_TX_RELE,"¿00000004000" + str(Tiempo_Rele) + "?") #Entrar
    elif Direccion == 1:    Set_File(COM_TX_RELE,"¿00000004010" + str(Tiempo_Rele) + "?") #Salir
    elif Direccion == 2:    Set_File(COM_TX_RELE,"¿000000040300?")                              #Cerrar

#-----------------------------------------------------------
def Entrar():
    global ID_Disp
    global Cons_Dispo
    if ID_Disp.find(Cons_Dispo) != -1:  Comando_Rele(0)       #Para dispositivos CCCB
    else:                           Actividad_Rele(0)     #Para dispositivos con relevos

#-----------------------------------------------------------
def Salir():
    global ID_Disp
    global Cons_Dispo
    if ID_Disp.find(Cons_Dispo) != -1:  Comando_Rele(1)       #Para dispositivos CCCB
    else:                           Actividad_Rele(1)     #Para dispositivos con relevos

#-----------------------------------------------------------
def Cerrado():
    global ID_Disp
    global Cons_Dispo
    if ID_Disp.find(Cons_Dispo) != -1: Comando_Rele(2)       #Para dispositivos CCCB
    else:                          Rele_close()         #Para cerrar pines

#-----------------------------------------------------------
def Rele_close():
    global Rele
    GPIO.output(Rele[0], GPIO.HIGH)# Entrada
    GPIO.output(Rele[1], GPIO.HIGH)# Salida

#-----------------------------------------------------------
def Direcion_Rele(Res):
    global H_S_RELE
    global H_E_RELE
    Direc = Get_File(CONF_DIREC_RELE)   #Leer_Archivo(13)  # Direccion_Torniquete
    if Res == 'Access granted-E':
        if Direc == 'D':
            #Salir()
            if H_S_RELE.isAlive() is False:
                H_S_RELE   = threading.Thread(target=Salir)
                H_S_RELE.start()
        else :
            #Entrar()
            if H_E_RELE.isAlive() is False:
                H_E_RELE   = threading.Thread(target=Entrar)
                H_E_RELE.start()

    elif Res == 'Access granted-S':
        if Direc == 'D':
            #Entrar()
            if H_E_RELE.isAlive() is False:
                H_E_RELE   = threading.Thread(target=Entrar)
                H_E_RELE.start()

        else :
            #Salir()
            if H_S_RELE.isAlive() is False:
                H_S_RELE   = threading.Thread(target=Salir)
                H_S_RELE.start()

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

H_S_RELE   = threading.Thread(target=Salir)
H_E_RELE   = threading.Thread(target=Entrar)


if ID_Disp.find(Cons_Dispo) != -1:
    #print 'sin relevos'
    a=1
else:
    #print 'con relevos'   #Avilitar los pines de los relevos
    GPIO.setmode (GPIO.BOARD)
    for k in range(2):
        GPIO.setup(Rele[k], GPIO.OUT)
    Rele_close()

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------


#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import os
import serial
from serial import SerialException
import time

#-----------------------------------------------------------
#                       CONSTANTES
#-----------------------------------------------------------
# Rutas para el control y comandos del sonido
FIRM            = '/home/pi/Firmware/'                      # Ruta Firmware
COMMA           = 'db/Command/'                             # Rutas comandos
COM_RX          = FIRM + COMMA + 'Serial/Com_Rx.txt'        # Archivo de comandos
COM_TX          = FIRM + COMMA + 'Serial/Com_Tx.txt'        # Archivo de comandos


PP_MeSerial = 0         # 0: NO print  1: Print
Puerto_Serial = '/dev/ttyS0'
RX_Rango= 500

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
def Add_Line_End(arch, Dato): #incluir el/n
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        #print lineas
        f2 =open(arch, "w")
        f2.write(''.join(lineas) )
        f2.write(Dato)
        f2.close()

#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------
port = serial.Serial(Puerto_Serial, baudrate=9600, timeout=1)

#-----------------------------------------------------------
def Recibir_Cadenas(RX_Serial):
    Numero_Caracteres = len(RX_Serial)
    if Numero_Caracteres >= 1:
        if PP_MeSerial:
            print 'N: '+str(Numero_Caracteres)+'RX: '+ RX_Serial

        if RX_Serial.find('\r') != -1:
            Rx =RX_Serial.split('\r')
            for x in Rx:
                #print x
                if len(x) >= 1:     Add_Line_End(COM_RX, x + '\n')

        else:
            #print RX_Serial
            if len(RX_Serial) >= 1: Add_Line_End(COM_RX, RX_Serial + '\n')

def Enviar_cadenas():
    rele = Get_File(COM_TX)
    if len(rele)>= 1:
        #print rele
        port.write(rele)
        Clear_File(COM_TX)


#-----------------------------------------------------------
def Lectura_Serial():

    global port
    global Puerto_Serial
    global RX_Rango

    while True:
        time.sleep(0.05)
        try :

            Enviar_cadenas()
            Recibir_Cadenas(port.read(RX_Rango))

        except SerialException: #   Reiniciar el serial
            while True:
                port = serial.Serial(Puerto_Serial, baudrate=9600, timeout=1)
                break

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------
print 'Listo'

Lectura_Serial()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

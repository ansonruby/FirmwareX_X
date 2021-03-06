#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#----                           importar complementos                               ----
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
import commands
import RPi.GPIO as GPIO #Libreria Python GPIO

from Lib_File import *  # importar con los mismos nombres
#from L_Tiempo import *  # importar con los mismos nombres

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#                                   CONTANTES
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#                                   FUNCIONES
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#                                   DISPOSITIVO
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def Get_MAC():
    MAC_DIRC        = 'cat /sys/class/net/wlan0/address'
    MAC             = commands.getoutput(MAC_DIRC)
    MAC             = MAC.replace(":","")
    return  MAC

#-----------------------------------------------------------
def GET_ID( Mascara = 0): # mejorar por que podia pasa cualquiera
    MAC = Get_MAC()
    Caracte         = ((Get_Line(INF_DISPO, 1)).replace("\n","")).replace("\r","")
    Fecha_Init      = ((Get_Line(INF_DISPO, 2)).replace("\n","")).replace("\r","")
    Consecutivo     = ((Get_Line(INF_DISPO, 3)).replace("\n","")).replace("\r","")
    if Mascara == 0 :   return Caracte+Fecha_Init+MAC+Consecutivo
    else            :   return Caracte+'XXX'+Consecutivo

#-----------------------------------------------------------


#-----------------------------------------------------------
#                   VARIABLES dispositivo
#-----------------------------------------------------------
Cons_Dispo='CCCD' #para avilitar funcionalidades segun sea el dispositivo
ID_Disp = GET_ID()
ID_Disp  = 'CCCB23102020b827eb529826000002' #IF_CHI_02
#ID_Disp  = 'ABDB12022020b827eb8d5a12000022' #SL_CHI_1
ID_Disp_Masc = GET_ID(1)
#faltan las funciones para altera la url
URL_Servidor     = 'https://plataforma.ifchile.com'
#URL_Servidor     = 'http://192.168.0l.104'


#Hora_Actualizacion_Usuarios_servidor
H_Get_Users_serv = "04:00 PM" #"12:10 AM"





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#                               Modulo de Relevos
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

"""
#-----------------------------------------------------------
#                       VARIABLES Relevos
#-----------------------------------------------------------
#        Entrada, Salida de los relevos
Rele =   [37,38]        #16, 19 #[21,23]
Tiempo_Torniquete = int(Leer_Archivo(30))   #tiempo de duracion de los relevos

def Cerrado_Pin():
    global Rele
    GPIO.output(Rele[0], GPIO.HIGH)# Entrada
    GPIO.output(Rele[1], GPIO.HIGH)# Salida

#-----------------------------------------------------------
#                   Configuracion Relevos
#-----------------------------------------------------------

if ID_Disp.find(Cons_Dispo) != -1:
    #print 'sin relevos'
    a=1
else:
    #print 'con relevos'   #Avilitar los pines de los relevos
    GPIO.setmode (GPIO.BOARD)
    for k in range(2):
        GPIO.setup(Rele[k], GPIO.OUT)
    Cerrado_Pin()
"""













#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#                               Modulo
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                   Configuracion
#-----------------------------------------------------------





#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------
#print ID_Disp
#print ID_Disp_Masc

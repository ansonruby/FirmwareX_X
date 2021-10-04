#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
from lib.Setting import *  # importar con los mismos nombres
#from lib.L_Archivos import *  # importar con los mismos nombres
#import time, commands

#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------

#-----------------------------------------------------------
#----      Funciones para la informacion del dispositivo  --
#-----------------------------------------------------------
def GET_Firmware():
    Firmware = ((Get_Line(INF_FIRMWARE, 1)).replace("\n","")).replace("\r","")
    return Firmware.replace("# ","")     # version firmware

#-----------------------------------------------------------
def GET_Vercion():
    Firmware = ((Get_Line(INF_VERCION, 1)).replace("\n","")).replace("\r","")
    return Firmware.replace("# ","")     # version firmware

#-----------------------------------------------------------
def GET_IPS():
    IPs = commands.getoutput('hostname -I')
    return IPs.split(' ')

#-----------------------------------------------------------
def GET_Nombre():
    return commands.getoutput('hostname')

#-----------------------------------------------------------
def GET_Inf():
    Inf = '              '
    Inf += GET_Firmware()+'\n'
    Inf += GET_Vercion()+'\n'
    Inf +='              Nombre\n'
    Inf += GET_Nombre()+'\n'
    Inf +='              Serial\n'
    Inf += GET_ID(1)+'\n'
    Inf +='              Conexion\n'
    IPS = GET_IPS()

    for linea in IPS:
        if len(linea)>=3:
            Inf +='IP: '
            Inf +=linea
            Inf +='\n'
    return Inf

#-----------------------------------------------------------


#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------
#print Leer_Archivo(17)
#print Get_MAC()
#print GET_ID()
#print GET_ID(1)
#print GET_Firmware()
#print GET_Vercion()
#print GET_IPS()
#print GET_Nombre()
#print GET_Inf()
#print GET_STatus_Red()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

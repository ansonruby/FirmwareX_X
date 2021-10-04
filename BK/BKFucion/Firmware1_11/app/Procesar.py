
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import time

from pro.mod.M_Peticion_Usuarios import *  	# importar con los mismos nombres
from pro.mod.lib.Lib_Networks import *  	# importar con los mismos nombres
from pro.mod.M_Procesar_QR import *  		# importar con los mismos nombres

#------------------------------------------------------------------------------
#----           EJECUTAR AL INICIO DEL DISPOSITIVO
#------------------------------------------------------------------------------
if Status_Redes() == 1: Set_File(HILO_STATUS_PETI_USERS, '1') #activar peticion de usuarios

#------------------------------------------------------------------------------
   	#---------------------------------------------------------
	#----						                        ------
	#----				 Programa principal             ------
	#----						                        ------
	#---------------------------------------------------------
#------------------------------------------------------------------------------
print 'listos'
while 1:
	#------------------if PP_Mensajes:---------------------------------------
	#  Proceso 0: Tiempo de espera para disminuir proceso
	#---------------------------------------------------------
	time.sleep(0.05)
	#---------------------------------------------------------
    # Proceso 2: Actualizacion de usuarios del dispositivos
    #---------------------------------------------------------
	Eventos_Usuarios_Server()
	#---------------------------------------------------------
	# Proceso 4: Procesamiento del QR
	#---------------------------------------------------------
	Procesar_QR()

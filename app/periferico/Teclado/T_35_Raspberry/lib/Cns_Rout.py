
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#                                   CONTANTES
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# NOTA: revizar reglas y convenciones de nombres para python

#---------------------------------
#           Rutas Generales
#---------------------------------
FIRM    = '/home/pi/Firmware/'      # Ruta Firmware
DATA    = 'db/Data/'                # Ruta Base de datos
STATUS  = 'db/Status/'              # Rutas stados
COMMA   = 'db/Command/'             # Rutas comandos
DISP    = '/home/pi/.ID/'           # Ruta Informacion Dispositivo
CONF    = 'db/Config/'               # Ruta Configuraciones
HILS    = 'db/Hilos/'               # Ruta Configuraciones

#---------------------------------
#           Datos del dispositivo
#---------------------------------

INF_DISPO       = DISP + 'Datos_Creacion.txt'
INF_FIRMWARE    = FIRM + 'README.md'
INF_VERCION     = FIRM + CONF + 'Vercion_Firmware.txt'
#INF_TOTAL_DISPO = FIRM + DATA + 'Inf_Dispotivo_Total.txt'


#---------------------------------
#           Rutas Base de datos
#---------------------------------

TAB_USER = FIRM + DATA + 'Tabla_Usuarios.txt'       # Usuarios del servidor o counter
TAB_ENVI = FIRM + DATA + 'Tabla_Enviar.txt'         # ? posible filtro para mejorar aun no utilizadosd
TAB_AUTO = FIRM + DATA + 'Tabla_Autorizados.txt'    # Registro de usuarios autorizados entrada y salida

#---------------------------------
#           Comandos
#---------------------------------

COM_LED         = FIRM + COMMA + 'Led/Com_Led.txt'
COM_BUZZER      = FIRM + COMMA + 'Buzzer/Com_Buzzer.txt'
COM_TECLADO     = FIRM + COMMA + 'Teclado/Com_Teclado.txt'
COM_FIRMWARE    = FIRM + COMMA + 'Firmware/Com_Firmware.txt'
COM_TX_RELE     = FIRM + COMMA + 'Rele/Com_Rele.txt'
COM_QR          = FIRM + COMMA + 'Qr/Com_Qr.txt'

#---------------------------------
#           Stados
#---------------------------------

STATUS_USER     = FIRM + STATUS + 'Usuario/Status_User.txt'
STATUS_TECLADO  = FIRM + STATUS + 'Teclado/Status_Teclado.txt'
STATUS_QR       = FIRM + STATUS + 'Qr/Status_Qr.txt'
STATUS_REPEAT_QR= FIRM + STATUS + 'Qr/Repeat_Qr.txt'
STATUS_RED      = FIRM + STATUS + 'Red/Status_Red.txt'

#---------------------------------
#           Configuraciones
#---------------------------------

CONF_TIEM_RELE = FIRM + CONF + 'Rele/Tiempo_Rele.txt'
CONF_DIREC_RELE = FIRM + CONF + 'Rele/Direccion_Rele.txt'

#---------------------------------
#           Manejo de Hilos
#---------------------------------

#-- peticion de usuarios
HILO_OUT_PETI_USERS = FIRM + HILS + 'M_Peticion_Users/Out_Peticion_Users.txt'
HILO_STATUS_PETI_USERS = FIRM + HILS + 'M_Peticion_Users/Status_Peticion_Users.txt'
#-- Procesar QR en el dispositivo
HILO_N_A_Exit_Dis_QR	    = FIRM + HILS + 'QR/Exit_Dispositivos_QR.txt'   #48
HILO_N_A_Status_Dis_QR	    = FIRM + HILS + 'QR/Status_Dispositivos_QR.txt' #49
HILO_N_A_Out_Dis_QR         = FIRM + HILS + 'QR/Out_Dispositivos_QR.txt'    #50


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

INF_DISPO = DISP + 'Datos_Creacion.txt'
INF_FIRMWARE = FIRM + 'README.md'
INF_VERCION = FIRM + CONF + 'Vercion_Firmware.txt'

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








#-------  informacion           ----------
N_A_ID_Lector       ='/home/pi/.ID/Datos_Creacion.txt'
#-------        Data     ----------
N_A_Servidor		= FIRM + DATA + 'Tabla_Servidor.txt'
N_A_Pines		    = FIRM + DATA + 'Tabla_Pines.txt'
N_A_Lector		    = FIRM + DATA + 'Tabla_Lector.txt'
N_A_Tabla_Enviar	= FIRM + DATA + 'Tabla_Enviar.txt'
N_A_Ordenada_Num	= FIRM + DATA + 'Tabla_Ordenada_Num.txt'
N_A_Ordenada_Crip	= FIRM + DATA + 'Tabla_Ordenada_Crip.txt'
#-------        Status     ----------
# Led
N_A_Estados_Led	        = FIRM + STATUS + 'Estado_Led.txt'
N_A__Led	            ='/home/pi/Firmware/db/Status/Led.txt'
# Teclado
N_A_Estados_Teclado     ='/home/pi/Firmware/db/Status/Estado_Teclado.txt'
N_A_Teclas_Led	        ='/home/pi/Firmware/db/Status/Teclas.txt'
# chicharrra
N_A_Estados_Chicharra   ='/home/pi/Firmware/db/Status/Estado_Chicharra.txt'
# QR
N_A_QR                  ='/home/pi/Firmware/db/Status/QR.txt'
N_A_Estados_QR          ='/home/pi/Firmware/db/Status/Estado_QR.txt'
N_A_Estados_Sensor      ='/home/pi/Firmware/db/Status/Estado_Sensor.txt'
N_A_Estados_QR_Repe     ='/home/pi/Firmware/db/Status/Estado_QR_Repetido.txt'
N_A_Estados_Servidor    ='/home/pi/Firmware/db/Status/Estado_Servidor.txt'
#-------        Log     ----------
N_A_QR_Numero_Lecturas  ='/home/pi/Firmware/db/Log/Numero_Lecturas_QR.txt'
N_A_Numero_Reinicios    ='/home/pi/Firmware/db/Log/Numero_Reinicios.txt'
#-------        Config     ----------
N_A_Direccion_Torniqute ='/home/pi/Firmware/db/Config/Direccion_Torniquete.txt'
N_A_Tiempo_Torniqute    ='/home/pi/Firmware/db/Config/Tiempo_Torniquete.txt'
N_A_Tx_Torniquete        ='/home/pi/Firmware/db/Config/TX_Torniquete.txt'
#-------        Servidor     ----------
N_A_Dominio_Servidor    ='/home/pi/Firmware/db/Config/link/Dominio_S.txt'
N_A_IP_Servidor         ='/home/pi/Firmware/db/Config/link/IP_Servidor.txt'
N_A_Dominio_BK          ='/home/pi/Firmware/db/Config/link/Dominio_BK.txt'
N_A_IP_BK               ='/home/pi/Firmware/db/Config/link/IP_BK.txt'
N_A_Dominio_Listado     ='/home/pi/Firmware/db/Config/link/Dominio_Listado.txt'
N_A_Mejor_Conexion      ='/home/pi/Firmware/db/Config/link/Mejor_Conexion.txt'
N_A_Vinculado           ='/home/pi/Firmware/db/Config/link/Vinculado.txt'
#-------        Actualizador     ----------
N_A_Procedimiento       ='/home/pi/Actualizador/db/Respuesta_Peticion_Firmware.txt'
N_A_Procesos            ='/home/pi/Firmware/auto/Procesos.txt'
N_A_Vercion_Firmware    ='/home/pi/Firmware/db/Config/Vercion_Firmware.txt'
N_A_Nommbre_Firmware    ='/home/pi/Firmware/README.md'
N_A_ProcesosBK          ='/home/pi/Firmware/auto/ProcesosBK.txt' # cambiar a la ruta del proceso de BK
N_A_Memoria_Actualizador='/home/pi/Actualizador/db/Memoria_Actualizador.txt'
N_A_Forzar_Firmware    ='/home/pi/Firmware/db/Status/Forzar_Firmware.txt'
N_A_Estado_Actualizador ='/home/pi/Actualizador/db/Estado_Actualizador.txt'
#-------        Comunicacion Dispostivos     ----------
N_A_Dispositivos        ='/home/pi/Firmware/db/Dispositivos/IP.txt'
N_A_Inf_Para_Dispos     ='/home/pi/Firmware/db/Dispositivos/Para_Dispostivos.txt'
N_A_Tx_Dispo            ='/home/pi/Firmware/db/Dispositivos/Tx_Dispo.txt'
N_A_Rx_Dispo            ='/home/pi/Firmware/db/Dispositivos/Rx_Dispo.txt'
#-------        Control de pines     ----------
N_A_Key                 ='/home/pi/.ID/Key.txt'
N_A_Pines_Usados        ='/home/pi/Firmware/db/Data/Tabla_Pines_Usados.txt'
#-------        Control web     ----------
N_A_Comandos            ='/home/pi/Firmware/db/Status/Comandos_Web.txt'
N_A_Wifi                ='/etc/wpa_supplicant/wpa_supplicant.conf'
N_A_IP_Static           ='/etc/dhcpcd.conf'
N_A_Con_Web             ='/var/www/html/Administracion/include/Control_Web.txt'
N_A_Procesos_web	    ='/home/pi/Firmware/db/Status/Procesos_web.txt'
N_A_Status_Ins_web	    ='/home/pi/Firmware/Web/Install/Status_Install.txt'
#-------        Hilos  QR   ----------
N_A_Exit_Dis_QR	        ='/home/pi/Firmware/db/Hilos/QR/Exit_Dispositivos_QR.txt'
N_A_Status_Dis_QR	    ='/home/pi/Firmware/db/Hilos/QR/Status_Dispositivos_QR.txt'
N_A_Out_Dis_QR          ='/home/pi/Firmware/db/Hilos/QR/Out_Dispositivos_QR.txt'
#-------        Hilos  QR   ----------
N_A_Exit_Pet_User	    ='/home/pi/Firmware/db/Hilos/M_Peticion_Users/Exit_Peticion_Users.txt'
N_A_Status_Pet_User	    ='/home/pi/Firmware/db/Hilos/M_Peticion_Users/Status_Peticion_Users.txt'
N_A_Out_Pet_User        ='/home/pi/Firmware/db/Hilos/M_Peticion_Users/Out_Peticion_Users.txt'


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#                                   FUNCIONES
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def Get_archivo(a):

    global N_A_Servidor
    global N_A_Lector
    global N_A_Tabla_Enviar
    global N_A_Estados_Led
    global N_A_Estados_Teclado
    global N_A_Teclas_Led
    global N_A_Estados_Chicharra
    global N_A_QR
    global N_A_Estados_QR
    global N_A_Estados_Sensor
    global N_A__Led
    global N_A_Estados_QR_Repe
    global N_A_QR_Numero_Lecturas
    global N_A_Direccion_Torniqute
    global N_A_Numero_Reinicios
    global N_A_Procedimiento
    global N_A_Procesos
    global N_A_Vercion_Firmware
    global N_A_ProcesosBK
    global N_A_Memoria_Actualizador
    global N_A_Estado_Actualizador
    global N_A_Dispositivos
    global N_A_Inf_Para_Dispos
    global N_A_Tx_Dispo
    global N_A_Rx_Dispo
    global N_A_Key
    global N_A_Pines
    global N_A_Pines_Usados
    global N_A_Estados_Servidor
    global N_A_Nommbre_Firmware
    global N_A_Tiempo_Torniqute

    global N_A_Dominio_Servidor
    global N_A_IP_Servidor
    global N_A_Dominio_BK
    global N_A_IP_BK
    global N_A_Dominio_Listado
    global N_A_Mejor_Conexion
    global N_A_Ordenada_Num
    global N_A_Ordenada_Crip
    global N_A_Tx_Torniquete
    global N_A_Forzar_Firmware
    global N_A_Vinculado
    global N_A_Comandos
    global N_A_Wifi
    global N_A_IP_Static
    global N_A_Con_Web
    global N_A_Procesos_web
    global N_A_Status_Ins_web
    global N_A_Exit_Dis_QR
    global N_A_Status_Dis_QR
    global N_A_Out_Dis_QR
    global N_A_ID_Lector
    global N_A_Exit_Pet_User
    global N_A_Status_Pet_User
    global N_A_Out_Pet_User

    arch = ''

    if a==0:	arch	=	N_A_Servidor
    if a==1:	arch	=	N_A_Lector
    if a==2:	arch	=	N_A_Tabla_Enviar
    if a==3:	arch	=	N_A_Estados_Led
    if a==4:	arch	=	N_A_Estados_Teclado
    if a==5:	arch	=	N_A_Teclas_Led
    if a==6:	arch	=	N_A_Estados_Chicharra
    if a==7:	arch	=	N_A_QR
    if a==8:	arch	=	N_A_Estados_QR
    if a==9:	arch	=	N_A_Estados_Sensor
    if a==10:	arch	=	N_A__Led
    if a==11:	arch	=	N_A_Estados_QR_Repe
    if a==12:	arch	=	N_A_QR_Numero_Lecturas
    if a==13:	arch	=	N_A_Direccion_Torniqute
    if a==14:	arch	=	N_A_Numero_Reinicios
    if a==15:	arch	=	N_A_Procedimiento
    if a==16:	arch	=	N_A_Procesos
    if a==17:	arch	=       N_A_Vercion_Firmware
    if a==18:	arch	=       N_A_ProcesosBK
    if a==19:	arch	=       N_A_Memoria_Actualizador
    if a==20:	arch	=       N_A_Estado_Actualizador
    if a==21:	arch	=       N_A_Dispositivos
    if a==22:	arch	=       N_A_Inf_Para_Dispos
    if a==23:	arch	=       N_A_Tx_Dispo
    if a==24:	arch	=       N_A_Rx_Dispo
    if a==25:	arch	=       N_A_Key
    if a==26:	arch	=       N_A_Pines
    if a==27:	arch	=       N_A_Pines_Usados
    if a==28:	arch	=       N_A_Estados_Servidor
    if a==29:	arch	=       N_A_Nommbre_Firmware
    if a==30:	arch	=       N_A_Tiempo_Torniqute

    if a==31:	arch	=       N_A_Dominio_Servidor
    if a==32:	arch	=       N_A_IP_Servidor
    if a==33:	arch	=       N_A_Dominio_BK
    if a==34:	arch	=       N_A_IP_BK
    if a==35:	arch	=       N_A_Dominio_Listado
    if a==36:	arch	=       N_A_Mejor_Conexion
    if a==37:	arch	=       N_A_Ordenada_Num
    if a==38:	arch	=       N_A_Tx_Torniquete
    if a==39:	arch	=       N_A_Ordenada_Crip
    if a==40:	arch	=       N_A_Forzar_Firmware
    if a==41:	arch	=       N_A_Vinculado
    if a==42:	arch	=       N_A_Comandos
    if a==43:	arch	=       N_A_Wifi
    if a==44:	arch	=       N_A_IP_Static
    if a==45:	arch	=       N_A_Con_Web
    if a==46:	arch	=       N_A_Procesos_web
    if a==47:	arch	=       N_A_Status_Ins_web
    if a==48:	arch	=       N_A_Exit_Dis_QR
    if a==49:	arch	=       N_A_Status_Dis_QR
    if a==50:	arch	=       N_A_Out_Dis_QR
    if a==51:	arch	=       N_A_ID_Lector
    if a==52:	arch	=       N_A_Exit_Pet_User
    if a==53:	arch	=       N_A_Status_Pet_User
    if a==54:	arch	=       N_A_Out_Pet_User

    return arch

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

# Get_archivo(a)

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------
#print Get_archivo(0)

#print TAB_USER

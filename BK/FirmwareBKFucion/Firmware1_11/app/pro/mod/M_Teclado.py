
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------

from lib.Lib_File           import *  # importar con los mismos nombres
from lib.Lib_Pygame         import *  # importar con los mismos nombres
from lib.Lib_Networks       import *  # importar con los mismos nombres
from M_Inf_Dispositivo      import *  # importar con los mismos nombres

#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------
#--- Para Menejo de teclas

#--- Para el display
Memoria = ""
Tamano = 11
Texto_Display= ""
Contador_Menu=0
operator= ""

#--- Para Evento de informaccion del dispositivo
Estado_Informacion      = 0
Estados_visualizacion   =0
Contador_Informacion    = 0
MAX_Constador_INF       = 80

#--- Para Evento de Forzar Firmware
Estado_Forzar_Firmware             = 0
Estado_visual_Forzar_Firmware      =0
Contador_Inf_Forzar_Firmware       = 0
MAX_Constador_INF_Forzar_Firmware  = 80

#--- Para Evento de red
Contador_Red        = 0
Estado_visual_Red   = 0
MAX_Constador_Red   = 80

#--- Para Evento del Usuario
Estado_Usuario = 0
Estado_visual_Usuario = 0

#--- Para Evento del QR repetido
Estado_QR = 0
Estado_visual_QR = 0
Contador_QR_Repetido=0
MAX_Contador_QR_Repetido=20



#-----------------------------------------------------------
#----      Funciones para el manejo del Teclado         ----
#-----------------------------------------------------------





# *****-----------------------------------------------------------
# ***** Evento de QR Estado_QR_Repetido
def Evento_Estado_QR_Repetido():
    global Estado_QR
    global Estado_visual_QR
    global Contador_QR_Repetido
    global MAX_Contador_QR_Repetido


    QR = Get_File(STATUS_REPEAT_QR)
    #print QR

    if '2' ==  QR : # or '3' ==  Usuario or '4' ==  Usuario:
        Estado_QR = QR
        Estado_visual_QR = 1
        Contador_QR_Repetido = Contador_QR_Repetido +1
        if Contador_QR_Repetido >= MAX_Contador_QR_Repetido:
            Contador_QR_Repetido=0
            Set_File(STATUS_REPEAT_QR, '0')
            Estado_visual_QR = 0

        return 1
    else:
        Estado_visual_QR = 0
        return -1


def Pintar_QR_Repetido():
    Pintar_Alerta()




































# *****-----------------------------------------------------------
# ***** Evento de estado del Usuario
def Evento_Estado_Usuario():
    global Estado_Usuario
    global Estado_visual_Usuario


    Usuario = Get_File(STATUS_USER)

    if '6' ==  Usuario or '3' ==  Usuario or '4' ==  Usuario:
        Estado_Usuario = Usuario
        Estado_visual_Usuario = 1
        return 1
    else:
        Estado_visual_Usuario = 0
        return -1


def Pintar_Estados_Usuario(Usuario):
    global Estado_visual_Usuario
    #print Usuario

    if   Usuario == '6': Pintar_Estado_Usuario('Denegar')
    elif Usuario == '3': Pintar_Estado_Usuario('Per_Derecha')
    elif Usuario == '4': Pintar_Estado_Usuario('Per_Izquierda')

    #Estado_visual_Usuario = 0



























# *****-----------------------------------------------------------
# ***** Evento de estado de la red
def Evento_Estado_Red():


    global Contador_Red
    global Estado_visual_Red
    global MAX_Constador_Red
    #print Estado_Informacion

    Contador_Red = Contador_Red + 1
    #print 'Esatdo Info:' +str(Contador_Informacion)
    # Avilitar visualizacion
    if Contador_Red == 1:
        Estado_visual_Red =1
        return 1
    # Desavilitar visualizacion
    if Contador_Red == int(MAX_Constador_Red/2):
        Estado_visual_Red =0
        return 1
    # contador de timepo de duracion visualizacion
    if Contador_Red >= MAX_Constador_Red:
        Contador_Red = 0
        return 1

    return -1



















# *****-----------------------------------------------------------
# ***** Evento de Forzar Firmware
def Evento_Forzar_Firmware():

    global Estado_Forzar_Firmware
    global Contador_Inf_Forzar_Firmware
    global Estado_visual_Forzar_Firmware
    global MAX_Constador_INF_Forzar_Firmware
    #print Estado_Informacion
    if Estado_Forzar_Firmware == 1:
        Contador_Inf_Forzar_Firmware = Contador_Inf_Forzar_Firmware + 1
        #print 'Esatdo Info:' +str(Contador_Informacion)
        # Avilitar visualizacion
        if Contador_Inf_Forzar_Firmware == 1:
            Set_File(COM_FIRMWARE, '1')   # cambiar estado para hacer la actualizacion de firmware
            Estado_visual_Forzar_Firmware =1
            return 1
        # Desavilitar visualizacion
        if Contador_Inf_Forzar_Firmware == MAX_Constador_INF_Forzar_Firmware-2:
            Estado_visual_Forzar_Firmware =0
            return 1
        # contador de timepo de duracion visualizacion
        if Contador_Inf_Forzar_Firmware >= MAX_Constador_INF_Forzar_Firmware:
            Contador_Inf_Forzar_Firmware = 0
            Estado_Forzar_Firmware =0
            return 1
    return -1





















# *****-----------------------------------------------------------
# ***** Evento de informacionde dispsotivo
def Inf_Dispositivo():
        return GET_Inf()

def Evento_Informacion_Dispositivo():

    global Estado_Informacion
    global Contador_Informacion
    global Estados_visualizacion
    global MAX_Constador_INF
    #print Estado_Informacion
    if Estado_Informacion == 1:
        Contador_Informacion = Contador_Informacion + 1
        #print 'Esatdo Info:' +str(Contador_Informacion)
        # Avilitar visualizacion
        if Contador_Informacion == 1:
            Estados_visualizacion =1
            return 1
        # Desavilitar visualizacion
        if Contador_Informacion == MAX_Constador_INF-2:
            Estados_visualizacion =0
            return 1
        # contador de timepo de duracion visualizacion
        if Contador_Informacion >= MAX_Constador_INF:
            Contador_Informacion = 0
            Estado_Informacion =0
            return 1
    return -1























# *****-----------------------------------------------------------
# *****Funciones para el Display y teclas

def motion(x,y):

    Ix=40
    Iy=75
    Disx=75+10
    Disy=75+10

    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*0)-10) and (y <= Iy+70+(Disy*0)) : return 1    #clickbut(1) #print "Tecla 1"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*0)-10) and (y <= Iy+70+(Disy*0)) : return 2    #clickbut(2) #print "Tecla 2"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*0)-10) and (y <= Iy+70+(Disy*0)) : return 3    #clickbut(3) #print "Tecla 3"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*1)) and (y <= Iy+70+(Disy*1)) :    return 4    #clickbut(4) #print "Tecla 4"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*1)) and (y <= Iy+70+(Disy*1)) :    return 5    #clickbut(5) #print "Tecla 5"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*1)) and (y <= Iy+70+(Disy*1)) :    return 6    #clickbut(6) #print "Tecla 6"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*2)) and (y <= Iy+70+(Disy*2)) :    return 7    #clickbut(7) #print "Tecla 7"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*2)) and (y <= Iy+70+(Disy*2)) :    return 8    #clickbut(8) #print "Tecla 8"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*2)) and (y <= Iy+70+(Disy*2)) :    return 9    #clickbut(9) #print "Tecla 9"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*3)) and (y <= Iy+70+(Disy*3)) :    return 14   #clrbut() #print "Tecla c"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*3)) and (y <= Iy+70+(Disy*3)) :    return 0    #clickbut(0) #print "Tecla 0"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*3)) and (y <= Iy+70+(Disy*3)) :    return 11   #clickbut(11) #print "Tecla k"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*4)) and (y <= Iy+70+(Disy*4)) :    return 12   #equlbut() #print "Tecla OK"

    return -1


def click_Tecla(number): # teclas de 0-9 y k
    global operator
    global Contador_Menu
    global Texto_Display
    global Memoria
    global Tamano
    global Estado_Informacion
    global Estado_Forzar_Firmware

    Set_File(COM_BUZZER, '1')      # activar sonido por 500*1
    if Contador_Menu == 3: # Numero de borrados
        if   number == 11: Estado_Forzar_Firmware  = 1 # Tecla 'K' print 'Forzar Actualizacion Firmware'
        elif number == 1 : Estado_Informacion      = 1 # Tecla '1' print 'ver informacion dispositivo'

    Contador_Menu=0

    if number == 11:    number = 'K'

    N_Teclas = len(operator)
    if N_Teclas > 0:
        operator=operator+str(number)
        Memoria = operator
    elif number != 0:
        operator=operator+str(number)
        Memoria = operator

    N_Teclas = len(operator)
    if N_Teclas >= Tamano: #print 'visualisar diferente'
        Memoria=Memoria[N_Teclas-Tamano:N_Teclas+1]

    Texto_Display = Memoria




def clrbut(): #para el boton c borrar

    global operator
    global Contador_Menu
    global Texto_Display
    global Memoria

    Set_File(COM_BUZZER, '1')      # activar sonido por 500*1
    trama = len(operator)
    if trama > 0:
        operator=operator[:trama-1]
        Memoria = operator
    else:
        operator=""
        Memoria = operator
        Contador_Menu+=1

    N_Teclas = len(operator)
    if N_Teclas >= Tamano: #print 'visualisar diferente'
        Memoria=Memoria[N_Teclas-Tamano:N_Teclas+1]

    Texto_Display = Memoria
    #print Contador_Menu
    if Contador_Menu == 5:  # numero de veces para activar El Menu de Configuracion
        Contador_Menu = 0
        pygame.quit()
        commands.getoutput('python /home/pi/Firmware/app/Menu_Config.py')
        sys.exit()

def equlbut():  #para el boton OK  #hacer un hilo para procesar los ruts
    global operator
    global Contador_Menu
    global Texto_Display
    global Memoria

    Set_File(COM_BUZZER, '1')           # activar sonido por 500*1
    Contador_Menu=0
    if len(operator) > 0:
        Set_File(COM_TECLADO, operator) # escrivir en archivo para procesar
        operator=""
        Memoria=""
        Texto_Display  = operator
        Set_File(STATUS_TECLADO, '1')       # Estado de teckas para enviar a servidor


def Evento_Teclado():

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:

            x,y = pygame.mouse.get_pos()

            Tecla = motion(x,y)
            if      Tecla == -1: return -1          # Ninguna tecla
            elif    Tecla == 14: clrbut()           #Tecla Borrar
            elif    Tecla == 12: equlbut()          #Tecla OK
            else               : click_Tecla(Tecla) #Tecla 0-9 y K

            return 1

    return -1





















# *****-----------------------------------------------------------
# *****Funciones Principales de Dibujar en pantalla
def Inicializacion():
    Inicializaciones_Graficas()
# *****------


def Dibujar():
    global Texto_Display
    global Estados_visualizacion
    global Estado_visual_Forzar_Firmware
    global Estado_visual_Red
    global Estado_visual_Usuario

    #Pintar_fondo(1) #fondo
    #Pintar_Display(Texto_Display) # display de numeros
    #Pintar_Estado_Usuario('Denegar') #'Denegar', 'Permitido' , 'Per_Derecha' 'Per_Izquierda'
    #Pintar_Estado_Red(0, 'sin_eth') # 'sin_eth' 'con_eth' 'sin_wif' 'con_wif'
    #Pintar_mensaje( 38, 70, Inf_Dispositivo()) #cuadro azul
    #Pintar_Display("Anderson") #
    #Pintar_Alerta() #avisos : El QR ya se proceso, retire su celular


    Pintar_fondo(1)
    Pintar_Display(Texto_Display)

    if Estados_visualizacion  == 1:         Pintar_mensaje( 38, 70, Inf_Dispositivo())
    if Estado_visual_Forzar_Firmware  == 1: Pintar_mensaje( 38, 70, "      Forzando\n Actualizacion\n     Firmware\n")
    if Estado_visual_Red  == 1:             Pintar_Status_Red(GET_STatus_Red())
    if Estado_visual_QR  == 1:              Pintar_QR_Repetido()
    if Estado_visual_Usuario   == 1:        Pintar_Estados_Usuario( Get_File(STATUS_USER))  #Leer_Estado(10))




    pygame.display.flip()



def Eventos():
    #------------------------------------------------
    #evento que muestar la informacion del dispsotivo
    #------------------------------------------------
    ET = -1
    EID = -1
    EFF = -1
    EER = -1
    EEU = -1
    EEQ = -1
    #------------------------------------------------
    EID = Evento_Informacion_Dispositivo()
    EFF = Evento_Forzar_Firmware()
    ET  = Evento_Teclado()
    EER = Evento_Estado_Red()
    EEU = Evento_Estado_Usuario()
    EEQ = Evento_Estado_QR_Repetido()
    #------------------------------------------------

    #print 'ET: ' + str(ET)
    #print 'EID: ' + str(EID)

    #------------------------------------------------
    if EID != -1 or ET != -1  or EFF != -1  or EER != -1  or EEU != -1 or EEQ != -1: return 1         # repintar
    else                     : return -1        # No pintar
    return -1


def Ciclo_Teclado():

    Inicializacion()
    Dibujar()
    print 'Comensando'
    while True:

        Tiempo_Espara_Proceso()
        Even = Eventos()
        if Even == 1:
            #print 'Evento:'
            Dibujar()
            Reset_Tiempo_proceso()
        else:
            Dormir_procesos()

    pygame.quit()



#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------


#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#if __name__ == "__main__":
#    main()
#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

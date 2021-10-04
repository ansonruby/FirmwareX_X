

import threading
import time

import lib.Control_Archivos
import lib.Control_Ethernet
import lib.Control_Fecha


Leer_Archivo            = lib.Control_Archivos.Leer_Archivo

Cambiar_LINK            = lib.Control_Ethernet.Cambiar_LINK
Estados_Internet        = lib.Control_Ethernet.Estados_Internet
Dominio_Valido          = lib.Control_Ethernet.Dominio_Valido
Agregar_Nuevo_Servidor  = lib.Control_Ethernet.Agregar_Nuevo_Servidor
Ver_Link                = lib.Control_Ethernet.Ver_Link

Tiempo                  = lib.Control_Fecha.T_Actual

#Res_Hay_Internet=1
Status_Hilo_activo_P_res =0
T_antes_RCS=0

RCS_Mensajes =0   # 0: NO print  1: Print

Tiempo_limite_desbloqueo=2  #En segundos



def Restablecer( Y_O_internet):  # intercambio_Hay_Internet
    global Status_Hilo_activo_P_res
    #print 'Estado Hilo:'+ str(Status_Hilo_activo_P_res)
    #print Status_Hilo_activo_P_res
    if Y_O_internet == 1 and Status_Hilo_activo_P_res == 0:
        Activar_Hilos_Restablecer()

    if Status_Hilo_activo_P_res == 1 and Y_O_internet == 1:
        #print 'diferencia de tiempo'
        T = Tiempo()
        # print T
        diferencia =  int( ( (int(T) -int(T_antes_RCS) ) /1000) /60)
        # print diferencia
        if diferencia >=Tiempo_limite_desbloqueo:  # 5
            # print 'bloqueo de hilo'
            Status_Hilo_activo_P_res = 0



def Proceso_Restablecer():

    global T_antes_RCS
    global RCS_Mensajes
    global Status_Hilo_activo_P_res

    #print 'no hay internet'
    T = Tiempo()
    # print T
    diferencia =  int( ( (int(T) -int(T_antes_RCS) ) /1000) /60)
    # print diferencia

    if diferencia >=1: #-------   Tiempo de intentos cada minuto
        T_antes_RCS=T
        #print 'intentar de nuevo'
        if RCS_Mensajes:
            print 'NO hay conecion con el servidor ?'
        Estado_Ethernet = Estados_Internet()
        if Estado_Ethernet.find("C") !=-1: #revicion wifi y ethernet
            if RCS_Mensajes:
                print 'Hay coneccion Local'
            Dominio_Prueba = (Leer_Archivo(31)).rstrip()
            if RCS_Mensajes:
                print 'Dominio actual:'+Dominio_Prueba
            IP_Dominio_Actual = Dominio_Valido(Dominio_Prueba)
            if IP_Dominio_Actual !=False:
                #-------------------------------------
                #-------- camvio la IP o la configuracion de acceso Test
                if RCS_Mensajes:
                    print 'Adquiere una IP :' + str(IP_Dominio_Actual)
                #-------------------------------------
                if Agregar_Nuevo_Servidor(Dominio_Prueba):
                    if RCS_Mensajes:
                        print 'actualizar link'
                    Cambiar_LINK() # activar cuando cambie los archivos
                    #Ping_Intento_Enviar_Usuarios_Autotizados() #enviar usuarios
                    #Hay_Internet = 0 #prueba de restablesimiento mejorar?
                else:
                    if RCS_Mensajes:
                        print 'Esperar otros errores en el dominio'
            else:
                #-------------------------------------
                #-------- Verificando cambio de dominio
                if RCS_Mensajes:
                    print 'Revizar lista de dominios'
                Nuevo_Dominio = List_Dom() #me devuleve una IP o dominio
                if RCS_Mensajes:
                    print Nuevo_Dominio
                if Nuevo_Dominio.find("Error") ==-1:
                    if RCS_Mensajes:
                        print 'para cambio o'
                    if Agregar_Nuevo_Servidor(Nuevo_Dominio):
                        Cambiar_LINK() # activar cuando cambie los archivos
                        #Ping_Intento_Enviar_Usuarios_Autotizados() #enviar usuarios
                        #Hay_Internet = 0 #prueba de restablesimiento mejorar?
                    else:
                        if RCS_Mensajes:
                            print 'Esperar otros errores'
                else:
                    #-------------------------------------
                    #No se puede hacer nada asta que el servidor se restabelsca
                    if RCS_Mensajes:
                        print 'Esperar restablecimiento del servidor'

        else:
            if RCS_Mensajes:
                print 'NO hay conecion local'

    Status_Hilo_activo_P_res = 0



#-----------------------------------------------------------
def Activar_Hilos_Restablecer():
    global P_Restablecer
    global Status_Hilo_activo_P_res
    if Status_Hilo_activo_P_res == 0:
        if P_Restablecer.isAlive() is False:

            if RCS_Mensajes:
                print 'Intentado restablaser'
            #print 'Punto Inicio, Intentado restablaser'
            P_Restablecer = threading.Thread(target=Proceso_Restablecer)#, args=(0,))
            P_Restablecer.start()
            Status_Hilo_activo_P_res = 1
            #print 'Activado'

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
P_Restablecer   = threading.Thread(target=Proceso_Restablecer)#, args=(0,))

"""
print 'while'
while 1:

    time.sleep(0.05)
    #print 'revicion restableser'
    Restablecer(1)
"""

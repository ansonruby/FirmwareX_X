

import time
import datetime
import threading

import lib.Control_Fecha
import lib.Control_Archivos
import lib.Control_Ethernet

Tiempo                  = lib.Control_Fecha.T_Actual
Hora                    = lib.Control_Fecha.Hora_Actual
#Time_add               = lib.Control_Fecha.Time_add
Time_add_hora           = lib.Control_Fecha.Time_add_hora
Time_add_seg            = lib.Control_Fecha.Time_add_seg


Leer                    = lib.Control_Archivos.Leer

Envio                   = lib.Control_Ethernet.envio



PP_Mensajes = 1


N_Intentos = 0
T_Ventana = 30          # expresado en segundos
Intentos = 5            # veces antes de activar la ventana
T_min_Intentos = 10     # expresado en segundos

def Enviar_usuarios_Autorizados_Sin_Internet():

    Ev = Leer()
    print len(Ev)

    if len(Ev) !=0 :
        Ev = Ev.replace('\n','","')
        Ev = '{"in_out":["'+Ev+'"]}'
        Ev = Ev.replace('",""]}','"]}')
        Ev = Ev.replace(',""','')
        if PP_Mensajes:
            print Ev
        T_A = Tiempo()
        ta=Envio(Ev,T_A,3)

        if ta.find("Error") == -1:
            print ta
            """
            Borrar(2) 		        # vaciar usarios enviados
            s = ta
            s= Filtro_Caracteres (s)
            if len(s) != 0:
                Escrivir_nuevo(1,s)     #al que pensar si los coloco en lectura como nuevo o no
                if PP_Mensajes:
                    print s           #que hacer con los que se quedarono
                return 1                #se iso la entrega y se guardo los usuarios
            """
        else:
            if PP_Mensajes:
                print 'No se puedo enviar los usuarios'		#programs una nueva entrega
            return -1

    else:
        if PP_Mensajes:
            print 'No hay nada para enviar'					# curso normal
        return 1    #  No hay nada para enviar

    return 1        #  No hay nada para enviar



def Proceso_envio_Usuarios():

    global Tiempo_activacion
    global T_Ventana
    global N_Intentos
    global Intentos

    T_Actual = time.time()


    if T_Actual >= Tiempo_activacion:


        Status = Enviar_usuarios_Autorizados_Sin_Internet()

        print ('N Status:', Status)

        if Status == 1:
            N_Intentos = 0
            Tiempo_activacion = Time_add_seg(T_Ventana)             # Tiempo de ventana normal
            if PP_Mensajes:
                print 'Tiempo de ventana normal'
        elif Status == -1:
            N_Intentos = N_Intentos + 1
            if N_Intentos >= Intentos:
                N_Intentos = 0
                Tiempo_activacion = Time_add_seg(T_Ventana)             # Tiempo de ventana normal
                if PP_Mensajes:
                    print 'Tiempo de ventana normal fin reintentos'
            else:
                Tiempo_activacion = Time_add_seg(T_min_Intentos)    # Tiempo de reintentos
                if PP_Mensajes:
                    print('N intentos:', N_Intentos)
                    print 'Tiempo por reintentos'


        if PP_Mensajes:
            print('Tiempo Para Otro :', time.ctime(Tiempo_activacion))









"""
Tiempo_activacion = Time_add_seg(T_Ventana)
print('Timepo activacion :', time.ctime(Tiempo_activacion))


while 1:

    time.sleep(1.05)

    Proceso_envio_Usuarios()

"""

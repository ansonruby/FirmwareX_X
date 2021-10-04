# -*- coding: utf-8 -*-
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
#import time
from lib.Lib_Time import *  # importar con los mismos nombres
from lib.Lib_File import *  # importar con los mismos nombres
from lib.Lib_Requests import *  # importar con los mismos nombres
from M_Inf_Dispositivo import *  # importar con los mismos nombres


import threading
#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------
E_H_Get_Users_serv = 0 #estada para que se actualise por hora

#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------

#-----------------------------------------------------------
#----      Funciones para el manejo de usuarios   ----
#-----------------------------------------------------------
def Filtro_Caracteres(s):       # eliminar los caracteres y estructura Jason
    s = s.replace('"',"")
    s = s.replace('[',"")
    s = s.replace('{',"")
    s = s.replace(']',"")
    s = s.replace('}',"")
    s = s.replace('data:',"")
    s = s.replace(',',"\r\n")
    return s
#-----------------------------------------------------------
def Get_Usuarios_Server():#peticion de usuarios al servidor y guardado en un archivo
    global ID_Disp
    global URL_Servidor

    T_A = T_Actual()            # Tiempo()
    #print 'Inicio'
    Us_acti=  Pedir_Usuarios_Activos(URL_Servidor,T_A, ID_Disp) # U_Activos
    #T2 = T_Actual()             # Tiempo()
    #print 'Fin'
    #print 'T: ' + str(int(T2)-int(T_A))

    if Us_acti.find("Error") == -1:
        s = Us_acti
        s= Filtro_Caracteres (s)
        Set_File(TAB_USER,s)                      #guardar usuarios
        Set_File(HILO_OUT_PETI_USERS,'OK')      #Status finalizacion hilo
        #print 'Get user OK'
        return 1

    Set_File(HILO_OUT_PETI_USERS,Us_acti)       #Status finalizacion hilo
    #print 'Get user Error'
    return -1

#-----------------------------------------------------------
def Activar_Hilos_Get_User():
    global GET_User_Server

    if GET_User_Server.isAlive() is False:
        GET_User_Server = threading.Thread(target=Get_Usuarios_Server)#, args=(0,))
        GET_User_Server.start()

#-----------------------------------------------------------
def Evento_por_hora_Usuarios_Server():
    global H_Get_Users_serv
    global E_H_Get_Users_serv

    if Hora_Actual() == H_Get_Users_serv:

        if E_H_Get_Users_serv == 0:
            E_H_Get_Users_serv = 1
            #print 'Get_User por hora'
            #Get_Usuarios_Server()
            Activar_Hilos_Get_User()
    else:
        E_H_Get_Users_serv = 0

#-----------------------------------------------------------
def Evento_por_Estado_Usuarios_Server():

    if Get_File(HILO_STATUS_PETI_USERS) == '1': #Star de Hilos Usuarios_Server
            #print 'Get_User por sistema'
            Activar_Hilos_Get_User()
            Clear_File(HILO_STATUS_PETI_USERS)

#-----------------------------------------------------------
def Eventos_Usuarios_Server():#peticion de usuarios al servidor
    Evento_por_hora_Usuarios_Server()  # solo una hora en espesifico se puede mejorar a un siclo de peticiones
    Evento_por_Estado_Usuarios_Server()

#-----------------------------------------------------------

    #hora especifica #"12:10 AM"
    #peticion del sofwate por algun evento

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
GET_User_Server   = threading.Thread(target=Get_Usuarios_Server)#, args=(0,))

#H_S_QR  = threading.Thread(target=P_Servidor_QR)#,  args=(0,))


#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------


#print 'hola agregando datos'
#while (True):
#    time.sleep(0.05)
#    Eventos_Usuarios_Server()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

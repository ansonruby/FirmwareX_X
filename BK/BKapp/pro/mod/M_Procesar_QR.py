# -*- coding: utf-8 -*-
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import threading

from lib.Lib_Time import *  # importar con los mismos nombres
from lib.Lib_Requests import *  # importar con los mismos nombres
from M_Inf_Dispositivo import *  # importar con los mismos nombres
from M_Rele import *  # importar con los mismos nombres


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
#----      Funciones para el manejo del buzzer     ----
#-----------------------------------------------------------

def Proceso_Led_Estado_4():
    Tiempo_Torniquete =int(Get_File(CONF_TIEM_RELE))
    Set_File(STATUS_USER,'4') #para la pantalla
    Set_File(COM_LED,'4') #para leD
    time.sleep(Tiempo_Torniquete)
    Set_File(COM_LED,'0')
    Set_File(STATUS_USER,'0') #para la pantalla

def Proceso_Led_Estado_3():
    Tiempo_Torniquete =int(Get_File(CONF_TIEM_RELE))
    Set_File(STATUS_USER,'3') #para la pantalla
    Set_File(COM_LED,'3')
    time.sleep(Tiempo_Torniquete)
    Set_File(COM_LED,'0')
    Set_File(STATUS_USER,'0') #para la pantalla

def Proceso_Led_Estado_6():
    Tiempo_Torniquete =int(Get_File(CONF_TIEM_RELE))
    Set_File(STATUS_USER,'6') #para la pantalla
    Set_File(COM_LED,'6')
    time.sleep(Tiempo_Torniquete)
    Set_File(COM_LED,'0')
    Set_File(STATUS_USER,'0') #para la pantalla


def Direcion_Led(Res):

    global H_E3_LED
    global H_E4_LED
    global H_E6_LED

    Direc = Get_File(CONF_DIREC_RELE)  # Direccion_Torniquete
    if Res == 'Access granted-E':
        if Direc == 'D':
            #Escrivir_Archivos(3,'4')
            if H_E4_LED.isAlive() is False:
                H_E4_LED   = threading.Thread(target=Proceso_Led_Estado_4)
                H_E4_LED.start()
        else :
            #Escrivir_Archivos(3,'3')
            if H_E3_LED.isAlive() is False:
                H_E3_LED   = threading.Thread(target=Proceso_Led_Estado_3)
                H_E3_LED.start()
    elif Res == 'Access granted-S':
        if Direc == 'D':
            #Escrivir_Archivos(3,'3')
            if H_E3_LED.isAlive() is False:
                H_E3_LED   = threading.Thread(target=Proceso_Led_Estado_3)
                H_E3_LED.start()
        else :
            #Escrivir_Archivos(3,'4')
            if H_E4_LED.isAlive() is False:
                H_E4_LED   = threading.Thread(target=Proceso_Led_Estado_4)
                H_E4_LED.start()
    else :
        #Escrivir_Archivos(3,'6')
        if H_E6_LED.isAlive() is False:
            H_E6_LED   = threading.Thread(target=Proceso_Led_Estado_6)
            H_E6_LED.start()



def Decision_Torniquete (Res, QR, ID2, Ti,Qr_Te, I_N_S ):

    #global Estados
    #Direc_Torniquete = Leer_Archivo(13)  # Direccion_Torniquete
    Co = QR+'.'             #QR
    Res=Res.rstrip('\n')    #limpiar respuesta
    Res=Res.rstrip('\r')

    Direcion_Led(Res)       #procesos en hilo LED
    Direcion_Rele(Res)      #Activacion de relevos en  Hilo?

    #guardar deciones de Entrada y Salida
    if Res == 'Access granted-E':
        print Co+Ti+'.'+Qr_Te+'.0.'+I_N_S
        Add_Line_End(TAB_AUTO, Co+Ti+'.'+Qr_Te+'.0.'+I_N_S+'\n')
    elif Res == 'Access granted-S':
        print Co+Ti+'.'+Qr_Te+'.1.'+I_N_S
        Add_Line_End(TAB_AUTO,Co+Ti+'.'+Qr_Te+'.1.'+I_N_S+'\n')
    else :
        print "Sin Acceso o rut equivocado estado 5 0 6"
    #Escrivir(Co+Ti+'.'+Qr_Te+'.0.'+I_N_S)               #guardar un registro
    #Escrivir_Archivo(Co+Ti+'.'+Qr_Te+'.0.'+I_N_S, 22)   #Para dispotivos asociados

#-----------------------------------------------------------
def Get_QR():
    Pal=Get_File(COM_QR)
    Pal=Pal.rstrip('\n')
    Pal=Pal.rstrip('\r')
    return Pal

#-----------------------------------------------------------
def P_Servidor_QR():            # Hilo principal
    global ID_Disp
    global URL_Servidor
    T_A = T_Actual()
    QRT = Get_QR()
    R_Q = (QRT).split('.')
    QR = R_Q[0]
    #print QR
    Respuesta = Enviar_QR(URL_Servidor, T_A, ID_Disp, QR)
    print 'RS: ' + Respuesta #+ ', T: ' + str(int(T2)-int(T_A))
    Set_File(HILO_N_A_Exit_Dis_QR,'1')
    #return Respuesta
    print 'Decision_Torniquete'
    Decision_Torniquete (Respuesta, QRT, "", T_A, '1','0')  #Respuesta_Con_Internet

#-----------------------------------------------------------
def P_Dispositivo_QR():

    Set_File(HILO_N_A_Exit_Dis_QR,'0')
    Set_File(HILO_N_A_Status_Dis_QR, '1')

    R_Q = (Get_QR()).split('.')
    QR = R_Q[0]
    IDQ = R_Q[1]

    Respuesta = 'Denegado'
    N_veri = 0

    if Get_File(HILO_N_A_Exit_Dis_QR) != '1':

        ID_1 = Verificar_ID(IDQ)
        if ID_1 != -1:
            N_veri = Verificar_acceso(ID_1) #revizar en donde swe dejan los usuarios

        if Get_File(HILO_N_A_Exit_Dis_QR) != '1':

            if N_veri != 0:
                if N_veri % 2 == 0	:	N_veri = 1 # Entrar
                else				:	N_veri = 2 # Salir

            if ID_1 == -1 and  N_veri == 0:					Respuesta =  'Denegado'		 #print 'NO existe'
            if ID_1 != -1 and  N_veri == 0 or N_veri == 1:	Respuesta =  'Access granted-E'#print 'Entrada'
            if ID_1 != -1 and  N_veri == 2:					Respuesta =  'Access granted-S'#print 'Salida'

            print 'RD: ' + Respuesta
            Set_File(HILO_N_A_Out_Dis_QR,Respuesta)
            Set_File(HILO_N_A_Status_Dis_QR, '2')

        else:
            #print 'Terminar Hilo'
            print 'RD: ' + Respuesta
            Set_File(HILO_N_A_Out_Dis_QR,Respuesta)
            Set_File(HILO_N_A_Status_Dis_QR, '3')
    else:
        #print 'Terminar Hilo'
        print 'RD: ' + Respuesta
        Set_File(HILO_N_A_Out_Dis_QR,Respuesta)
        Set_File(HILO_N_A_Status_Dis_QR, '3')

#-----------------------------------------------------------
def Activar_Hilos_Procesar_QR():
    global H_D_QR
    global H_S_QR

    if H_D_QR.isAlive() is False:
        H_D_QR = threading.Thread(target=P_Dispositivo_QR)#, args=(0,))
        H_D_QR.start()
    if H_S_QR.isAlive() is False:
        H_S_QR  = threading.Thread(target=P_Servidor_QR)#, args=(0,))
        H_S_QR.start()

#-----------------------------------------------------------
def Procesar_QR():
    if Get_File(STATUS_QR) == '1':   # Hay un QR sin procesar
        print '------ QR ---- '
        Activar_Hilos_Procesar_QR()
        Clear_File(STATUS_QR)        #final del procesos

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
H_D_QR   = threading.Thread(target=P_Dispositivo_QR)#, args=(0,))
H_S_QR  = threading.Thread(target=P_Servidor_QR)#,  args=(0,))

H_E4_LED   = threading.Thread(target=Proceso_Led_Estado_4)#, args=(0,))
H_E3_LED  = threading.Thread(target=Proceso_Led_Estado_3)#,  args=(0,))
H_E6_LED  = threading.Thread(target=Proceso_Led_Estado_6)#,  args=(0,))

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#while (True):
#    time.sleep(0.05)
#    Procesar_QR()


#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

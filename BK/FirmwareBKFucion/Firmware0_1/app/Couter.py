
import lib.Control_Archivos  as Ca
#import lib.Control_Ethernet  as Ce

import commands
import socket
import fcntl
import struct
import time
import requests


#----------------------------------------------
#                   definiciones
#----------------------------------------------

Escrivir_Estados        = Ca.Escrivir_Estados
Generar		            = Ca.Generar_ID_Tarjeta
Escrivir_Archivo        = Ca.Escrivir_Archivo
Leer_Archivo            = Ca.Leer_Archivo
Leer_Lineas             = Ca.Leer_Lineas
Borrar                  = Ca.Borrar_Archivo
Link_servidor           = Ca.Mejor_Opcion_link
Escrivir_nuevo          = Ca.Escrivir_nuevo
Verificar_ID            = Ca.Verificar_ID

#Get_Post_try_catch     =Ce.Get_Post_try_catch   #(peticion, CE_url, CE_datos, CE_cabeceras, tout):


"""
g2yt1.6ebe76c9fb411be97b3b0d48b791a7c9
gqyt3.3c7849bc28d281f187156af8ec4c882b
g2zdk.9a97ba14cb334d71cceffc84244f5d9c
"""


def add_user_counter(usuario):
    s = usuario.partition(".")
    ID =s[0]
    #print IDPrueba
    #ID='12dsad'
    Respuesta = Verificar_ID(ID)
    #print Respuesta
    if Respuesta == -1:
        Comando = usuario.strip('\n')
        Escrivir_Archivo(Comando,0)
        #print 'Usuario agregado'
    #else:
    #    print 'ya existe'


def Resolver_Comando_Counter():

    global Comando_Antes
    Comando = Leer_Archivo(48)
    if len(Comando) >= 1 :
        Usuarios = Comando.split("\n")
        for linea in Usuarios:
            s=linea.rstrip('\n')
            if len(s) > 0:
                add_user_counter(s)

    Borrar(48)




"""
def Nuevos_Usuarios_conter():
    IP_conter = Leer_Archivo(49)
    IP_conter = IP_conter.replace('',"\n")
"""
#payload = {'Dato': 'g2yt1asd12343.6ebe76c9fb411be97b3b0d48b791a7c9'}
#print Get_Post_try_catch('GET_PARAM', 'http://192.168.0.14/Prueba/new_user.php', payload, '', 2)

"""
dat = '"g2yt1asd12343.6ebe76c9fb411be97b3b0d48b791a7c9","g2yt1asd123435.6ebe76c9fb411be97b3b0d48b791a7c9"'
#dat = '"g2yt1asd12343.6ebe76c9fb411be97b3b0d48b791a7c9","g2yt1asd123435.6ebe76c9fb411be97b3b0d48b791a7c9' # con error
CE_datos ='{"data":['+dat+']}'

r = requests.post('http://192.168.0.14/api/new_user/index.php', data=CE_datos, headers='', timeout=2)

print r
print 'Texto: ' + r.text

time.sleep(1.05)
"""
#print 'listo'
#Resolver_Comando_Counter()

#print Get_Post_try_catch('POST', 'http://192.168.0.14/Prueba/new_user.php', CE_datos, '', 2)
#print Get_Post_try_catch('POST', 'http://192.168.0.14/api/counter/new_user/index.php', CE_datos, '', 2)



#while 1:

    #---------------------------------------------------------
    #  Proceso 0: Tiempo de espera para disminuir proceso
    #---------------------------------------------------------
    #time.sleep(1.05)
    #Resolver_Comando_Counter()

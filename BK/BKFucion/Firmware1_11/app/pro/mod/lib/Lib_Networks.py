
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
#---pendientes no se utilizan
import socket
import urllib2
import os
import commands
import requests
import time


#-------------------------------------------------------
#                                   CONTANTES
#-------------------------------------------------------

CE_V = 1          # 0: servidor de prueba 1: las direciones del aplicativo
P_Mensajes=0     # 0: NO print  1: Print


#-------------------------------------------------------
#----      Funciones para peticiones al servidor     ----
#-------------------------------------------------------
def Estatus_Coneccion (c):
        res2 = commands.getoutput('cat /sys/class/net/'+c+'/carrier')
        if res2 == '0':     return 0 #  print 'Desconectado'
        else:               return 1 # print 'Conectado'

#-----------------------------------------------------------
def GET_STatus_Red():
        Sres = ""
        Cantidad =0
        res = commands.getoutput('ls /sys/class/net/')
        redes =res.split("\n")

        for x1 in range(len(redes)):
                c= redes[x1]
                #print c
                if c.find('eth') != -1: #print 'ethernet'
                        if Estatus_Coneccion (c) == 0:  #print 'ED'
                            Sres = Sres + 'ED'
                            Cantidad+=1
                        else:                           #print 'EC'
                            Sres = Sres + 'EC'
                            Cantidad+=1
                if c.find('wlan') != -1: #print 'Wifi'

                        if Estatus_Coneccion (c) == 0:  #print 'WD'
                                Sres = Sres + 'WD'
                                Cantidad+=1
                        else:                           #print 'WC'
                                Sres = Sres + 'WC'
                                Cantidad+=1
        #print str(Cantidad) + Sres
        return  str(Cantidad) + Sres

#-----------------------------------------------------------
def Status_Redes():
	Estado_redes = GET_STatus_Red()
	if Estado_redes.find('C') != -1: 	return 1 #print 'hay red lan'
	else : 								return 0 #print 'No LAN'
    
#-----------------------------------------------------------


#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------


#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

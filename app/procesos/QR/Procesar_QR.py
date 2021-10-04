
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import os
import time

#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------
# Rutas para el control y comandos del sonido
FIRM            = '/home/pi/Firmware/'                      # Ruta Firmware
COMMA           = 'db/Command/'                             # Rutas comandos
COM_RX          = FIRM + COMMA + 'Serial/Com_Rx.txt'        # Archivo de comandos
COM_TX          = FIRM + COMMA + 'Serial/Com_Tx.txt'        # Archivo de comandos

#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------

GF=''
GI=''
M_QR=''             # depronto se nesesite una memoria de lista de dos pociciones para procesar despues o revizar
Antes_QR=''         # QR anterior


#-----------------------------------------------------------
#-----------------------------------------------------------
#----      Funciones para de uso general               ----
#-----------------------------------------------------------
#-----------------------------------------------------------

#-------------------------------------------------------
#----      Funciones para el manejo de archivos     ----
#-------------------------------------------------------
def Clear_File(arch):                                       # Borrar un archivo y revicion si existe
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write("")
        archivo.close()

#-------------------------------------------------------
def Get_File(arch):                                         # Leer un archivo y revicion si existe
    mensaje = ""
    if os.path.exists(arch):
        f = open (arch,'r')
        mensaje = f.read()
        #print(mensaje)
        f.close()
        return mensaje
    else:
        return mensaje                                      # ? es necesario colocar una vandera si no esta?

#-------------------------------------------------------
def Add_Line_End(arch, Dato): #incluir el/n
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        #print lineas
        f2 =open(arch, "w")
        f2.write(''.join(lineas) )
        f2.write(Dato)
        f2.close()


#-----------------------------------------------------------
#----      Funciones para el manejo del  QR             ----
#-----------------------------------------------------------
def Armado_de_QR_Valido(Tramas):
    global GF, GI, M_QR, Antes_QR

    Bandera = 0
    B_Nuevo = 0
    B_Igual = 0

    #print Tramas

    Tramas = Tramas.split('\n')
    for Trama in Tramas:
        #print 'tramas'
        Cantidad = len(Trama)
        if Cantidad > 0:
            Bandera, M_Trama =Trama_Analizar(Trama)
            #print 'B: ' + str(Bandera) + ', M:' + str(M_Trama)

            if Bandera == 1:
                if Antes_QR != M_Trama :
                    B_Nuevo = 1
                    M_QR = M_Trama
                    Antes_QR = M_Trama
                    #print 'nuevo saliar guardar qr '
                    #print 'Nuevo'
                    #return 1, M_QR #salida rapida por qr nuevo y valido
                else:
                    B_Igual = 1
                    #print 'Igual'
                    #return 3, M_QR

    #print 'fin tramas'
    if B_Nuevo == 1:    return 1, M_QR
    if B_Igual == 1:    return 3, M_QR

    if Bandera != -1:   return Bandera, M_QR
    else:               return Bandera, ""


#-----------------------------------------------------------
def Trama_Analizar(Trama):
    global GF, GI , M_QR
    Inicio = Trama.find("<")
    Fin = Trama.find(">")
    Bandera = 0

    if (Inicio != -1 ) and (Fin != -1):
        M_QR = Trama[(Inicio+1):(Fin)]
        GF =''
        GI =''
        Bandera = 1                         #
        #print "QR_F : " + M_QR
    elif (Inicio != -1 ) and (Fin == -1):
        GI = Trama[(Inicio+1):]
        Bandera = -1                        #print "Guardar Inicio: " + GI
    elif (Inicio == -1 ) and (Fin != -1):
        GF = Trama[0:(Fin)]           #print "Guardar Fin: " + GF
        M_QR = GI + GF
        GF =''
        GI =''
        Bandera = 1                         #
        #print "QR_F T: " + M_QR
    elif (Inicio == -1 ) and (Fin == -1):
        if Trama.find("Igual") != -1:
            Bandera = 3                 #
            GF =''
            GI =''
            #print "QR_F Igual: " + M_QR
        else:
            M_QR = Trama
            Bandera = 2                     #
            #print "X    : " + M_QR

    if Bandera != -1:   return Bandera, M_QR
    else:               return Bandera, ""

#-----------------------------------------------------------

#-----------------------------------------------------------

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#-----------------------------------------------------------
def Procesar_qr(Tramas):
    global COM_RX
    if len(Tramas)>=1:
        #print Tramas
        Clear_File(COM_RX)
        Bandera, QR =Armado_de_QR_Valido(Tramas)
        if Bandera != -1:
            if Bandera == 1:
                print 'Nuevo B: ' + str(Bandera) + ', QR: ' + QR
            if Bandera == 3:
                print 'Repet B: ' + str(Bandera) + ', QR: ' + QR
            if Bandera == 2:
                print 'NO ID B: ' + str(Bandera) + ', QR: ' + QR
        #print Bandera

print 'listos'

while True:
    time.sleep(0.05)
    Procesar_qr(Get_File(COM_RX))


Procesar_qr(Get_File(COM_RX))

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

# print len(Tramas) 	cat /var/log/apache2/other_vhosts_access.log  cat /var/log/apache2/other_vhosts_access.log | grep 403
# cut -d' ' -f1 access.log | sort | uniq
# cat /var/log/apache2/other_vhosts_access.log| awk '{print($1)}'|sort |uniq -c |sort -n



#-----------------------------------------------------------
"""
def Recibir_Cadenas(RX_Serial):

    Numero_Caracteres = len(RX_Serial)
    if Numero_Caracteres >= 1:
        status, QR = Armado_de_QR_Valido(RX_Serial)
        #print str(status) +': '+ QR
        if status == 1: # Nuevo QR para Procesar ------------------------
            if PP_MensajesQR == 1:
                print 'N_QR: '+ QR #print "Nuevo QR fusepong"
            Clear_File(COM_QR)              # Borrar QR
            Set_File(COM_QR, QR)            # Guardar QR
            Set_File(STATUS_QR, '1')        # Cambiar estado del QR
            Set_File(STATUS_REPEAT_QR, '0') # Estado QR repetido
        if status == 3: # QR ya leido -----------------------------------
            if PP_MensajesQR == 1:
                print 'L_QR: '+ QR #print "QR Igual"
            #Escrivir_Archivos('2',11)        # Estado QR repetido
            if QR.count(".") == 3:            # para procesar QR invitado
                Set_File(STATUS_QR, '1')      # Cambiar estado del QR
            else:
                Set_File(STATUS_REPEAT_QR, '2')     # Estado QR repetido
        if status == 2: # QR NO valido -------------------------
            if PP_MensajesQR == 1:
                print 'X   : '+ QR #print "NO es un QR"
            Clear_File(COM_QR)            # Borrar QR
            Set_File(COM_QR, QR)          # Guardar QR
            Set_File(STATUS_QR, '1')      # Cambiar estado del QR
"""

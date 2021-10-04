
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------

#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------


GF=''
GI=''
M_QR=''  #depronto se nesesite una memoria de lista de dos pociciones para procesar despues o revizar
Antes_QR=''
#-----------------------------------------------------------
#----      Funciones para el manejo del sensor QR     ----
#-----------------------------------------------------------
def Convertir_listado( RX_Serial):
    return RX_Serial.split('\r')

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
            Bandera = 3                     #
            #print "QR_F Igual: " + M_QR
        else:
            M_QR = Trama
            Bandera = 2                     #
            #print "X    : " + M_QR

    if Bandera != -1:   return Bandera, M_QR
    else:               return Bandera, ""

#-----------------------------------------------------------
def Armado_de_QR_Valido(RX_Serial):
    global GF, GI, M_QR, Antes_QR

    Bandera = 0
    B_Nuevo = 0
    B_Igual = 0
    #print '---------------------'
    #print "Rx : " + RX_Serial
    #print '---------------------'
    Tramas = RX_Serial.split('\r')
    for Trama in Tramas:
        Cantidad = len(Trama)
        if Cantidad > 0:
            Bandera, M_Trama =Trama_Analizar(Trama)

            if Bandera == 1:
                if Antes_QR != M_Trama :
                    B_Nuevo = 1
                    M_QR = M_Trama
                    Antes_QR = M_Trama
                else: B_Igual = 1

    if B_Nuevo == 1:    return 1, M_QR
    if B_Igual == 1:    return 3, M_QR

    if Bandera != -1:   return Bandera, M_QR
    else:               return Bandera, ""


#-----------------------------------------------------------
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

#-----------------------------------------------------------

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

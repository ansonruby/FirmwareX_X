
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import os
from Cns_Rout import *  # importar con los mismos nombres
#-------------------------------------------------------
#----      Funciones para el manejo de archivos     ----
#-------------------------------------------------------

def Clear_File(arch):
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write("")
        archivo.close()

#-------------------------------------------------------
def Get_File(arch):
    mensaje = ""
    if os.path.exists(arch):
        f = open (arch,'r')
        mensaje = f.read()
        #print(mensaje)
        f.close()
        return mensaje
    else:
        return mensaje

#-------------------------------------------------------
def Set_File(arch, Text):
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write(Text)
        archivo.close()

#-------------------------------------------------------
def Add_File(arch, Text):
    if os.path.exists(arch):
        archivo = open(arch, "a")
        archivo.write(Text)
        archivo.close()

#-------------------------------------------------------
def Get_Line(arch, Numero):
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        return lineas[Numero-1] # revisar si comensar en 1 o 0
    else:
        return ""

#-------------------------------------------------------
def Clear_Line(arch, Numero):
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        lineas.pop(Numero-1)
        #print lineas
        f2 =open(arch, "w")
        f2.write(''.join(lineas) )
        f2.close()

#-------------------------------------------------------
def Update_Line(arch, Numero, Dato): #incluir el/n
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        lineas[Numero-1]= Dato
        #print lineas
        f2 =open(arch, "w")
        f2.write(''.join(lineas) )
        f2.close()

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
#-------------------------------------------------------
def Add_Line_Pos(arch, Numero, Dato): #incluir el/n
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        inicio = lineas[0:(Numero-1)]
        fin = lineas[(Numero-1):]

        f2 =open(arch, "w")
        f2.write(''.join(inicio) )
        f2.write(Dato)
        f2.write(''.join(fin) )
        f2.close()
#-------------------------------------------------------
def Num_lines(arch):
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        return len(lineas)
    else:
        return -1







#-------------------------------------------------------
def Verificar_ID(Pal): #mejorar por que podia pasa cualquiera en menos tiempo con 40.000 usuarios demora 3 a 4 segundos en autorizar

    archivo = open(TAB_USER, 'r')
    archivo.seek(0)
    for linea in archivo.readlines():
        s=linea.rstrip('\n')
        s=s.rstrip('\r')
        s2 =s.partition(".")
        #print 'ID: '+ s2[0] + ' RUT: '+s2[2]
        Rut = s2[0]
        if 	Rut ==	Pal:
            archivo.close()
            return s2[0]
    archivo.close()

    return -1

#-------------------------------------------------------
def Verificar_acceso(ID1): #mejorar por que podia pasa cualquiera

	Contador=0
	archivo = open(TAB_AUTO, 'r')
	archivo.seek(0)
	for linea in archivo.readlines():
		s=linea.rstrip('\n')
		s2 =s.partition(".")
		s3 = s2[2].partition(".")
		#print 'QR: '+ s2[0] + ' ID: '+s3[0]
		ID2 = s3[0]
		if 	ID2 ==	ID1:
			Contador +=1
	archivo.close()
	return Contador

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------


#Clear_File(TAB_USER)
#Set_File(TAB_USER, 'Hola anderson\ncomensando denuevo\n')
#print Get_File(TAB_USER)
#print Get_Line(TAB_USER,2)
#Clear_Line(TAB_USER,1)
#Update_Line(TAB_USER,2,'OTRA cosa\n')       #incluir el/n
#Add_Line_End(TAB_USER, 'Dato al final\n')   #incluir el/n
#Add_Line_Pos(TAB_USER, 2, 'en posicion 2')  #incluir el/n
#Add_File(TAB_USER, 'mas cosa sin borrar el archivo\n')
#print Get_File(TAB_USER)
#print Num_lines(TAB_USER)




#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
# Clear_File(archivo):
# Get_File(archivo):
# Set_File(archivo, Texto):
# Add_File(archivo, Texto):

# Get_Line(archivo, Numero):
# Clear_Line(archivo, Numero):
# Update_Line(archivo, Numero, Dato): #incluir el/n
# Add_Line_End(archivo, Dato): #incluir el/n
# Add_Line_Pos(archivo, Numero, Dato): #incluir el/n
# Num_lines(a):


#---------------------------------------------------------
# hacer mas genericos y pociblemente reubicar
#---------------------------------------------------------
# Leer_Led():
# Leer():
# Verificar_ID(Pal): #mejorar por que podia pasa cualquiera
# ID(Pal): #mejorar por que podia pasa cualquiera
# Verificar_acceso(ID1): #mejorar por que podia pasa cualquiera
# Escrivir_Enviar(Texto):
# Escrivir(Texto):
# Escrivir_nuevo(a, Texto):
#-----------------------------------------------------------
#                   reubicar
#-----------------------------------------------------------

# Mejor_Opcion_link():
# Generar_ID_Tarjeta(MAC): #mejorar por que podia pasa cualquiera
# Estado_Usuario(Pal,P_I):
# Verificar_PIN(ID1, PIN): #revicion de pines
# PIN_Usado(ID1, PIN,Npines): #revicion de pines
#-------------------------------------------------------

"""
def Leer_Lineas(a):

    mensaje = ""
    arch = Get_archivo(a)
    if os.path.exists(arch):
        f = open (arch,'r')
        mensaje = f.readlines()
        f.close()
        return mensaje
    else:
        return mensaje

#-------------------------------------------------------
def Verificar_ID(Pal): #mejorar por que podia pasa cualquiera

	global N_A_Servidor
	archivo = open(N_A_Servidor, 'r')
	archivo.seek(0)
	for linea in archivo.readlines():
		s=linea.rstrip('\n')
		s=s.rstrip('\r')
		s2 =s.partition(".")
		#print 'ID: '+ s2[0] + ' RUT: '+s2[2]
		Rut = s2[0]
		if 	Rut ==	Pal:
			archivo.close()
			return s2[0]
	archivo.close()
	return -1
#-------------------------------------------------------
def ID(Pal): #mejorar por que podia pasa cualquiera

	global N_A_Servidor
	archivo = open(N_A_Servidor, 'r')
	archivo.seek(0)
	for linea in archivo.readlines():
		s=linea.rstrip('\n')
		s=s.rstrip('\r')
		s2 =s.partition(".")
		#print 'ID: '+ s2[0] + ' RUT: '+s2[2]
		Rut = s2[2]
		if 	Rut ==	Pal:
			archivo.close()
			return s2[0]
	archivo.close()
	return -1
#-------------------------------------------------------
def Verificar_acceso(ID1): #mejorar por que podia pasa cualquiera

	global	N_A_Lector
	Contador=0
	archivo = open(N_A_Lector, 'r')
	archivo.seek(0)
	for linea in archivo.readlines():
		s=linea.rstrip('\n')
		s2 =s.partition(".")
		s3 = s2[2].partition(".")
		#print 'QR: '+ s2[0] + ' ID: '+s3[0]
		ID2 = s3[0]
		if 	ID2 ==	ID1:
			Contador +=1
	archivo.close()
	return Contador
"""




"""

def Mejor_Opcion_link():

    opciones = Leer_Archivo(36)
    opciones = opciones.strip()
    #opciones = '0'
    #print opciones
    IP_Ser=Leer_Archivo(32)
    IP_Ser=IP_Ser.strip()
    Domi_Ser=Leer_Archivo(31)
    Domi_Ser=Domi_Ser.strip()

    IP_Bk = Leer_Archivo(34)
    IP_Bk=IP_Bk.strip()
    #print opciones
    #print Domi_Ser
    #print IP_Ser

    if opciones == '0':    return 'http://' + IP_Bk     #Mensajes('Test 0 Error, http Dominio NO, IP NO; https Dominio NO, IP NO.','Error')
    if opciones == '1':    return 'http://' + Domi_Ser  #Mensajes('Test 25%  OK, http Dominio OK, IP NO; https Dominio NO, IP NO.','OK')
    if opciones == '10':   return 'http://' + IP_Ser    #Mensajes('Test 25%  OK, http Dominio NO, IP OK; https Dominio NO, IP NO.','OK')
    if opciones == '11':   return 'http://' + IP_Ser    #Mensajes('Test 50%  OK, http Dominio OK, IP OK; https Dominio NO, IP NO.','OK')

    if opciones == '100':  return 'https://' + IP_Ser   #Mensajes('Test 25%  OK, http Dominio NO, IP NO; https Dominio NO, IP OK.','OK')
    if opciones == '101':  return 'https://' + IP_Ser   #Mensajes('Test 50%  OK, http Dominio OK, IP NO; https Dominio NO, IP OK.','OK')
    if opciones == '110':  return 'https://' + IP_Ser   #Mensajes('Test 50%  OK, http Dominio NO, IP OK; https Dominio NO, IP OK.','OK')
    if opciones == '111':  return 'https://' + IP_Ser   #Mensajes('Test 75%  OK, http Dominio OK, IP OK; https Dominio NO, IP OK.','OK')

    if opciones == '1000': return 'https://' + Domi_Ser #Mensajes('Test 25%  OK, http Dominio NO, IP NO; https Dominio OK, IP NO.','OK')
    if opciones == '1001': return 'https://' + Domi_Ser #Mensajes('Test 50%  OK, http Dominio OK, IP NO; https Dominio OK, IP NO.','OK')
    if opciones == '1010': return 'http://' + IP_Ser    #Mensajes('Test 50%  OK, http Dominio NO, IP OK; https Dominio OK, IP NO.','OK')
    if opciones == '1011': return 'http://' + IP_Ser    #Mensajes('Test 75%  OK, http Dominio OK, IP OK; https Dominio OK, IP NO.','OK')

    if opciones == '1100': return 'https://' + IP_Ser   #Mensajes('Test 50%  OK, http Dominio NO, IP NO; https Dominio OK, IP OK.','OK')
    if opciones == '1101': return 'https://' + IP_Ser   #Mensajes('Test 75%  OK, http Dominio OK, IP NO; https Dominio OK, IP OK.','OK')
    if opciones == '1110': return 'https://' + IP_Ser   #Mensajes('Test 75%  OK, http Dominio NO, IP OK; https Dominio OK, IP OK.','OK')
    if opciones == '1111': return 'https://' + IP_Ser   #Mensajes('Test 100% OK, http Dominio OK, IP OK; https Dominio OK, IP OK.','OK')




def Generar_ID_Tarjeta(MAC): #mejorar por que podia pasa cualquiera
        global N_A_ID_Lector

        Caracte         = ''
        Fecha_Init      = ''
        Consecutivo     = ''

        Contador=0

        archivo = open(N_A_ID_Lector, 'r')
        archivo.seek(0)
        for linea in archivo.readlines():
                s=linea.rstrip('\n')
                s=s.rstrip('\r')
                #s2 =s.partition(".")
                #print 'ID: '+ s2[0] + ' RUT: '+s2[2]
                if Contador == 0:  Caracte=s
                if Contador == 1:  Fecha_Init=s
                if Contador == 2:  Consecutivo=s

                #print s
                Contador+=1

        archivo.close()

        return Caracte+Fecha_Init+MAC+Consecutivo



def Estado_Usuario(Pal,P_I):

	if P_I == 0:
		ID_1 = ID(Pal)
	else:
		ID_1 = Verificar_ID(Pal)
		#ID_1 = Pal

	N_veri = Verificar_acceso(ID_1)


	#print 'ID: '
	#print ID_1
	#print 'Veces: '
	#print N_veri
	if N_veri != 0:
		if N_veri % 2 == 0	:	N_veri = 1 # Entrar
		else				:	N_veri = 2 # Salir

	if ID_1 == -1 and  N_veri == 0:					return ID_1, 'Denegado'		   #print 'NO existe'
	if ID_1 != -1 and  N_veri == 0 or N_veri == 1:	return ID_1, 'Access granted-E'#print 'Entrada'
	if ID_1 != -1 and  N_veri == 2:					return ID_1, 'Access granted-S'#print 'Salida'


def Verificar_PIN(ID1, PIN): #revicion de pines

        global	N_A_Pines
        archivo = open(N_A_Pines, 'r')
        archivo.seek(0)
        Revicion =''
        for linea in archivo.readlines():
                s=linea.rstrip('\n')
                s2 =s.split(".")
                ID2 = s2[0]
                if ID2 == ID1:
                        Revicion = s
                        break
        archivo.close()

        #print Revicion

        if Revicion.find(PIN) != -1:
                #print 'Existe en generados'
                return 1

        return 0

def PIN_Usado(ID1, PIN,Npines): #revicion de pines

        global	N_A_Pines_Usados
        archivo = open(N_A_Pines_Usados, 'r')
        archivo.seek(0)
        Revicion =''
        Usado = 0
        C_Pines = 0
        Usos = 0

        for linea in archivo.readlines():
                s=linea.rstrip('\n')
                s2 =s.split(".")
                ID2 = s2[1]
                if ID2 == ID1:
                        C_Pines = C_Pines + 1
                        Revicion = s
                        if Revicion.find(PIN) != -1:
                                #print 'Existe en usado'
                                Usos = Usos + 1
                                Usado = 1
                                #return 1

        archivo.close()

        return Usado, C_Pines, Usos


        #print Revicion



        return 0
"""

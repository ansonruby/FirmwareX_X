
import commands


import lib.Control_Archivos
import lib.Control_Fecha
import lib.Control_Ethernet


Tiempo                  = lib.Control_Fecha.T_Actual
Hora                    = lib.Control_Fecha.Hora_Actual


Leer_Archivo            = lib.Control_Archivos.Leer_Archivo
Borrar                  = lib.Control_Archivos.Borrar_Archivo

Veri_Firmware           = lib.Control_Ethernet.Veri_Firmware #pruebas de actualizar firmware
Confimacion_Firmware    = lib.Control_Ethernet.Confimacion_Firmware #pruebas de actualizar firmware
Serial                  = lib.Control_Ethernet.ID_Tarjeta


# variablee proceso actualizador de firmware
E_Actualizacion_Firmware=0
R_Actualizacion_Firmware=0 # actualizar en otromomento
A_Actualizacion_Firmware=0 # bloque


PAF_Mensajes = 0     # 0: NO print  1: Print




def Filtro_Caracteres(s): # eliminar los caracteres y estructura Jason

    s = s.replace('"',"")
    s = s.replace('[',"")
    s = s.replace('{',"")
    s = s.replace(']',"")
    s = s.replace('}',"")
    s = s.replace('data:',"")
    s = s.replace(',',"\r\n")
    return s







def  Procedimiento_Actualizar_Firmware():
    global E_Actualizacion_Firmware
    global R_Actualizacion_Firmware
    global A_Actualizacion_Firmware
    if A_Actualizacion_Firmware==1:
        E_Actualizacion_Firmware=1
        A_Actualizacion_Firmware=0
        if PAF_Mensajes:
            print 'Proceso de revision del firmware'
        Respuesta = Veri_Firmware(Tiempo(), Leer_Archivo(17).replace('\n',''))       #enviar peticion a servidor

        if Respuesta.find("Error") == -1:
            #if Respuesta!='NO': #respuesta del servidor
            #print Respuesta.text
            # -------------------------------
            #       sacar informacion
            #s = Filtro_Caracteres(Respuesta.text)
            s = Filtro_Caracteres(Respuesta)

            s=s.partition('\n')
            s1 = s[0].replace('id:','')
            ID_F = s1.replace('\r','')
            s2 = s[2].partition('\r')
            s3 = s2[0].replace('version:','')
            Vercion_F =s3.replace('\r','')
            Git_F = s2[2].replace('\r','')
            Git_F = Git_F.replace('\n','')
            Git_F = Git_F.replace('github:','')

            #--------------------------------
            if PAF_Mensajes:
                print 'ID: '+ ID_F + ' vercion: '+Vercion_F + ' git: '+Git_F

            if ID_F=='OK':
                if PAF_Mensajes:
                    print 'Estoy actualizado'
            else:
                #print Leer_Estado(20) # Estado Actualizador
                if Leer_Estado(20) == '0': # estado inicial de actualizacion firmware
                    if PAF_Mensajes:
                        print 'Estado incial'
                    Verificar_Actualizacion(ID_F, Vercion_F, Git_F) #activar cuuando se quiea actualizar

        else :
            if PAF_Mensajes:
                print 'NO contesto el servidor'


def Actualizar_Firmware(Hora_Actualizacion):

        global E_Actualizacion_Firmware
        global R_Actualizacion_Firmware
        global A_Actualizacion_Firmware

        if Leer_Archivo(40) == '1': # forzando la actualizacion por Teclado
            Borrar(40)
            A_Actualizacion_Firmware=1
            E_Actualizacion_Firmware=0
            Procedimiento_Actualizar_Firmware()

        if Hora() == Hora_Actualizacion and E_Actualizacion_Firmware == 0: Procedimiento_Actualizar_Firmware()

        if Hora() != Hora_Actualizacion and A_Actualizacion_Firmware==0:
                if PAF_Mensajes:
                    print 'Habilitacion hora actualizacion Firmware'
                A_Actualizacion_Firmware=1
                E_Actualizacion_Firmware=0

        if Leer_Archivo(20) == '3':
            if PAF_Mensajes:
                print 'Hay una terminacion de firmware enviar respuesta al servidor'
            Ultimo = ""
            res16 = Leer_Archivo(19) # Leer en donde va el proceso de actualizacion
            #print res16
            #print len (res16)

            if len (res16) != 0:

                Faces =res16.split("\n")
                for Face in range(len(Faces)):
                    c = Faces[Face]
                    #print Face
                    #print c
                    c2 =c.split(" ")
                    if len(c2[0]) >= 2:
                        #print len(c2[0])
                        #print c2[0]
                        Ultimo = c2[0]
            if PAF_Mensajes:
                print Ultimo
            if Ultimo == '12.3':
                if PAF_Mensajes:
                    print 'Enviar respuesta al servidor Correcta'
                Borrar(20)                  # Estado Actualizador
                Escrivir_Estados('0',20)    # Estado Actualizador
                Borrar(19)                  # log
                #antes de enviar respues actualizar el actualizador
                Actualizar_Actualizador()

                print Confimacion_Firmware(Tiempo(), Leer_Archivo(17).replace('\n',''),'')

        if Leer_Archivo(20) == '5':
            Ultimo = ""
            res16 = Leer_Archivo(19) # Leer en donde va el proceso de actualizacion
            #print res16
            #print len (res16)

            if len (res16) != 0:

                Faces =res16.split("\n")
                for Face in range(len(Faces)):
                    c = Faces[Face]
                    #print Face
                    #print c
                    c2 =c.split(" ")
                    if len(c2[0]) >= 2:
                        #print len(c2[0])
                        #print c2[0]
                        Ultimo = c2[0]

            Borrar(20)                  # Estado Actualizador
            Escrivir_Estados('0',20)    # Estado Actualizador
            Borrar(19)                  # log
            if PAF_Mensajes:
                print Ultimo
            print Confimacion_Firmware(Tiempo(), Leer_Archivo(17).replace('\n',''),Ultimo)





def Actualizar_Actualizador():

    #Log_Actualizador('4. Cambiar nombre de firmware en ejecucion')
    res = commands.getoutput('[ ! -f /home/pi/ActualizadorBK ] && echo "Existe" || echo "NO exiete"')
    if res == 'Existe':
        if PAF_Mensajes:
            print 'Eliminar BK'
        res = commands.getoutput('sudo rm -R' + ' /home/pi/ActualizadorBK')
        print res

    res = commands.getoutput('mv /home/pi/Actualizador /home/pi/ActualizadorBK')
    res = commands.getoutput('cp -r /home/pi/Firmware/Actualizador /home/pi/Actualizador')
    res = commands.getoutput('chmod -R 755 /home/pi/Actualizador/sh/app_Actualizando.sh')
    if PAF_Mensajes:
        print 'Respuesta:'+ res


def Verificar_Actualizacion ( ID_F, Vercion_F, Git_F):

    if ID_F !=  Serial :
        if PAF_Mensajes:
            print 'NO es para mi'
        return '0'

    C =str(Leer_Archivo(17))  # vercion firmware
    if C.find(Vercion_F) != -1 :
        if PAF_Mensajes:
            print 'ya esta actualizado'
        return '0'
    else:
        if PAF_Mensajes:
            print 'Devo actualizar'
        # cambiar estado y  guarrdar los datos
        Borrar(15)
        Escrivir_Archivo(ID_F,15)
        Escrivir_Archivo(Vercion_F,15)
        Escrivir_Archivo(Git_F,15)

        Borrar(20)              #
        Escrivir_Estados('1',20)   # Estado inicial del actualizador
        return '1'

    return '2'

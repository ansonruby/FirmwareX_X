
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
def Get_Line(arch, Numero):
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        return lineas[Numero-1] # revisar si comensar en 1 o 0
    else:
        return ""

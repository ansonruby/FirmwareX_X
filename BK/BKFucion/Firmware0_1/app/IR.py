
import commands
import sys
import time
import RPi.GPIO as GPIO #Libreria Python GPIO
import threading


GPIO.setmode (GPIO.BOARD)
CC_Pin_IR =  31#5 #8sin fuente #3 para la sinta de seguridad
CC_Pin_Led  =  3
GPIO.setup(CC_Pin_IR, GPIO.IN)
GPIO.setup(CC_Pin_Led, GPIO.OUT)
a = '0'
b = '0'
Status_Hilo_activo =0


GPIO.output(CC_Pin_Led, GPIO.LOW)
time.sleep(1.10)
GPIO.output(CC_Pin_Led, GPIO.HIGH)

Estados_IR = '1' #estados del dispositivos para visualizar en los leds
Estados_Antes_IR = '1'

def Eventos_IR():
    global Estados_IR
    global Estados_Antes_IR
    global CC_Pin_IR
    global CC_Pin_Led

    Estados_IR= str(GPIO.input(CC_Pin_IR))
    #print Estados_IR
    if Estados_IR != Estados_Antes_IR:
        Estados_Antes_IR =  Estados_IR
        #print 'Cambio:' + Estados_IR
        if Estados_IR == '0':
            GPIO.output(CC_Pin_Led, GPIO.LOW)
            #time.sleep(0.10)
            #GPIO.output(CC_Pin_Led, GPIO.HIGH)
        else:
            GPIO.output(CC_Pin_Led, GPIO.HIGH)

"""
print 'listo'
while (True):

        time.sleep(0.10)
        Eventos_IR()
"""

import time

def Fecha_Actual():
	tiempo_segundos = time.time()
	#print(tiempo_segundos)
	tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
	tiempo_cadena = time.strftime("%d/%m/%y %I:%M:%S%p")
	#print(tiempo_cadena)
	return tiempo_cadena

def Hora_Actual():
	tiempo_segundos = time.time()
	#print(tiempo_segundos)
	#tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
	tiempo_cadena = time.strftime("%I:%M %p")
	#print(tiempo_cadena)
	return tiempo_cadena

def T_Actual():
	return str(int(time.time()*1000.0))

def Time_add_seg(Tiempo_mas):
	return time.time() + Tiempo_mas

def Time_add_min(Tiempo_mas):
	return time.time() + Tiempo_mas*60

def Time_add_hora(Tiempo_mas):
	return time.time() + Tiempo_mas*(60*60)

"""""
OLIMPIADAS: 
En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide 
los siguientes tiempos:
Hannah Neise:   8 minutos 3 segundos y 10 centésimas
Jackie Narracott:  12 minutos 7 segundos y 8 centésimas
Kimberley Bos:   9 minutos 14 segundos y 3 centésimas
1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas 
2. Convierte los tiempos de minutos-segundos-centésimas a segundos
3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en 
metros por segundo. 
4. Imprime los resultados por pantalla
"""
#pedir tiempo de cada finalista
tiempo_hanna=input("hola Hannah ingrese su tiempo (MINUTOS,SEGUNDOS,CENTESIMAS) : ")
tiempo_jackie=input("hola jackie ingrese su tiempo (MINUTOS,SEGUNDOS,CENTESIMAS) : ")
tiempo_kimber=input("hola kimber ingrese su tiempo (MINUTOS,SEGUNDOS,CENTESIMAS) : ")
#convertir los tiempos a segundos(primero se extraen)
minutos_hannah,segundos_hannah,centesimas_hannah=tiempo_hanna.split(" ")
minutos_jackie,segundos_jackie,centesimas_jackie=tiempo_jackie.split(" ")
minutos_kimber,segundos_kimber,centesimas_kimber=tiempo_kimber.split(" ")

time_hannah=float(minutos_hannah)*60 + float(segundos_hannah)+float(centesimas_hannah)*0.01
time_jackie=float(minutos_jackie)*60 + float(segundos_jackie)+float(centesimas_jackie)*0.01
time_kimber=float(minutos_kimber)*60 + float(segundos_kimber)+float(centesimas_kimber)*0.01

#calculando la velocidad
#velocidad=distancia/tiempo
velocidad_hannah=100.0/time_hannah
velocidad_jackie=100.0/time_jackie
velocidad_kimber=100.0/time_kimber
#mostrar resultado
print(f"la velocidad de hannah es {velocidad_hannah} Metros por segundos")
print(f"la velocidad de jacki es {velocidad_jackie} Metros por segundos")
print(f"la velocidad de kimber es {velocidad_kimber} Metros por segundos")
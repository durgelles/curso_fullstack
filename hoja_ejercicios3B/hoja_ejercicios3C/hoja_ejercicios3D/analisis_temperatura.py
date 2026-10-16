"""Enunciado

Imagina que tienes una lista con las temperaturas registradas durante 14 días consecutivos. Quieres calcular la suma de las temperaturas registradas para cada día de la semana.

Dispones de estas listas:

temperaturas = [28, 30, 31, 29, 32, 33, 27, 28, 29, 30, 31, 32, 34, 28]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves",
               "Viernes", "Sábado", "Domingo"]
¿Qué tienes que hacer?
Crear una lista llamada temperatura_dias con siete ceros.
Crear una variable dia que comience en cero.
Recorrer la lista temperaturas con un bucle for.
Acumular cada temperatura en la posición correspondiente de temperatura_dias.
Avanzar el contador dia y reiniciarlo cuando llegue a siete.
Mostrar el resultado indicando el día de la semana y la suma de sus temperaturas.

Pista: la estructura es prácticamente la misma que utilizaste en el ejercicio de las ventas. Intenta escribir el código sin mirar tu solución anterior."""

#crear lista de temperatura
temperaturas = [28, 30, 31, 29, 32, 33, 27, 28, 29, 30, 31, 32, 34, 28]
#crear lista de semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves",
               "Viernes", "Sábado", "Domingo"]
#Crear una lista llamada temperatura_dias con siete ceros
temperaturas_dias=[0,0,0,0,0,0,0]
#crear una variable para acumular en cada dia de la semana
dia=0
#Recorrer la lista temperaturas con un bucle for

for temperatura in temperaturas:
    temperaturas_dias[dia]+=temperatura
    dia+=1

    if dia==7:
        dia=0

for i in range(len(dias_semana)):
     print(f"el dia {dias_semana[i]} la suma de sus temperaturas es :{temperaturas_dias[i]} ")






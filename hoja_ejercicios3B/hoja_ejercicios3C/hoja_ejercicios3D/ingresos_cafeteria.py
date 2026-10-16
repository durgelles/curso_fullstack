"""Ejercicio 2: Ingresos de una cafetería

Dispones de estos datos:

ingresos = [150, 200, 180, 250, 300, 400, 350,
            170, 220, 190, 280, 320, 450, 380,
            160, 210, 200, 270, 330, 500, 420]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves",
               "Viernes", "Sábado", "Domingo"]
Tu misión

Crea un programa que acumule los ingresos de los 21 días y muestre el total correspondiente a cada día de la semana"""

#creando listas de ingresos 
ingresos = [150, 200, 180, 250, 300, 400, 350,
            170, 220, 190, 280, 320, 450, 380,
            160, 210, 200, 270, 330, 500, 420]
#creando lista  de dia de la semana

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves",
               "Viernes", "Sábado", "Domingo"]
#se crea lista para acumular cada ingreso en cada dia de la semana y sumarlo
ingresos_dias=[0,0,0,0,0,0,0]
# se crea variable que es es la que recorre cada dia
dia=0
# se recorre con un bucle
for ingreso in ingresos:
    ingresos_dias[dia]+=ingreso
    dia+=1

    if dia==7:
    

     dia=0

mayor_ingreso=max(ingresos_dias)
menor_ingreso=min(ingresos_dias)
for i in range(len(dias_semana)):
   print(f"el dia {dias_semana[i]} los ingesos fueron de: {ingresos_dias[i]}") 
   
   if ingresos_dias[i]==mayor_ingreso:
      mayor = dias_semana[i]

   if ingresos_dias[i]== menor_ingreso:
      menor=dias_semana[i]   

print(f"el dia de mayor ingreso fue {mayor} con {mayor_ingreso}")
print(f"el dia de menor ingreso fue {menor} con {menor_ingreso}")





""""ALCULADORA DE AHORROS:
Ahora que ya tienes soltura con los fundamentos de Python toca poner tus conocimientos en 
práctica en un proyecto más extenso. El objetivo es crear un programa con el que puedas calcular 
tus ahorros anuales. El programa deberá calcular cuánto puede ahorrar una persona dado sus 
ingresos por hora, sus horas trabajadas y su gasto de vida semanal. 
1. Primero haremos que el programa nos pida nuestro nombre y después imprima un saludo por 
pantalla de tipo: ‘Hola <Nombre>’
2. Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables 
diferentes
3. Multiplica ambas variables para obtener el salario semanal
4. Ahora calcula las ganancias anuales. Guarda el valor en una variable.
5. Ahora imprime por pantalla un mensaje del tipo: ‘<Nombre> tiene unas ganancias anuales de: 
<cantidad> euros’
6. Pide los gastos semanales por pantalla y guárdalos en una variable.
7. Calcula el gasto anual 
8. ¡Recuerda añadir comentarios sobre lo que esta haciendo cada parte del código!
9. Los ahorros anuales serán la resta entre lo ganado durante el año menos los gastos anuales.
10. Imprime los resultados por pantalla
¿Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y decidiese reducir sus 
gastos a 3/4 de lo que gastaba antes, tendría suficiente dinero para sus gastos?
"""""
#se le pide al usaario el los datos, nombre , cuanto gana por horas , horas trabajadas
nombre=input("ingrese su nombre: ")
print(f"hola,{nombre.title()} bienvenido ")
dinero_hora=float(input("cuanto ganas por hora "))
horas_de_trabajo=float(input("cuantas horas a la semana trabaja "))
# calcular el salario semanal
salario_semanal=dinero_hora*horas_de_trabajo
#calcular el salario anual
ganancias_anuales=salario_semanal*52
print(f"{nombre.title()} , tienes una ganacia anuales de : {ganancias_anuales} euros")
#pedir los gastos mensuales
gastos_semanales=float(input(" de cuantos euros son tus gastos semanales "))
#calculamos el gasto anual
gastos_anuales =gastos_semanales*52 
print(f"{nombre.title()}, tus gastos anuales con de {gastos_anuales} euros")
#calculamos los ahorros anuales
ahorros_anuales=ganancias_anuales-gastos_anuales
print(f"{nombre.title()}, tus ahorros anuales son de {ahorros_anuales},euros")


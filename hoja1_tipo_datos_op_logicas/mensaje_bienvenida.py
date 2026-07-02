"""""
MENSAJE DE BIENVENIDA: 
El objetivo de este ejercicio es que crees un script que dado un nombre de usuario le de la 
bienvenida con su nombre en el formato correcto
1. Escribe un programa que almacene el string ‘estas usando python’ en una variable y luego 
muestre por pantalla el contenido de la variable.
2. Amplía el programa para que pregunte el nombre de usuario en la terminal y después muestre 
por pantalla el mensaje: ‘¡Hola, <nombre>, estas usando python! (<nombre> es el nombre que 
el usuario hay introducido)
3. Usa una función interna de python que actúe sobre el string que has creado antes para que el 
mensaje que imprima sea: ‘¡HOLA, <NOMBRE>, ESTAS USANDO PYTHON!
4. Cambia el script para que el mensaje se imprima al completo en minúsculas (usa de nuevo 
una función interna de python)
5. Cambia el script para que, sin importar como introduzca el usuario el nombre, lo formatee para 
que tenga el formato correcto, es decir con la primera letra en mayúsculas y las demás en 
minúscula (Si el usuario introduce el nombre ferNanDO, el programa deberá formatear el 
nombre a Fernando).
6. Amplía el script para que si por error el usuario introduce un nombre con un punto en medio, el 
programa automáticamente lo borre (Si el usuario introduce el nombre Fern.ando, el programa 
deberá formatear el nombre a Fernando)
7. Consigue que el mensaje final sea: ‘¡Hola, <Nombre>, estas usando Python!’
"""""

#pedir nonbre al usuario
nombreUsuario=input("hola , cual es su nombre ")
print(f"bienvenido{nombreUsuario}")

mensaje="estas usando Python"
print(f"HOLA, {nombreUsuario.upper()}, {mensaje.upper()}")
print(f"Hola, {nombreUsuario.lower()}, {mensaje.lower()}")
print(f"Hola, {nombreUsuario.title()}, {mensaje.title()}")
print(f"Hola, {nombreUsuario.upper().replace(".","")}, {mensaje.upper().replace(".","")}")
print(f"Hola, {nombreUsuario.title()}, {mensaje}")

""""
4. Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
pantalla el número de veces que aparece la letra en la frase. 
"""""
#pedir una frase al usuario
frase_usuario=input("ingrese una frases: ")
letter=input("ingrese una letra : ")
cont=0

#recorrer la frase para ver cuantas veces sale la 
for letra in frase_usuario:
    if letra==letter:
     cont=cont+1
   
else:
    print(f"la letra {letter} no esta en la frase ingresada ")

print(f"la letra {letter} sale en la frase {cont} veces ")

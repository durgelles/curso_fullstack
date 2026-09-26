""""ENCRIPTACIÓN ROT13:
El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
catalán la ”Ç”, en alemán la ”ß”, etc.).
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual. 
         [a,b,c,d,e,f,g,h,i,j,k,l,m] 		 	 [H, O, L, A]
 
                ROT13
		 
         
          
         [n,o,p,q,r,s,t,u,v,w,x,y,z]		 	 [U, B, Y, N]

         
         
         
1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
codificado según el cifrado ROT13
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
esta codificación ROT13 de la otra. 



"""
#crear lista del abecedario
abecedario_minuscula=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
abecedario_mayuscula=[]
for char in abecedario_minuscula:
    abecedario_mayuscula.append(char.upper())

#pedir una frase al usuario
texto_usuario=input("ingrese un texto :")
segundo_texto_usario=input("ingrese el segundo texto : ")
#crear variable para guardar el texto en forma se string
texto_rot_string=""
#recorrer la frase 
for char in texto_usuario:
    if char in abecedario_minuscula:
        
            for j in range(len(abecedario_minuscula)):
                if char==abecedario_minuscula[j]:
                    if j+13<26:
                     texto_rot_string=texto_rot_string+abecedario_minuscula[j+13]
                    else:
                     texto_rot_string=texto_rot_string+abecedario_minuscula[j+13-26]
    elif char in abecedario_mayuscula:
       
                   for j in range(len(abecedario_mayuscula)):
                       if char==abecedario_mayuscula[j]:
                           if j+13<26:
                            texto_rot_string=texto_rot_string+abecedario_mayuscula[j+13]
                           else:
                            texto_rot_string=texto_rot_string+abecedario_mayuscula[j+13-26]
    else:
        texto_rot_string=texto_rot_string+char


print(texto_rot_string)










                
                

           
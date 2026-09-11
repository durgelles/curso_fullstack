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
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
texto_rot_1=[]
texto_rot_2=[]
#pedir una frase al usuario
texto_usuario_1=input("ingrese el primer texto :")
texto_usuario_2=input("ingrese el segundo texto :")
#recorrer cada letra de la frase o palabra
for i in range(len(texto_usuario_1)):
    for j in range(len(abecedario)):
        if texto_usuario_1[i]==abecedario[j]:
            if j+13<26:
             texto_rot_1.append(abecedario[j+13])
            else:
               texto_rot_1.append(abecedario[j+13-26])


texto_rot1_string= "".join(texto_rot_1) 

#recorriendo la segunda frase
for i in range(len(texto_usuario_2)):
    for j in range(len(abecedario)):
        if texto_usuario_2[i]==abecedario[j]:
            if j+13<26:
             texto_rot_2.append(abecedario[j+13])
            else:
               texto_rot_2.append(abecedario[j+13-26])


texto_rot2_string= "".join(texto_rot_2) 


if texto_rot1_string == texto_usuario_2  :
   print(f" el segundo texto : {texto_usuario_2} es la codificacion rot13 del primer texto : {texto_usuario_1}")
else:
   print("no existe codificacion rot13 entre los texto")
   
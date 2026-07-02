"""""
RESTAURANTE ONLINE:
En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente 
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana. 
Los ingredientes extra de la hamburguesa clásica son:- Queso Idiazabal- Bacon- Huevo
Los ingredientes extra de la hamburguesa vegana son:- Tofu- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la 
respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos. 
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus 
ingredientes.
"""
#pedir al usuario que tipo de hamburguessa desea
tipo_hamburguesa=input("ingrese el tipo de hamburguesa que desea(clasica o vegana) : ").lower()
if tipo_hamburguesa=="clasica":
    agrego=input(" que agrego desea de la Hamburguesa clasica :  queso idiazabal- bacon- huevo ").lower()
    if agrego in  " queso idiazabal bacon huevo ":
     print(f"su hamburguesa es {tipo_hamburguesa} con {agrego} ")
    else:
       print(" el agrego no esta en el menu ")
elif tipo_hamburguesa=="vegana":
    agrego=(input("que tipo de agrego desea para su hamburguesa vegana : Tofu o cebolla caramelizada ")).lower()
    if agrego in "tofu cebolla caramelizada":
      print(f"su hamburguesa es {tipo_hamburguesa} con {agrego} ")
    else:
       print(" el agrego no esta en el menu ")
else:
   print("  no es valido el tipo de hamburguesa")

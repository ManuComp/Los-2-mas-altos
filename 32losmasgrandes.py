#Integrantes del equipo
#Chavez Pavon Jose Manuel
#Ramirez Ramirez Servando
#Saules Rojas David
#Lopez Adriana

import random 

#Funcino para crear una lista
#La cual usaremos para simular las alturas de las 32 personas
#La llenaremos de forma aleatoria
def lista (): 
	l = [] #Creamos la lista de las "alturas"
	for x in range (0,32):
		l.append(random.randint(1,300))
	return l #Regresamos la lista


#Funcion para obtener cual es la persona mas alta
#Recorremos la lista de dos en dos pregutando cual es mayor
#Los elementos mayores los agregamos a una nueva lista 
#A los elementos que fueron comparados los metemos en un diccionario
#Para despues con ellos obtener el segundo mayor
#var "lista" = La lista de las alturas 
#var "dic" = el diciconario de los elementos comparados 
def primero (lista, dic):
	a=0 #Iterador 'a' a utilizar para recorrer la lista inicializado en cero
	l2 = [] #Lista para ir agregando a los elementos mayores
	#Clausula de escape
	if len(lista) == 1:
		print lista[0]
		#Llamada a la funcion segundo, la cual nos dara el segundo mas alto
		segundo(dic[lista[0]])
		return
	#Recorremos la lista buscando a los elementos mayores
	while a<len(lista):
		#Verificamos que elmento es mayor
		if lista[a] > lista[a+1]:
			l2.append(lista[a])#El mayor lo agregamos a l2
			dic[lista[a]] = str(lista[a+1]) + " "#Al menor lo agregamos al diccionario pasandole como llave al elemento mayor
		#El caso contrario del if
		else: 
			l2.append(lista[a+1])#El mayor lo agregamos a l2
			dic[lista[a+1]] = str(lista[a]) + " "#Al menor lo agregamos al diccionario pasandole como llave al elemento mayor
		a+=2 #Aumentos nuestro iterador dos posiciones
	primero(l2, dic) #Llamada recursiva de la funcion 

#Funcion para obtener el segundo elementos mas grande
#var "cadena" = la cadena que nos da el diccionario que tiene como llave
#al elemento mas grande
def segundo (cadena):
	repe = cadena.split()#Separamos la cadena por espacios con split()
	print max(repe)#Obtenemos el elemento mayor de la cadena con max() y lo imprimimos
	return 




l = lista()#Creamos la lista a ejecutar
dicc={}#Diccionario para los elementos que fueron comparados pero no fueron mayores
primero(l,dicc)#Llamada de la funcion primero



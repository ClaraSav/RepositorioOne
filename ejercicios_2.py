# -*- coding: utf-8 -*-

#UNEFA-- Ingenieria de Sistemas nocturno
#Ejercicios #2 de Lenguajes de Programación 2
#Alumna: Clara Savelli

#define una lista para utilizar en los ejercicios
def leer_lista():
	lista = []
	while True:
		#llenamos el diccionario
		opcion = input("\n1 para ingresar palabra \n2 para salir \nOpcion: ")
		if opcion == 1:
			lista.append(raw_input("introduzca una palabra: "))
		elif opcion == 2:
			break
		else:
			print "opcion incorrecta, intente nuevamente"
	return lista



#1.Desarrolle una programa que reciba una lista de palabras, de igual 
#forma debe recibir un prefijo y retornar todas las palabras que inicien
# con dicho prefijo.

def wordsWithPrefix(words):
	wordPre = [] #para almacenar las palabras con el prefijo
	#words = leer_lista()
	prefix = raw_input("introduzca un prefijo: ")
	
	for word in words:
		if word.startswith(prefix):
			wordPre.append(word)
	return wordPre

#2. Desarrolle un programa que reciba mediante bloques de repetición 
#información bajo la estructura de un diccionario, es decir, debe 
#recibir la clave y el valor correspondiente hasta que el usuario decida
# dejar de ingresar información, luego debe retornar una lista con todas
# las llaves que corresponden a valores numéricos (enteros o decimales).

#define un diccionario
def diccio():
	dic = {}
	while True:
		#llenamos el diccionario
		opcion = input("\n1 para ingresar clave y valor \n2 para salir \nOpcion: ")
		if opcion == 1:
			clave = raw_input("ingrese clave: ")
			dic[clave] = raw_input("ingrese valor: ")
		elif opcion == 2:
			break
		else:
			print "opcion incorrecta, intente nuevamente"
	return dic

def llavesNum():
	dicc = diccio()
	#buscamos las claves con valores numericos
	ClaveNum = []
	for i in dicc.keys(): 
		if i.isdigit(): #para ver si es entero
			ClaveNum.append(i)
		if '.' in i: # para ver si es float
			numerof = ""
			for j in range(len(i)):
				if j != i.find('.'): 
					numerof += i[j]
				elif j == i.find('.'): #descartamos el primer punto
					continue
				else:
					numerof += i[j]
			if numerof.isdigit():
				ClaveNum.append(i)
	return ClaveNum
			
#3. Desarrolle un programa que reciba un diccionario tal que retorne 
#una lista con todos los valores del diccionario. En esta lista no 
#se deben incluir repetidos.

def valoresRep(dicti):
	valores = []
	for v in dicti:
		if v in valores:
			continue
		else:
			valores.append(v)
	return valores

#4. Desarrolle un programa que reciba un diccionario y una lista, el 
#retorno debe ser los valores del diccionario que tengan su clave 
#en la lista recibida.

def buscarPorClave(dic, lista):
	valores = []
	for i in lista:
		if i in dic.keys():
			valores.append(dic[i])
	return valores

#5. Desarrolle un programa que reciba dos diccionarios y retorne una lista 
#con los elementos que no se repitan en las claves de los diccionarios.

def compararDic():
	print "primer diccionario\n"
	dic1 = diccio()
	print "\nsegundo diccionario \n"
	dic2 = diccio()
	
	#verificamos los que se repiten
	repetidos = []
	for i in dic1:
		for j in dic2:
			if i == j:
				repetidos.append(i)
	
	#guardamos todos los demás en una lista
	lista = []
	for i in dic1:
		if not(i in repetidos):
			lista.append(i)
	for j in dic2:
		if not(j in repetidos):
			lista.append(j)
	return lista

#6. Desarrolle un programa que reciba un diccionario y retorne otro
# diccionario donde las claves del diccionario recibido se conviertan 
#en los valores y los valores en las claves.

def intercambio(dicci):
	dicNuevo = {}
	for clave in dicci:
		dicNuevo[dicci[clave]] = clave
	return dicNuevo

#7. Desarrolle un programa donde dado un numero n se cree un diccionario 
#con la dimensión de dicho numero, donde la clave deberá estar 
#comprendidas entre el 0 y el numero n y los valores entre el numero n
#y el numero 0. ejemplo: n=5 {‘0’:5,’1’:4,’2’:3,’3’:2,’4’:1,’5’:0}

def ndiccionario():
	N = input("ingrese un valor entero: ")
	x = N
	dic = {}
	for n in range(N + 1):
		if x >= 0:
			dic[n] = x
			x -= 1
	return dic

#8. Suponga un diccionario que contiene como llave el nombre de una 
#persona y como valor una lista con todos sus “gustos”. Desarrolle 
#un programa que realice las siguientes acciones:
#- Si la persona no existe la agregue al diccionario con una lista que 
#contiene un solo elemento.
#- Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
#- Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.

def gustos():
	dicci = {}
	print "Ingrese el nombre de la persona con todos sus gustos\n"
	while True:
		opcion = input("1. Ingresar persona\n2. Salir \nopcion: ")
		if opcion == 1:
			gustos = []
			nombre = raw_input("Nombre: ")
			gusto = raw_input("Gusto: ")
			gustos.append(gusto)
			if not(nombre in dicci):
				dicci[nombre] = gustos
			elif not(gusto in dicci[nombre]):
				dicci[nombre].append(gusto)
			else:
				continue
		elif opcion == 2:
			break
		else:
			print "\nopción invalida, intente nuevamente\n"
	return dicci

#FUNCIONES PARA PROBAR LOS EJERCICIOS

#print wordsWithPrefix(leer_lista())
#print llavesNum()
#print valoresRep(diccio())
#print buscarPorClave(diccio(), leer_lista())
#print compararDic()
#print intercambio(diccio())
#print ndiccionario()
print gustos()

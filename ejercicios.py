# -*- coding: utf-8 -*-
#!/usr/bin/python

#UNEFA-- Ingenieria de Sistemas nocturno
#Ejercicios de Lenguajes de Programación 2
#Alumna: Clara Savelli


#1) Diseña un algoritmo para calcular el área de un circulo dado su radio
#(Recuerda que el área de un circulo es pi veces el cuadrado del radio.).

def area_circulo():
	radio = input("introduzca el radio del circulo: ")
	Pi = 3.1416 #redondeo de pi a cuatro decimales
	
	#fórmula del área del circulo
	area = Pi * (radio ** 2.0)
	print area

#2) Diseña un algoritmo que calcule el IVA (16%) de un producto dado su
#precio de venta sin IVA.

def calculo_iva():
	precio = input("introduzca el precio del producto: ")
	
	iva = (16 * precio) / 100
	precio_con_iva = precio + iva
	print "El iva es: " + str(iva)
	print "El precio más el iva es: " + str(precio_con_iva)

#3) Traduce las siguientes expresiones matemáticas a Python y evalualas. Trata de
#utilizar el menor número de paréntesis posible.

def expresiones():
	a = 2 + 3*6/2
	b = (4 + 6)/(2 + 3)
	c = (4/2)**5
	d = (4/2)**(5+1)
	e = (-3) **2
	f = -3**2
	
	ecuaciones = [a,b,c,d,e,f]
	for i in ecuaciones:
		print str(i) + "\n"

#4) ¿Que resultara de evaluar las siguientes expresiones? Presta especial atención al
#tipo de datos que resulta de cada operación individual.

def tipo_resultado():
	a = 1 / 2 / 4.0 
	# = (1/2)/4.0 = 0/4.0 = 0.0
	b = 1 / 2.0 / 4.0 
	# = (1/2.0)/4.0 = 0.5/4.0 = 0.125
	c = 1 / 2.0 / 4 
	# = (1/2.0)/4 = 0.5/4 = 0.125
	d = 1.0 / 2 / 4 
	# = (1.0/2)/4 = 0.5/4 = 0.125
	e = 4 ** .5 
	# = 4 ** 0.5 = 2.0
	f = 4.0 ** (1/2) 
	# = 4.0 ** (1/2) = 4.0 ** 0 = 1.0
	g = 4.0 ** (1/2) + 1/2 
	# = (4.0 ** (1/2)) + 1/2 = (4.0 ** 0) + 1/2 = 1.0 + 0 = 1.0
	h = 4.0 ** (1.0/2) + 1 / 2.0 
	# = 4.0 ** 0.5 + 0.5 = 2.0 + 0.5 = 2.5
	i = 3e3 /10 
	# = (3*10**3)/10 = 3000.0/ 10 = 300.0
	j = 10 / 5e-3 
	# = 10 / 5e(-3) = 10/0.005 = 2000.0
	k = 10/ 5e-3 + 1 
	# = 10 / 5e(-3) + 1= 10/0.005 + 1 = 2000.0 + 1 = 2001.0
	l = 3 / 2 + 1 
	# = (3 / 2) + 1 = 1 + 1 = 2
	
	resultados = [a,b,c,d,e,f,g,h,i,j,k,l]
	for i in resultados:
		print str(i) + "\n"

#5) Diseña un programa que, a partir del valor de la base y de la altura de un
#triangulo (3 y 5 metros, respectivamente), muestre el valor de su área (en metros
#cuadrados).

def area_triangulo():
	base = 3
	altura = 5
	
	area = base * altura / 2.0
	print "area del triangulo: " + str(area) + " metros cuadrados"

#6) Haz un programa que pida al usuario una cantidad de euros, una tasa de interés y
#un numero de años. Muestra por pantalla en cuanto se habrá convertido el
#capital inicial transcurridos esos años si cada año se aplica la tasa de interés
#introducida.

def intereses():
	print "Introduzca todos los datos pedidos: "
	euros = input("Cantidad en euros: ")
	tasa = input("Tasa de interés: ")
	anos = input("Cantidad de años: ")
	
	cap_final = euros
	contador = 1
	while contador <= anos:
		cap_final = (cap_final * tasa /100.0) + cap_final # donde (cap_final * tasa /100.0) son los intereses
		contador = contador +1
	print "\n capital final obtenido: " + str(cap_final)

#7) Haz un programa que pida el nombre de una persona y lo muestre en pantalla
#repetido 1000 veces, pero dejando un espacio de separación entre aparición y
#aparición del nombre.

def rep_nombre():
	name = raw_input("introduzca su nombre: ")
	
	contador = 1
	while contador <= 1000:
		print name + "\n"
		contador = contador + 1
	print contador

#8) Diseña un programa que lea un numero flotante por teclado y
#muestre por pantalla el mensaje El número es negativo solo si el
#número es menor que cero.

def verify_negative():
	numero = input("introduzca un numero: ")
	numero = float(numero)
	
	if numero < 0:
		print "el número es negativo"
	else:
		print "el numero no es negativo"

#9) Diseña un programa que lea la edad de dos personas y diga quien es mas
#joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la
#misma edad. En tal caso, hazlo saber con un mensaje adecuado

def lector_edad():
	edad1 = input("Edad de la persona 1: ")
	edad2 = input("Edad de la persona 2: ")
	
	if edad1 == edad2:
		print "Ambas personas tienen la misma edad"
	elif edad1 < edad2:
		print "la persona 1 es menor que la persona 2"
	else:
		print "la persona 1 es mayor que la persona 2"

#10) Diseña un programa que, dado un numero entero, determine si este es el
#doble de un numero impar. (Ejemplo: 14 es el doble de 7, que es impar.)

def doble_impar():
	numero = input("introduzca un numero entero: ")
	
	mitad = numero / 2.0 #de esta manera no tenemos resultados indeseados
	if (mitad % 2) == 1:
		print "el numero es el doble de un numero impar"
	else:
		print "el numero NO es el doble de un numero impar"

#verificar las funciones de los ejercicios:
#area_circulo()
#calculo_iva()
#expresiones()
#tipo_resultado()
#area_triangulo()
#intereses()
#rep_nombre()
#verify_negative()
#lector_edad()
doble_impar()
	

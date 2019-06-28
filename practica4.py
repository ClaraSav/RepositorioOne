# -*- coding: utf-8 -*-

#UNEFA-- Ingenieria de Sistemas nocturno
#Ejercicios de Lenguajes de Programación
#Alumna: Clara Savelli

#realizamos el diccionario con el codigo morse
morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd':'-..', 'e': '.', 'f': '..-.',
'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k':'-.-', 'l': '.-..', 'm': '--',
'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ': ' '}

#Desarrolle una función que reciba una tira que corresponde a letras tal que
#retorne el código morse respectivo. El código morse de cada letra debe estar
#separado por un espacio en blanco. Por ejemplo para “hola” retorna “…. —- .-.. .-“.

def letterToMorse(word):
	result = ''
	for letter in word:
		result += ' ' + morse[letter]
	print word + ': ' + result

#Desarrolle una función que reciba una tira que corresponde a una palabra en
#código morse, separadas las claves morse de cada letra por un espacio en
#blanco, tal que retorne la palabra respectiva. Por ejemplo para “-. .- -. .-”
#retorna “nana”. Piense en que tipo de diccionario debería de utilizar.

def morseToLetter(word):
	word2 = word
	result = ''
	
	#proseguimos solo si la palabra no es una cadena vacia
	while word != '':
		if ' ' in word:
			i = word.index(" ") #la letra es hasta donde está el primer espacio en blanco
		else:
			i = len(word) #si es una sola letra
			
		Letter = word[:i]
		
		for key, value in morse.items():
			if value == Letter:
				result += key
		word = word[i+1:]
	print word2 + ': ' + result
				
		
	

#desarrollando el menu
cont = True
while cont:
	option = 0
	sentence = ''
	print '\n*********Convertidor de codigo morse***********'
	print 'Opciones:\n'
	print '\t1. De letras a morse.'
	print '\t2. De morse a letras.'
	print '\t3. salir.'
	option = input("Opcion: ")
		
	if option == 1:
		sentence = raw_input("Ingrese la palabra: ")
		letterToMorse(sentence)
	elif option ==2:
		sentence = raw_input("Ingrese la palabra: ")
		morseToLetter(sentence)
	elif option == 3:
		cont = False
		break
	else:
		print "opcion invalida. Intente nuevamente"


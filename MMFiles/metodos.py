from MMFiles.clases import jugador	# Importamos la clase jugador
import pickle	# para poder guardar objetos en archivos, estiba los objetos(convierte a bytes)
import os 		# Manipular en consola
import random	

def jugar():
	continuar = "SI"	#  Variable para validar el ciclo
	digitos = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")	# Digitos validos para el codigo
	while continuar.upper() == "SI":
		os.system("cls")
		print("\t\t...::: YouMasterMind :::...")
		dificultad = int(input("\n\tSelecciona la dificultad del juego(1. Facil, 2. Dificil, 3. Ni lo intentes...nunca podras olvidarme): "))
		if dificultad == 1:
			cantDigitos = 3
		elif dificultad == 2:	# Validamos que nivel es para determinar el numero de digitos del codigo
			cantDigitos = 4
		elif dificultad == 3:
			cantDigitos = 5

		codigo = ""

		for i in range(cantDigitos):	# Ciclo para crear el codigo con los digitos correspondientes
			elegido = random.choice(digitos)	# Se selecciona aleatoriamente un digito de la tupla digitos()
			while elegido in codigo:	# Si el digito seleccionado ya habia sido seleccionado, se seleccion otro
				elegido = random.choice(digitos)
			codigo += elegido	# Se concatena el digito al codigo

		os.system("cls")
	
		print("\t\t...::: YouMasterMind :::...")
		print("\n\tTienes que adivinar un codigo de ", cantDigitos, " digitos distintos")
		propuesta = input("\n\tQue codigo propones?: ")

		intentos = 1

		while propuesta != codigo:	# Ciclo para validar si el codigo es correcto
			intentos += 1
			aciertos = 0
			coincidencias = 0
		
			for i in range(cantDigitos):
				if propuesta[i] == codigo[i]:	# Validamos si el digito esta en la misma posicion dentro del codigo
					aciertos += 1
				elif propuesta[i] in codigo:	# Validamos si el digito esta en el codigo
					coincidencias += 1
		
			print("\tTu codigo (", propuesta, ") tiene ", aciertos, " aciertos y ", coincidencias, " coincidencias")
			propuesta = input("\tIntenta con otro codigo: ")

		print("\n\tFelicidades!!!... Haz acertado el codigo en ", intentos, " intentos")

		scores = getRecords()	# Utilizamos la funcion para obtener los records

		if intentos < scores[cantDigitos - 3].getIntentos():	# Una vez acertado el codigo, se valida si los intentos son menores al record
			nombre = input("\n\tFelicidades!!!...Haz hecho un nuevo record, ingresa tu nombre: ")
			scores[cantDigitos - 3] = jugador(nombre, intentos)

			archivo = open("MMFiles/records", "wb")

			for i in scores:
				pickle.dump(i, archivo)	# Se sobreescribe el archivo con los nuevos records
										# Tambien podemos usar JSON, en lugar de pickle
			archivo.close()

		continuar = input("\n\tQuieres jugar de nuevo?(Si/No): ")

def instrucciones():
	os.system("cls")
	print("""
		...::: YouMasterMind :::...\n
	Al jugar YouMasterMind, pones a prueba tu mente y tu habilidad de razonar.
	Debes adivinar un codigo numerico generado aleatoriamente, YouMasterMind te ayuda al
	decirte cuantos numeros, del codigo que propusiste:
	- Acertaste: numero en su posicion correcta
	- Coincidencia: numero que esta en el codigo pero no en su posicion\n
	YouMasterMind cuenta con 3 niveles de dificultad, lo que hace que el codigo numerico
	tenga un mayor o menor numero de digitos:
	- Facil: 3 digitos
	- Dificl: 4 digitos
	- Extremo: 5 digitos
	""")
	jugarOSalir()

def jugarOSalir():
	while True:
		op = input("\tQuieres jugar?(Si/No): ")
		if op.upper() == "SI":
			jugar()
			break
		elif op.upper() == "NO":
			break
		else:
			print("\tSi o NO!!!")

def getRecords():	# Obtener los records y almacenar en una lista
	archivo = open("MMFiles/records", "rb")

	scores = []
	for i in range(3):
		scores.append(pickle.load(archivo))	# Load() (file.read) lee un objeto estibado

	archivo.close()

	return scores

def highScores():	# Funcion para mostrar los records
	records = ("Facil...", "Dificl...", "Extremo...")
	scores = getRecords()
	os.system("cls")
	print("\t\t...::: YouMasterMind :::...\n")

	for i in range(3):
		print("\t", records[i])
		print("\t\t", scores[i].getNombre(), "\t\t", scores[i].getIntentos(), " intentos")

	print()

	jugarOSalir()
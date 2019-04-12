import os
import MMFiles.metodos

opcion = 0
while opcion != 4:
	os.system("cls")
	print("\t\t...::: Bienvenido/a a YouMasterMind :::...")
	print("\n\t1. Jugar\n\t2. Como jugar¿?\n\t3. HighScores\n\t4. Salir")

	while True:		# Validamos si ocurre una Excepcion(error)
		try:
			opcion = int(input("\n\tElige una opción: "))
			break
		except ValueError:	# Este error
			print("\n\tNo es una opcion valida, intenta de nuevo!")

	if opcion == 1:
		MMFiles.metodos.jugar()
	elif opcion == 2:
		MMFiles.metodos.instrucciones()
	elif opcion == 3:
		MMFiles.metodos.highScores()

os.system("cls")
os.system("exit")
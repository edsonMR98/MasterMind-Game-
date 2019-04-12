class jugador:
	def __init__(self, n, i): # constructor para inicializar el nombre e intentos del objeto
		self.__nombre = n
		self.__intentos = i

	def getNombre(self):
		return self.__nombre

	def getIntentos(self):
		return self.__intentos
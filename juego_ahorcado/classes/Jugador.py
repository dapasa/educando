import getpass
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__palabra = ''
        self.__victorias = 0

    def set_palabra(self, palabra):
        while not palabra.isalpha():
                palabra = getpass.getpass("Por favor " + self.nombre + ", escribí tu palabra (debe contener solo letras y sin espacios): ")
        self.__palabra = palabra

    def set_victorias(self, victorias):
        self.__victorias = victorias
    
    def get_palabra(self):
        return self.__palabra
    
    def get_victorias(self):
        return self.__victorias
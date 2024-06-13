from classes.Jugador import Jugador

class Juego():
    def __init__(self, jugador_uno, jugador_dos):
        self.jugador_uno = Jugador(jugador_uno)
        self.jugador_dos = Jugador(jugador_dos)
        self.palabra_actual = ''
        self.turno = self.jugador_uno
        self.__ganador = None
    
    def jugar (self):
        palabra = ''
        if self.turno == self.jugador_uno:
            self.jugador_uno.set_palabra(palabra)
            palabra = self.jugador_uno.get_palabra()
            print("Ahora " + self.jugador_dos.nombre + ", te toca adivinar!! tenes hasta 3 intentos!:" )
            self.adivinar(palabra)
        else:
            self.jugador_dos.set_palabra(palabra)
            palabra = self.jugador_dos.get_palabra()

    def mostrar_progreso(self, palabra, palabra_oculta, letra):
        nueva_palabra_oculta = list(palabra_oculta)
        for i, char in enumerate(palabra):
            if char == letra:
                nueva_palabra_oculta[i] = letra
        return ''.join(nueva_palabra_oculta)

    def adivinar(self, palabra):
        palabra_oculta = '-' * len(palabra)
        intentos = 3
        letras_correctas = []

        print(palabra_oculta)
        while palabra_oculta != palabra and intentos > 0:
            letra = input("Elegí una letra: ")

            if letra in letras_correctas:
                print("Ya elegiste esa letra, proba con una nueva.")
                continue
            letras_correctas.append(letra)
            
            if letra in palabra:
                palabra_oculta = self.mostrar_progreso(palabra, palabra_oculta, letra)
                print("Bien! la letra '{}' está en la palabra".format(letra))
                print("palabra: ", palabra_oculta)
                print("\n\n")
            else:
                print("No, la letra '{}' no está en la palabra. Te quedan '{}' intenos.".format(letra, intentos - 1))
                print("\n\n")
                intentos -= 1

        if intentos == 0:
            print("Perdisteeeee, suerte para la próxima")
        else:
            print("Felicitaciones adivinaste!!!")
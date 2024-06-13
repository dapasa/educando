import classes.Menu as menu
from classes.Juego import Juego
jugando = True

while jugando:
    print("Seleccione una opción:")
    menu.menu()
    seleccion = input()
    
    if int(seleccion) == 1:
        print("Vamo a jugar")
        player_one = input("Ingrese el nombre del jugador 1: ")
        player_two = input("Ingrese el nombre del jugador 2: ")
        juego = Juego(player_one, player_two)
        juego.jugar()
    elif int(seleccion) == 2:
        print("Bye bye")
        jugando = False
    else:
        print("Opción no válida vuelva a intentar\n")

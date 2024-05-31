from getpass import getpass

def beggining_game():
    print("ingrese una palabra para comenzar el juego")
    word = getpass('')
    word_format = word.isalpha()
    if word_format == True:
        word = word.lower()
        count_word = (len (word))*'-' 
        print ('La palabra tiene ' + str(len(word)) + ' letras ' + 'ud tiene tres intentos ' + count_word)
        count = 3
        new_letter2 = []
        count_len = (len (word))
        for i in word:
            new_letter2.append('-')
        while count != 0 and count_len > 0:
            letter = str (input ("ingrese una letra:"))
            letter_format = letter.isalpha()
            if letter_format == True:
                if len(letter)>1:
                    print("escriba solo una letra")
                else:
                    letter = letter.lower()
                    if letter in word and letter not in new_letter2:
                        position = [position for position, dato in enumerate(word) if dato == letter]
                        if len (position) > 1:
                            count_len -= 1
                        for i in position:
                            new_letter2[i] = letter
                        count_len -= 1       
                        print (" la letra ingresada es correcta " + "vidas restantes " + str(count))             
                        print (new_letter2)
                    elif letter in new_letter2:
                        print("letra ya ingresada " + "vidas restantes " + str(count))
                    else:
                        count -= 1 
                        print (" la letra ingresada es NO correcta " + "vidas restantes " + str(count))                  
                        if count == 0:
                            print ("mala suerte la palabra era " + word)
                            break
            else:
                print(" solo se acepta palabras. No numeros, No simbolos , No espacios")
        else:
            print ("bravo acertaste la palabra, la cual era " + word)
    else:
        print(" solo se acepta palabras. No numeros, No simbolos , No espacios")

beggining_game()
while True:
    letter2 = str (input ("quiere volver a jugar "))
    letter2 = letter2.lower()
    if letter2 == "si":
        beggining_game()
    elif letter2 == "no":
        print("bye") 
        break
    else:
        print(" solo se acepta 'si' o 'no' como respuesta")






        


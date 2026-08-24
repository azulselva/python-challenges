def opcion_jugador(jugador_uno, jugador_dos):
    jugador_uno = int(jugador_uno)
    jugador_dos = int(jugador_dos)

    if jugador_uno == 1 and jugador_dos == 1:
        ganador = 0. 
        return ganador

    elif jugador_uno == 2 and jugador_dos == 2:
        ganador = 0
        return ganador

    elif jugador_uno == 3 and jugador_dos == 3:
        ganador = 0
        return ganador

    elif jugador_uno == 1 and jugador_dos == 2:
        ganador = 2
        return ganador

    elif jugador_uno == 1 and jugador_dos == 3:
        ganador = 1
        return ganador

    elif jugador_uno == 2 and jugador_dos == 1:
        ganador = 1
        return ganador
        
    elif jugador_uno == 2 and jugador_dos == 3:
        ganador = 2
        return ganador
    
    elif jugador_uno == 3 and jugador_dos == 1:
        ganador = 2
        return ganador
    
    elif jugador_uno == 0 and jugador_dos == 1:
         ganador = 2
         return ganador
        
    elif jugador_uno == 3 and jugador_dos == 2:
         ganador = 1
         return ganador 

def run():
    contador_one_player = 0
    contador_two_player = 0
        
    menu = ''' 
    Vamos jugar "Piedra, papel o tijera". Pueden participar dos jugadores.
    Cada jugador elije piedra papel o tijera, de acuerdo a los siguientes numerales:

    1. Si elije piedra
    2. Si elije papel
    3. Si elije tijera
    Gana el jugador que venza en dos de tres encuentros.'''

    print(menu)
    
    for i in range(3):
        jugador_uno = input('Ingresa la opción del jugador uno: ')
        jugador_dos = input('Ingresa la opción del jugador dos: ')

        ganador = opcion_jugador(jugador_uno, jugador_dos)

        if ganador == 0:
            print('Es un empate') 

        elif ganador == 1:
            contador_one_player = contador_one_player + 1
            print('El ganador es el jugador 1')
        
        else:
            contador_two_player =  contador_two_player + 1
            print('El ganador es el jugador 2') 

    if contador_one_player == 0 and contador_two_player == 0:
        print('''Es un empate. Puedes jugar otra ronda o buscar otra alternativa: 
        Tal grado de sincronización amerita una batalla cuerpo a cuerpo, o un matrimonio''')
    
    elif contador_one_player > contador_two_player:
        print('El ganador de la ronda es el jugador uno, con ' + str(contador_one_player) + ' puntos de 3 posibles.')
    
    else:
        print ('el ganador de la ronda es el jugador dos, con ' + str(contador_two_player) + ' puntos de tres posibles')

if __name__ == '__main__':
    run()
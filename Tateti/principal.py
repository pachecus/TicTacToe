tablero = ["-","-","-",
            "-","-","-",
            "-","-","-"]

def movimientos_legales(tablero):
    return [i for i, celda in enumerate(tablero) if celda == "-"]

def evaluar_tablero(tablero):
    combinaciones_gandoras = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
                             [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
                                [0, 4, 8], [2, 4, 6] 
                            ]
    for combinacion in combinaciones_gandoras:
        a, b, c = combinacion
        if tablero[a] == tablero[b] == tablero[c] != "-":
            if tablero[a] == "X":
                return 1 # gana el jugador
            else:
                return -1 # gana la maquina
            
    if "-" not in tablero:
        return 0
    
    return None

def minimax(tablero, profundidad, es_maximizando):
    resultado = evaluar_tablero(tablero)
    
    if resultado is not None:
        return resultado
    
    if es_maximizando:
        mejor_valor = -float("inf")
        for movimiento in movimientos_legales(tablero):
            tablero[movimiento] = "O"
            valor = minimax(tablero, profundidad + 1, False)
            tablero[movimiento] = "-"
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float("inf")
        for movimiento in movimientos_legales(tablero):
            tablero[movimiento] = "X"
            valor = minimax(tablero, profundidad + 1, True)
            tablero[movimiento] = "-"
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def mejor_movimiento(tablero):
    mejor_puntaje = -float("inf")
    mejor_mov = None
    for movimiento in movimientos_legales(tablero):
        tablero[movimiento] = "O"
        puntaje = minimax(tablero, 0, False)
        tablero[movimiento] = "-"
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_mov = movimiento
    return mejor_mov
    
def juego_terminado(tablero):
    return evaluar_tablero(tablero) is not None or "-" not in tablero

def imprimir_tablero(tablero):
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print("\n")

def jugar():
    tablero = ["-" for _ in range(9)]
    
    while not juego_terminado(tablero):
        imprimir_tablero(tablero)
        
        # Turno del jugador humano
        movimiento_valido = False
        while not movimiento_valido:
            movimiento = int(input("Ingresa tu movimiento (0-8): "))
            if movimiento in movimientos_legales(tablero):
                tablero[movimiento] = "X"
                movimiento_valido = True
            else:
                print("Movimiento inválido. Inténtalo de nuevo.")
        
        if juego_terminado(tablero):
            break
        
        # Turno de la IA
        movimiento_ia = mejor_movimiento(tablero)
        tablero[movimiento_ia] = "O"
    
    imprimir_tablero(tablero)
    
    resultado = evaluar_tablero(tablero)
    if resultado == 1:
        print("¡Ganaste!")
    elif resultado == -1:
        print("La IA ganó.")
    else:
        print("Empate.")

# Configuración
profundidad = 5  # Profundidad máxima para el algoritmo Minimax
jugar()  # Iniciar el juego





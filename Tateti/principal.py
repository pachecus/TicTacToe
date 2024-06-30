import os
import tkinter as tk
from tkinter import messagebox

def evaluar_tablero(tablero):
    combinaciones_ganadoras = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
                               [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
                               [0, 4, 8], [2, 4, 6]  # Diagonales
                               ]
    for combinacion in combinaciones_ganadoras:
        a, b, c = combinacion
        if tablero[a] == tablero[b] and tablero[a] == tablero[c] and tablero[a] != "-":
            if tablero[a] == "X":
                return 1  # gana el jugador
            else:
                return -1  # gana la máquina
    if "-" not in tablero:
        return 0  # empate
    return None  # el juego no termino


def movimientos_legales(tablero):
    return [i for i, celda in enumerate(tablero) if celda == "-"] # son las celdas que no tienen ni X ni O


def minimax(tablero, profundidad, es_maximizando): # algoritmo que evalua las posiciones posibles pero ligeramente modificado
    resultado = evaluar_tablero(tablero)
    
    if resultado is not None:
        return resultado * (profundidad_maxima - profundidad + 1)

    
    if profundidad >= profundidad_maxima:  # Si se alcanza la profundidad máxima
        return 0  # Retornar 0 porque no se sabe si es una situación ganadora o perdedora
    
    if es_maximizando:
        mejor_valor = float("inf")
        for movimiento in movimientos_legales(tablero):
            tablero[movimiento] = "O"
            valor = minimax(tablero, profundidad + 1, False)
            tablero[movimiento] = "-"
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor
    else:
        peor_valor = float("-inf")
        for movimiento in movimientos_legales(tablero):
            tablero[movimiento] = "X"
            valor = minimax(tablero, profundidad + 1, True)
            tablero[movimiento] = "-"
            peor_valor = max(peor_valor, valor)
        return peor_valor



def mejor_movimiento(tablero):
    mejor_puntaje = float("-inf")
    mejor_mov = None
    for movimiento in movimientos_legales(tablero):
        tablero[movimiento] = "O"
        puntaje = minimax(tablero, 0, False)
        tablero[movimiento] = "-"
        if mejor_puntaje == float("-inf"):
            mejor_puntaje = puntaje
            mejor_mov = movimiento
        elif puntaje < mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_mov = movimiento

    return mejor_mov



def juego_terminado(tablero):
    return evaluar_tablero(tablero) is not None or "-" not in tablero


def imprimir_tablero(tablero):
    os.system('cls')
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print("\n")


def jugar():
    tablero = ["-" for _ in range(9)]

    while not juego_terminado(tablero):
        imprimir_tablero(tablero)

        # Turno del jugador
        movimiento_valido = False
        while not movimiento_valido:
            movimiento = int(input("Ingresa tu movimiento (0-8): "))
            if tablero[movimiento] == "-":
                tablero[movimiento] = "X"
                movimiento_valido = True
            else:
                print("Movimiento inválido. Inténtalo de nuevo.")

        if juego_terminado(tablero):
            break

        # Turno de la maquina
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


profundidad_maxima = 9
jugar()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tarea2_2Algoritmogenético.py
------------
Tarea 2 - 2.Algoritmo genético
"""
__author__ = "ADLG & DJLP"

# isSafe comprueba si dos reinas estan en conflicto
def sinConflicto(matriz,f,c):

	# devuelve falso si dos reinas estan la misma columna
	for i in range(f):
		if matriz[i][c] == 'R':
			return False
	# devuelve falso si dos reina estan la misma fila
	(i,j) = (f,c)
	while i >= 0 and j >= 0:
		if matriz[i][j] == 'R':
			return False
		i = i - 1
		j = j - 1

	# devuelve falso si dos reinas estan en la misma diagonal
	(i,j) = (f,c)
	while i >= 0 and j < len(matriz):
		if matriz[i][j] == 'R':
			return False

		i = i - 1
		j = j + 1

	return True

# funcion que imprime todas las soluciones sin conflictos posibles
def printSolucion(matriz):
	for f in matriz:
		print(str(f).replace(',', '').replace('\'', ''))
	print()

def nReinas(matriz,f):

	# si las n reinas se posicionan con exito es decir sin conflictos entonces imrpime la solución
	if f == len(matriz):
		printSolucion(matriz)
		return

	for i in range(len(matriz)):
		if sinConflicto(matriz,f,i):
			matriz[f][i] = 'R' # si no hay dos reinas en conflicto entonces colocamos a la reina en la casilla catual
			                   # R significa reina
			nReinas(matriz,f+1) # lo hacemos para la siguiente fila
			matriz[f][i] = 'V' # retrocedemos y eliminamos a la reina de la casilla catual V sifnifica vacio

# numero de casillas pueden ser N
N = 8

matriz = [['V' for x in range(N)] for y in range(N)]

nReinas(matriz,0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tarea1-1.py
------------
Tarea 1 - 2. Agentes
"""
__author__ = "ADLG & DJLP"

import entornos_o
import doscuartos_o 
import random

"""
    Clase para un entorno de seis cuartos.
    El estado se define como (robot, A,B,C,D,E,F) donde robot puede tener los valores "A","B","C","D","E","F"
    Los cuartos pueden tener los valores "limpio", "sucio"
    Las acciones válidas en el entorno son ("Subir", "Bajar", "Ir_derecha", "Ir_izquierda", "Nada", "Limpiar").
"""
class SeisCuartos(entornos_o.Entorno):

	# Se inicializa al robot en el cuarto A con todos los cuartos sucios.
	def __init__(self, x0=["A", "sucio", "sucio", "sucio", "sucio", "sucio", "sucio"]):
		self.x = x0[:]
		self.desempeño = 0

	def accion_legal(self, accion):
		return accion in ("Subir", "Bajar", "Ir_derecha", "Ir_izquierda", "Nada", "Limpiar")

	def acciones_legales(self):
		posición, _ = self.percepción()
		if posición is "A" :
			return ("Ir_derecha","Bajar","Nada","Limpiar")
		elif posición is "B" :
			return ("Ir_derecha","Ir_izquierda","Nada","Limpiar")
		elif posición is "C":
			return ("Ir_izquierda","Bajar","Nada","Limpiar")
		elif posición is "D":
			return ("Ir_izquierda","Subir","Nada","Limpiar")
		elif posición is "E" :
			return ("Ir_derecha","Ir_izquierda","Nada","Limpiar")
		elif posición is "F" :
			return ("Ir_derecha","Subir","Nada","Limpiar")

	def transición(self, accion):
		if not self.accion_legal(accion):
			raise ValueError("La acción no es legal para este estado")

		robot, a,b,c,d,e,f = self.x
		if accion is not "Nada" or a is "sucio" or b is "sucio" or c is "sucio"or d is "sucio" or e is "sucio"or f is "sucio":
			if accion in ("Ir_derecha", "Ir_izquierda", "Limpiar"):
				self.desempeño -=1
			elif accion in ("Subir", "Bajar"):
				self.desempeño -=2
			else:
				self.desempeño *=1


		if accion is "Limpiar":
			self.x[" ABCDEF".find(self.x[0])] = "limpio"
		elif accion is "Ir_derecha":
			if robot is "A":
				self.x[0] = "B"
			elif robot is "B":
				self.x[0] = "C"
			elif robot is "F":
				self.x[0] = "E"
			elif robot is "E":
				self.x[0] = "D"
		elif accion is "Ir_izquierda":
			if robot is "C":
				self.x[0] = "B"
			elif robot is "B":
				self.x[0] = "A"
			elif robot is "D":
				self.x[0] = "E"
			elif robot is "E":
				self.x[0] = "F"
		elif accion is "Subir":
			if robot is "F":
				self.x[0] = "A"
			elif robot is "D":
				self.x[0] = "C"
		elif accion is "Bajar":
			if robot is "A":
				self.x[0] = "F"
			elif robot is "C":
				self.x[0] = "D"

	def percepción(self):
		return self.x[0], self.x[" ABCDEF".find(self.x[0])]


# Un agente que solo regresa una accion al azar entre las acciones legales.
class AgenteAleatorio(entornos_o.Agente):
	def __init__(self, entorno):
		self.entorno = entorno

	def programa(self, percepcion):
		return random.choice(self.entorno.acciones_legales())

# Un agente reactivo simple
class AgenteReactivoSimple(entornos_o.Agente):
	def programa(self, percepción):
		robot, situación = percepción
		return ('Limpiar' if situación == 'sucio' else 'Ir_derecha' if robot == 'B' else 'Bajar' if robot == 'C' else "Ir_izquierda" if robot == 'D' else "Ir_izquierda" if robot == 'E' else "Subir" if robot == 'F' else "Ir_derecha")

# Un agente reactivo basado en modelo
class AgenteReactivoModelo(entornos_o.Agente):
	def __init__(self):
		self.modelo = ["A", "sucio", "sucio", "sucio", "sucio", "sucio", "sucio"]

	def programa(self, percepción):
		robot, situación = percepción

		self.modelo[0] = robot
		self.modelo[' ABCDEF'.find(robot)] = situación

		a,b,c,d,e,f = self.modelo[1], self.modelo[2], self.modelo[3], self.modelo[4], self.modelo[5], self.modelo[6]
		if a == b == c == d == e == f == 'limpio':
			return 'Nada'
		elif situación == 'sucio':
			return 'Limpiar'
		elif robot == 'A':
			if b == 'sucio' or f == 'sucio':
				return 'Ir_derecha'
			else:
				return 'Bajar'
		elif robot == 'B':
			if c == 'sucio':
				return 'Ir_derecha'
			else:
				return 'Ir_izquierda'
		elif robot == 'C':
			if b == 'sucio' or d == 'sucio':
				return 'Bajar'
			else:
				return 'Ir_izquierda'
		elif robot == 'D':
			if c == 'sucio' or e == 'sucio':
				return 'Ir_izquierda'
			else:
				return 'Bajar'
		elif robot == 'E':
			if f == 'sucio':
				return 'Ir_izquierda'
			else:
				return 'Ir_derecha'
		elif robot == 'F':
			if a == 'sucio':
				return 'Subir'
			elif e == 'sucio':
				return 'Ir_derecha'

# test para el Agente aleatorio
def AgenteRandom():
	print("Prueba del entorno con un AGENTE ALEATORIO")
	entorno = SeisCuartos()
	entornos_o.simulador(entorno, AgenteAleatorio(entorno),100)
	
# test para el Agente Reactivo Simple
def AgenteReactSimple():
	print("Prueba del entorno con un AGENTE REACTIVO simple")
	entorno = SeisCuartos()
	entornos_o.simulador(entorno, AgenteReactivoSimple(),100)

# test para el Agente Reactivo con Modelo
def AgenteReactModelo():
	print("Prueba del entorno con un AGENTE REACTIVO con modelo")
	entorno = SeisCuartos()
	entornos_o.simulador(entorno, AgenteReactivoModelo(),100)

if __name__ == "__main__":
	AgenteRandom()
	AgenteReactSimple()
	AgenteReactModelo()
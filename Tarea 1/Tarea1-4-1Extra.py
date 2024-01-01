#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tarea1-4-1Extra.py
------------
Tarea 1 - 4.1 Punto extra
"""
__author__ = "ADLG & DJLP"

# Clase que representara una grafica/grafo.
class Grafo:

    def __init__(self, grafica=None, direccion=True):
        self.grafica = grafica or {}
        self.direccion = direccion
        if not direccion:
            self.creaGrafo()

    # Crea el grafo.
    def creaGrafo(self):
        for a in list(self.grafica.keys()):
            for (b, dist) in self.grafica[a].items():
                self.grafica.setdefault(b, {})[a] = dist

    # Relaciona dos puntos con una distancia.
    def conecta(self, A, B, distance=1):
        self.grafica.setdefault(A, {})[B] = distance
        if not self.direccion:
            self.grafica.setdefault(B, {})[A] = distance

    # Obtiene los vecinos de un vecino.
    def get(self, a, b=None):
        aristas = self.grafica.setdefault(a, {})
        if b is None:
            return aristas
        else:
            return aristas.get(b)

    # Regresa una lsita de nodos en la grafica.
    def nodos(self):
        s1 = set([k for k in self.grafica.keys()])
        s2 = set([k2 for v in self.grafica.values() for k2, v2 in v.items()])
        nodos = s1.union(s2)
        return list(nodos)

# Clase que representara un nodo.
class Nodo:

    def __init__(self, name:str, padre:str):
        self.name = name
        self.padre = padre
        self.distanciaI = 0 
        self.distanciaD = 0 
        self.km = 0 

    #Metodos que comparan, ordenan e imprimen nodos.
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.km < other.km
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

# Best-first Search Primero el Mejor.
def BFSPM(grafo, heuristica, inicio, destino):
    
    open = []
    closed = []
    nodoInicial = Nodo(inicio, None)
    nodoDestino = Nodo(destino, None)
    open.append(nodoInicial)
    
    while len(open) > 0:
        open.sort()
        nodoActual = open.pop(0)
        closed.append(nodoActual)
        
        if nodoActual == nodoDestino:
            recorrido = []
            while nodoActual != nodoInicial:
                recorrido.append(nodoActual.name + ': ' + str(nodoActual.distanciaI)+' m')
                nodoActual = nodoActual.padre
            print("Ruta encontrada:")
            recorrido.append(nodoInicial.name + ': ' + str(nodoInicial.distanciaI)+' m')
            return recorrido[::-1]
        vecinos = grafo.get(nodoActual.name)
        for key, value in vecinos.items():
            vecino = Nodo(key, nodoActual)
            if(vecino in closed):
                continue
            vecino.distanciaI = nodoActual.distanciaI + grafo.get(nodoActual.name, vecino.name)
            vecino.distanciaD = heuristica.get(vecino.name)
            vecino.km = vecino.distanciaD
            if(agregaVecino(open, vecino) == True):
                open.append(vecino)
    return None

# valida si se debe de agregar un vecino a la lista.
def agregaVecino(open, vecino):
    for nodo in open:
        if (vecino == nodo and vecino.km >= nodo.km):
            return False
    return True

def main():

    graph = Grafo()
    # Distancias entre ciudades y vias.

    graph.conecta('Tijuana', 'Tecate', 66.71)
    graph.conecta('Nogales', 'Nacozari', 277.60)
    graph.conecta('Mexicali', 'Nogales', 535.20)
    graph.conecta('Mexicali', 'Manzanillo', 2023.66)
    graph.conecta('Mexicali', 'Lázaro Cárdenas', 2284.46 )
    graph.conecta('Mexicali', 'CDMX', 2370.71 )
    graph.conecta('Mexicali', 'Gómez palacios', 2626.53 )
    graph.conecta('Gómez Palacios', 'Ciudad Juárez', 3333.37 )
    graph.conecta('Gómez Palacios', 'iedras Negras', 3402.12 )
    graph.conecta('Gómez Palacios', 'Tampico', 3421.80)
    graph.conecta('Gómez Palacios', 'Manzanillo', 1078.43 )
    graph.conecta('Gómez Palacios', 'Lázaro Cárdenas', 902.27)
    graph.conecta('Gómez Palacios', 'CDMX', 896.67)
    graph.conecta('Piedras Negras', 'CDMX', 1228.09 )
    graph.conecta('Piedras Negras', 'Tampico', 1035.10 )
    graph.conecta('Topolobampo', 'Ojinada', 703.78)
    graph.conecta('Durango', 'Gómez Palacios', 238.96 )
    graph.conecta('Durango', 'Piedras Negras', 894.40)
    graph.conecta('Nuevo Laredo', 'Matamoros', 616.36)
    graph.conecta('Nuevo Laredo', 'Puerto Altamira', 1042.41 )
    graph.conecta('Nuevo Laredo', 'CDMX', 1143.71 )
    graph.conecta('Nuevo Laredo', 'Xalapa', 1400.82 )
    graph.conecta('Nuevo Laredo', 'Lázaro Cárdenas', 1608.28)
    graph.conecta('CDMX', 'Puebla', 177.70 )
    graph.conecta('Puebla', 'Oaxaca', 267.06)
    graph.conecta('CDMX', 'Puebla', 103.16 )
    graph.conecta('Puebla', 'Coatzacoalcos', 563.24)
    graph.conecta('Puebla', 'Santa Cruz', 542.71)
    graph.conecta('Santa Cruz', 'Coatzacoalcos', 183.49 )
    graph.conecta('Ciudad Hidalgo', 'Coatzacoalcos', 515.68  )
    graph.conecta('Coatzacoalcos', 'Valladolid', 996.50)

    graph.creaGrafo()

    heuristica = {}
    heuristica['Mexicali'] = 2641.94
    heuristica['Nogales'] = 2235.60
    heuristica['Nacozari'] = 2055.85
    heuristica['Ciudad Juárez'] = 1974.06
    heuristica['Ojinada'] = 1742.82
    heuristica['Topolobampo'] = 1759.12
    heuristica['Piedras Negras'] = 1526.44
    heuristica['Gómez Palacios'] = 1343.10
    heuristica['Durango'] = 1279.11
    heuristica['Manzanillo'] = 997.71
    heuristica['Lázaro Cárdenas'] = 793.81
    heuristica['CDMX'] = 536.69
    heuristica['Nuevo Laredo'] = 1256.60
    heuristica['Matamoros'] = 1037.34
    heuristica['Puerto Altamira'] = 787.10
    heuristica['Tampico'] = 680.45
    heuristica['Xalapa'] = 438.05
    heuristica['Puebla'] = 418.94
    heuristica['Oaxaca'] = 204.11
    heuristica['Coatzacoalcos'] = 239.14
    heuristica['Ciudad Hidalgo'] = 342.50
    heuristica['Valladolid'] = 956.93
    heuristica['Santa Cruz'] = 0 

    ruta = BFSPM(graph, heuristica, 'Piedras Negras', 'Santa Cruz')
    print(ruta)

if __name__ == "__main__":
    main()
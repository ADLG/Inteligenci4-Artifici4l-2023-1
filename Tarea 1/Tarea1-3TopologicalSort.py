#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tarea1-3TopologicalSort.py
------------
Tarea 1 - 3. Búsqueda ciega
"""
__author__ = "ADLG & DJLP"

# Para doder implementar este metodo debemos saber que aristas se quian cuando eliminamos un Nodos
# por lo que este metodo resta una unidad a los ingrados de cada arista a la que estaba conectada
# Por ejemplo en la grafica de la tarea si eliminamos B como tiene aristas a E y C entonces les restamos una
# unidad a los ingrados de E y C

def eliminaAristas(c,lista):
    if c == 'A':
        lista[2] = lista[2] -1;
        lista[3] = lista[3] -1;
    elif c == 'B':
        lista[2] = lista[2] -1;
        lista[4] = lista[4] -1;
    elif c == 'C':
        lista[3] = lista[3] -1;
    elif c == 'E':
        lista[0] = lista[0] -1;
        lista[2] = lista[2] -1;

    return lista


def topologicalSorts():
    #Creando grafo
    A = ['A','B','C','D','E'] #Nodos del grafo
    A_pesos = [1,0,3,2,1] #Ingrados de cada nodo el primero corresponde a A y asi sucesivamente
    R = [] #Lista donde se guardaran los nodos visitados

    while len(R) < 5:
        n = A_pesos.index(0)
        R.append(A[n]); #Agregammos el nodo con ingrado 0 a la lista R
        A_pesos[n] = -1; #Modificamos los ingrados 0 por -1 como si los eliminaramos esto equivale a eliminar el nodo visitado
        A_pesos = eliminaAristas(A[n],A_pesos); #eliminamos las aristas y actualizamos los ingrados de cada nodo

    for l in R:
        print(l);

print("Este es el orden en que visitamos los nodos de la gráfica siendo el de hasta arriba el primero que visitamos,")
print("y el de hasta abajo el ultimo que visitamos");
topologicalSorts();

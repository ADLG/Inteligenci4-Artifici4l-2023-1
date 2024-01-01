#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tarea1-4-Aestrella-BusquedaInformada.py
------------
Tarea 1 - 4.2 Busqueda Informada A*
"""
__author__ = "ADLG & DJLP"

from collections import deque

class Grafica:
    def __init__(self, ad_lis):
        self.ad_lis = ad_lis

    def get_vecinos(self, v):
        return self.ad_lis[v]

    # Valores de la funcion heuristica h(n) de la distancia en linea recta calculada con Lineas Metro
    def h(self, n):
        H = {
        'Coyoacan': 5750,
        'Zapata': 4530,
        'Hospital 20 de Noviembre': 4770,
        'Insurgentes sur': 2640,
        'Mixcoac': 5660,
        'San Antonio': 5000,
        'San Pedro de los Pinos': 4660,
        'Tacubaya': 4450,
        'Patriotismo': 3570,
        'Chilpancingo': 2480,
        'Centro Medico': 1140,
        'Division del norte': 3340,
        'Eugenia': 1140,
        'Etiopia': 1740,
        'Parque de los venados': 4260,
        'Eje Central': 5100,
        'Ermita': 5020,
        'Portales': 4150,
        'Nativitas': 3100,
        'Villa Cortes': 2250,
        'Xola': 1510,
        'Viaducto': 1080,
        'Chabacano': 960,
        'Lazaro Cardenas': 0
        }

        return H[n]

        #Algoritmo estrellla (A*)
    def algoritmo_a_estrella(self, start, stop):

        abrir_lst = set([start])
        cerrar_lst = set([])
        poo = {}
        poo[start] = 0
        par = {}
        par[start] = start

        while len(abrir_lst) > 0:
            n = None
            for v in abrir_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
            if n == None:
                print('No existe la ruta')
                return None
            if n == stop:
                reconst_ruta = []
                while par[n] != n:
                    reconst_ruta.append(n)
                    n = par[n]

                reconst_ruta.append(start)
                reconst_ruta.reverse()
                print('Ruta encontrada: {}'.format(reconst_ruta))
                return reconst_ruta

            for (m, peso) in self.get_vecinos(n):
                if m not in abrir_lst and m not in cerrar_lst:
                    abrir_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + peso
                else:
                    if poo[m] > poo[n] + peso:
                        poo[m] = poo[n] + peso
                        par[m] = n
                        if m in cerrar_lst:
                            cerrar_lst.remove(m)
                            abrir_lst.add(m)

            abrir_lst.remove(n)
            cerrar_lst.add(n)

        print('No existe la ruta')
        return None

# Creando la grafica con sus vecinos de cada nodo y los pesos de cada arista.
# Para este ejercicio no utilizamos todos los nodos de la grafica del metro si no una subgrafica
# La cual es
#                                coyoacan
#                                   | 1153
#                                   v
#                                 Zapata
#                             450/    | 794    \ 563
#                               v     v        v
#                           H20 Nov   Div N    Par. d Venados
#                          725 |       |             | 1280
#                              v       v             v
#                            Insur    Eugenia     Eje Central
#                          651 |       |              | 895
#                              v       v              v
#                            Mixco    Etiopia      Ermita
#                          788 |       |              | 748
#                              v       v              v
#                            San Ant  Centro Me    Portales
#                          606 |       |              | 924
#                              v       |              v
#                          S.P.Pinos   |            Nativitas
#                         1084 |       |              | 750
#                              v       |              v
#                           Tacubaya   |            Villa Cortes
#                         1133 |       |              | 698
#                              v       |              v
#                          Ptriotimo   |            Xola
#                          955 |       |              | 490
#                              v       |              v
#                       Chilpancingo   |            Viaducto
#                                \     |              | 774
#                                \     |              v
#                                \     |            Chabacano
#                                \     |            /
#                                \     |           /
#                                v     v          v
#                                 Lazaro Cardenas
ad_lis = {
    'Coyoacan': [('Zapata', 1153)],
    'Zapata': [('Hospital 20 de Noviembre', 450), ('Division del norte',794), ('Parque de los venados',563)],
    'Hospital 20 de Noviembre': [('Insurgentes sur', 725)],
    'Insurgentes sur': [('Mixcoac', 651)],
    'Mixcoac': [('San Antonio', 788)],
    'San Antonio': [('San Pedro de los Pinos', 606)],
    'San Pedro de los Pinos': [('Tacubaya', 1084)],
    'Tacubaya': [('Patriotismo', 1133)],
    'Patriotismo': [('Chilpancingo', 955)],
    'Chilpancingo': [('Centro Medico', 1152)],
    'Centro Medico': [('Lazaro Cardenas', 1059)],
    'Division del norte': [('Eugenia', 715)],
    'Eugenia': [('Etiopia', 950)],
    'Etiopia': [('Centro Medico', 1119)],
    'Parque de los venados': [('Eje Central', 1280)],
    'Eje Central': [('Ermita', 895)],
    'Ermita': [('Portales', 748)],
    'Portales': [('Nativitas', 924)],
    'Nativitas': [('Villa Cortes', 750)],
    'Villa Cortes': [('Xola', 698)],
    'Xola': [('Viaducto', 490)],
    'Viaducto': [('Chabacano', 774)],
    'Chabacano': [('Lazaro Cardenas', 1000)]
}
grafica1 = Grafica(ad_lis) # INicializamos la grafica con ad_list que es la grafica creada anteriormente
grafica1.algoritmo_a_estrella('Coyoacan', 'Lazaro Cardenas') #Ruta a buscar de coyoacan a Lazaro Cardenas con A*

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tarea2_3Estrategiasevolutivas.py
------------
Tarea 2 - 3.ESTRATEGIAS EVOLUTIVAS
"""
__author__ = "ADLG & DJLP"

import numpy as np
import random

class Informacion:
    def __init__(self, modelo, mutacionPorcentaje, n_individuos, n_seleccion, n_generaciones, b1 = True):
        self.modelo = modelo
        self.mutacionPorcentaje = mutacionPorcentaje
        self.n_individuos = n_individuos
        self.n_seleccion = n_seleccion
        self.n_generaciones = n_generaciones
        self.b1 = b1

    def crear_individuo(self):
        MaterialA = [100,435,58,430]
        MaterialB = [184,415,50,439]
        MaterialC = [96,501,82,520]
        MaterialD = [68,300,15,263]
        NumMateriales = np.random.randint(2,5)

        if NumMateriales == 2:
            M1 = np.random.randint(1,5)
            # print(M1)
            M2 = np.random.randint(1,5)
            if (M1 == M2):
                while (M1 == M2):
                    M2 = np.random.randint(1,5)
            # print(M2)
            
            if(M1 == 1):
                N1 = np.random.randint(1,21)
                N2 = np.random.randint(1,7)
                N1=N1*.01
                N2=N2*.1
            if(M2 == 1): 
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,21)
                N1=N1*.1
                N2=N2*.01
            else:
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,7)
                N1=N1*.1
                N2=N2*.1
            # print(N1)
            # print(N2)
            if M1 == 1:
                L1 = [n * N1 for n in MaterialA]
            elif M1 == 2:
                L1 = [n * N1 for n in MaterialB]
            elif M1 == 3:
                L1 = [n * N1 for n in MaterialC]
            else:
                L1 = [n * N1 for n in MaterialD]

            if M2 == 1:
                L2 = [n * N2 for n in MaterialA]
            elif M2 == 2:
                L2 = [n * N2 for n in MaterialB]
            elif M2 == 3:
                L2 = [n * N2 for n in MaterialC]
            else:
                L2 = [n * N2 for n in MaterialD]

            resultado = list(map(lambda x,y: x+y, L1, L2))
            # print(L1)
            # print(L2)
            # print(Resultado)
            return resultado

        if NumMateriales == 3:
            M1 = np.random.randint(1,5)
            M2 = np.random.randint(1,5)
            if (M1 == M2):
                while (M1 == M2):
                    M2 = np.random.randint(1,5)
            M3 = np.random.randint(1,5)
            if (M3 == M1) or (M3 == M2):
                while (M3 == M1) or (M3 == M2):
                    M3 = np.random.randint(1,5)

            if(M1 == 1):
                N1 = np.random.randint(1,21)
                N2 = np.random.randint(1,7)
                N3 = np.random.randint(1,7)
                N1=N1*.01
                N2=N2*.1
                N3=N3*.1
            if(M2 == 1): 
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,21)
                N3 = np.random.randint(1,7)
                N1=N1*.1
                N2=N2*.01
                N3=N3*.1
            if(M3 == 1): 
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,7)
                N3 = np.random.randint(1,21)
                N1=N1*.1
                N2=N2*.1
                N3=N3*.01
            else:
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,7)
                N3 = np.random.randint(1,7)
                N1=N1*.1
                N2=N2*.1
                N3=N3*.1

            if M1 == 1:
                L1 = [n * N1 for n in MaterialA]
            elif M1 == 2:
                L1 = [n * N1 for n in MaterialB]
            elif M1 == 3:
                L1 = [n * N1 for n in MaterialC]
            else:
                L1 = [n * N1 for n in MaterialD]

            if M2 == 1:
                L2 = [n * N2 for n in MaterialA]
            elif M2 == 2:
                L2 = [n * N2 for n in MaterialB]
            elif M2 == 3:
                L2 = [n * N2 for n in MaterialC]
            else:
                L2 = [n * N2 for n in MaterialD]

            if M3 == 1:
                L3 = [n * N3 for n in MaterialA]
            elif M3 == 2:
                L3 = [n * N3 for n in MaterialB]
            elif M3 == 3:
                L3 = [n * N3 for n in MaterialC]
            else:
                L3 = [n * N3 for n in MaterialD]

            resultado = list(map(lambda x,y,z: x+y+z, L1, L2, L3))
            return resultado
        else:
            M1 = np.random.randint(1,5)
            M2 = np.random.randint(1,5)
            if (M1 == M2):
                while (M1 == M2):
                    M2 = np.random.randint(1,5)
            M3 = np.random.randint(1,5)
            if (M3 == M1) or (M3 == M2):
                while (M3 == M1) or (M3 == M2):
                    M3 = np.random.randint(1,5)
            M4 = np.random.randint(1,5)
            if (M4 == M1) or (M4 == M2) or (M4 == M3):
                while (M4 == M1) or (M4 == M2) or (M4 == M3):
                    M4 = np.random.randint(1,5)

            if(M1 == 1):
                N1 = np.random.randint(1,21)
                N2 = np.random.randint(1,7)            
                N3 = np.random.randint(1,7)
                N4 = np.random.randint(1,7)
                N1=N1*.01
                N2=N2*.1
                N3=N3*.1
                N4=N4*.1
            if(M2 == 1): 
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,21)            
                N3 = np.random.randint(1,7)
                N4 = np.random.randint(1,7)
                N1=N1*.1
                N2=N2*.01
                N3=N3*.1
                N4=N4*.1
            if(M3 == 1): 
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,7)            
                N3 = np.random.randint(1,21)
                N4 = np.random.randint(1,7)
                N1=N1*.1
                N2=N2*.1
                N3=N3*.01
                N4=N4*.1
            else:
                N1 = np.random.randint(1,7)
                N2 = np.random.randint(1,7)            
                N3 = np.random.randint(1,7)
                N4 = np.random.randint(1,21)
                N1=N1*.1
                N2=N2*.1
                N3=N3*.1
                N4=N4*.01

            if M1 == 1:
                L1 = [n * N1 for n in MaterialA]
            elif M1 == 2:
                L1 = [n * N1 for n in MaterialB]
            elif M1 == 3:
                L1 = [n * N1 for n in MaterialC]
            else:
                L1 = [n * N1 for n in MaterialD]

            if M2 == 1:
                L2 = [n * N2 for n in MaterialA]
            elif M2 == 2:
                L2 = [n * N2 for n in MaterialB]
            elif M2 == 3:
                L2 = [n * N2 for n in MaterialC]
            else:
                L2 = [n * N2 for n in MaterialD]

            if M3 == 1:
                L3 = [n * N3 for n in MaterialA]
            elif M3 == 2:
                L3 = [n * N3 for n in MaterialB]
            elif M3 == 3:
                L3 = [n * N3 for n in MaterialC]
            else:
                L3 = [n * N3 for n in MaterialD]

            if M4 == 1:
                L4 = [n * N4 for n in MaterialA]
            elif M4 == 2:
                L4 = [n * N4 for n in MaterialB]
            elif M4 == 3:
                L4 = [n * N4 for n in MaterialC]
            else:
                L4 = [n * N4 for n in MaterialD]

            resultado = list(map(lambda v,x,y,z: v+x+y+z, L1, L2, L3, L4))
            return resultado


    def crear_poblacion(self):
        return [self.crear_individuo() for _ in range(self.n_individuos)]

    def fitness(self, indiv):
        fitness = 0

        for i in range(len(indiv)):
            if indiv[i] == self.modelo[i]:
                fitness += 1
        
        return fitness
    
    def seleccion(self, poblacion):

        s = [(self.fitness(i), i) for i in poblacion]
        s = [i[1] for i in sorted(s)]

        return s[len(s)-self.n_seleccion:]
    
    def reproduccion(self, poblacion, seleccion):

        punto = 0
        padre = []

        for i in range(len(poblacion)):
            punto = np.random.randint(1, len(self.modelo) - 1)
            padre = random.sample(seleccion, 2)

            poblacion[i][:punto] = padre[0][:punto]
            poblacion[i][punto:] = padre[1][punto:]
        
        return poblacion
    
    def mutacion(self, poblacion):
        
        for i in range(len(poblacion)):
            if random.random() <= self.mutacionPorcentaje:
                punto = np.random.randint(len(self.modelo))
                if (punto == 2):
                    while (punto == 2):
                        punto = np.random.randint(len(self.modelo))
                nuevoValorandom = np.random.randint(1, 100)

                while nuevoValorandom == poblacion[i][punto]:
                    nuevoValorandom = np.random.randint(1, 100)
                
                poblacion[i][punto] = nuevoValorandom
            return poblacion
    
    def EE_11_EE(self):
        poblacion = self.crear_poblacion()

        print("\n3.ESTRATEGIAS EVOLUTIVAS\n\nLas listas representan las Aleaciones generadas con la Estrategia Evolutiva (1+1)-EE, por lo que sus valores y las posiciones son representados asi: [[Costo,Dureza,Peso,Disipación de calor],[Costo,Dureza,Peso,Disipación de calor],[Costo,Dureza,Peso,Disipación de calor] ...]")
        for i in range(self.n_generaciones):

            if self.b1:
                print('*********')
                print('Generacion: ', i)
                print('Aleaciones:', poblacion)
                print('*********')

            selected = self.seleccion(poblacion)
            poblacion = self.reproduccion(poblacion, selected)
            poblacion = self.mutacion(poblacion)

def main():
    aleacionModelo = [101.2, 428.79999999999995, 48.7, 417.4]
    modelo = Informacion(
        modelo = aleacionModelo,
        mutacionPorcentaje = 0.5,
        n_individuos = 10,
        n_seleccion = 4,
        n_generaciones = 20,
        b1=True)
    modelo.EE_11_EE()

if __name__ == '__main__':
    main()
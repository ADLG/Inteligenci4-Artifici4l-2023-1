#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tarea1-4-BFS-BusquedaInformada.py
------------
Tarea 1 - 4.2 Busqueda Informada Best-First Search
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

    # Metodos que comparan, ordenan e imprimen nodos.
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
    # Distancias entre estaciones de cada linea:

    # Linea 1.
    graph.conecta('Pantitlán', 'Zaragoza', 1320)
    graph.conecta('Zaragoza', 'Gómez Farías', 762)
    graph.conecta('Gómez Farías', 'Boulevard Puerto Aéreo', 611)
    graph.conecta('Boulevard Puerto Aéreo', 'Balbuena', 595)
    graph.conecta('Balbuena', 'Moctezuma', 703)
    graph.conecta('Moctezuma', 'San Lázaro', 478)
    graph.conecta('San Lázaro', 'Candelaria', 866)
    graph.conecta('Candelaria', 'Merced', 698)
    graph.conecta('Merced', 'Pino Suárez', 745)
    graph.conecta('Pino Suárez', 'Isabel la Católica', 382)
    graph.conecta('Isabel la Católica', 'Salto del Agua', 445)
    graph.conecta('Salto del Agua', 'Balderas', 458)
    graph.conecta('Balderas', 'Cuauhtémoc', 409)
    graph.conecta('Cuauhtémoc', 'Insurgentes', 793)
    graph.conecta('Insurgentes', 'Sevilla', 645)
    graph.conecta('Sevilla', 'Chapultepec', 501)
    graph.conecta('Chapultepec', 'Juanacatlán', 973)
    graph.conecta('Juanacatlán', 'Tacubaya', 1158)
    graph.conecta('Tacubaya', 'Observatorio', 1262)

    # Linea 2
    graph.conecta('Cuatro Caminos', 'Panteones', 1639)
    graph.conecta('Panteones', 'Tacuba', 1416)
    graph.conecta('Tacuba', 'Cuitláhuac', 637)
    graph.conecta('Cuitláhuac', 'Popotla', 620)
    graph.conecta('Popotla', 'Colegio Militar', 462)
    graph.conecta('Colegio Militar', 'Normal', 516)
    graph.conecta('Normal', 'San Cosme', 657)
    graph.conecta('San Cosme', 'Revolución', 537)
    graph.conecta('Revolución', 'Hidalgo', 587)
    graph.conecta('Hidalgo', 'Bellas Artes', 447)
    graph.conecta('Bellas Artes', 'Allende', 387)
    graph.conecta('Allende', 'Zócalo', 602)
    graph.conecta('Zócalo', 'Pino Suárez', 745)
    graph.conecta('Pino Suárez', 'San Antonio Abad', 817)
    graph.conecta('San Antonio Abad', 'Chabacano', 642)
    graph.conecta('Chabacano', 'Viaducto', 774)
    graph.conecta('Viaducto', 'Xola', 490)
    graph.conecta('Xola', 'Villa de Cortés', 698)
    graph.conecta('Villa de Cortés', 'Nativitas', 750)
    graph.conecta('Nativitas', 'Portales', 924)
    graph.conecta('Portales', 'Ermita', 748)
    graph.conecta('Ermita', 'General Anaya', 838)
    graph.conecta('General Anaya', 'Tasqueña', 1330)

    # Linea 3
    graph.conecta('Indios Verdes', 'Deportivo 18 de Marzo', 1166)
    graph.conecta('Deportivo 18 de Marzo', 'Potrero', 966)
    graph.conecta('Potrero', 'La Raza', 1106)
    graph.conecta('La Raza', 'Tlatelolco', 1445)
    graph.conecta('Tlatelolco', 'Guerrero', 1042)
    graph.conecta('Guerrero', 'Hidalgo', 702)
    graph.conecta('Hidalgo', 'Juárez', 251)
    graph.conecta('Juárez', 'Balderas', 659)
    graph.conecta('Balderas', 'Niños Héroes', 665)
    graph.conecta('Niños Héroes', 'Hospital General', 559)
    graph.conecta('Hospital General', 'Centro Médico', 653)
    graph.conecta('Centro Médico', 'Etiopía/Plaza de la Transparencia', 1119)
    graph.conecta('Etiopía/Plaza de la Transparencia', 'Eugenia', 950)
    graph.conecta('Eugenia', 'División del Norte', 715)
    graph.conecta('División del Norte', 'Zapata', 794)
    graph.conecta('Zapata', 'Coyoacán', 1153)
    graph.conecta('Coyoacán', 'Viveros/Derechos Humanos', 908)
    graph.conecta('Viveros/Derechos Humanos', 'Miguel Ángel de Quevedo', 824)
    graph.conecta('Miguel Ángel de Quevedo', 'Copilco', 1295)
    graph.conecta('Copilco', 'Universidad', 1306)

    # Linea 4
    graph.conecta('Santa Anita', 'Jamaica', 758)
    graph.conecta('Jamaica', 'Fray Servando', 1033)
    graph.conecta('Fray Servando', 'Candelaria', 633)
    graph.conecta('Candelaria', 'Morelos', 1062)
    graph.conecta('Morelos', 'Canal del Norte', 910)
    graph.conecta('Canal del Norte', 'Consulado', 884)
    graph.conecta('Consulado', 'Bondojito', 645)
    graph.conecta('Bondojito', 'Talismán', 959)
    graph.conecta('Talismán', 'Martín Carrera', 1129)

    # Linea 5    
    graph.conecta('Politécnico', 'Instituto del Petróleo', 1188)
    graph.conecta('Instituto del Petróleo', 'Autobuses del Norte', 1067)
    graph.conecta('Autobuses del Norte', 'La Raza', 975)
    graph.conecta('La Raza', 'Misterios', 892)
    graph.conecta('Misterios', 'Valle Gómez', 969)
    graph.conecta('Valle Gómez', 'Consulado', 679)
    graph.conecta('Consulado', 'Eduardo Molina', 815)
    graph.conecta('Eduardo Molina', 'Aragón', 860)
    graph.conecta('Aragón', 'Oceanía', 1219)
    graph.conecta('Oceanía', 'Terminal Aérea', 1174)
    graph.conecta('Terminal Aérea', 'Hangares', 1153)
    graph.conecta('Hangares', 'Pantitlán', 1644)

    # Linea 6
    graph.conecta('El Rosario', 'Tezozómoc', 1257)
    graph.conecta('Tezozómoc', 'Azcapotzalco', 973)
    graph.conecta('Azcapotzalco', 'Ferrería', 1173)
    graph.conecta('Ferrería', 'Norte 45', 1072)
    graph.conecta('Norte 45', 'Vallejo', 660)
    graph.conecta('Vallejo', 'Instituto del Petróleo', 755)
    graph.conecta('Instituto del Petróleo', 'Lindavista', 1258)
    graph.conecta('Lindavista', 'Deportivo 18 de Marzo', 1075)
    graph.conecta('Deportivo 18 de Marzo', 'La Villa – Basílica', 570)
    graph.conecta('La Villa – Basílica', 'Martín Carrera', 1141)

    # Linea 7
    graph.conecta('El Rosario', 'Aquíles Serdán', 1615)
    graph.conecta('Aquíles Serdán', 'Camarones', 1402)
    graph.conecta('Camarones', 'Refinería', 952)
    graph.conecta('Refinería', 'Tacuba', 1295)
    graph.conecta('Tacuba', 'San Joaquín', 1433)
    graph.conecta('San Joaquín', 'Polanco', 1163)
    graph.conecta('Polanco', 'Auditorio', 812)
    graph.conecta('Auditorio', 'Constituyentes', 1430)
    graph.conecta('Constituyentes', 'Tacubaya', 1005)
    graph.conecta('Tacubaya', 'San Pedro de los Pinos', 1084)
    graph.conecta('San Pedro de los Pinos', 'San Antonio', 606)
    graph.conecta('San Antonio', 'Mixcoac', 788)
    graph.conecta('Mixcoac', 'Barranca del Muerto', 1476)

    # Linea 8
    graph.conecta('Garibaldi', 'Bellas Artes', 634)
    graph.conecta('Bellas Artes', 'San Juan de Letrán', 456)
    graph.conecta('San Juan de Letrán', 'Salto del Agua', 292)
    graph.conecta('Salto del Agua', 'Doctores', 564)
    graph.conecta('Doctores', 'Obrera', 761)
    graph.conecta('Obrera', 'Chabacano', 1143)
    graph.conecta('Chabacano', 'La Viga', 843)
    graph.conecta('La Viga', 'Santa Anita', 633)
    graph.conecta('Santa Anita', 'Coyuya', 968)
    graph.conecta('Coyuya', 'Iztacalco', 993)
    graph.conecta('Iztacalco', 'Apatlaco', 910)
    graph.conecta('Apatlaco', 'Aculco', 534)
    graph.conecta('Aculco', 'Escuadrón 201', 789)
    graph.conecta('Escuadrón 201', 'Atlalilco', 1738)
    graph.conecta('Atlalilco', 'Iztapalapa', 732)
    graph.conecta('Iztapalapa', 'Cerro de la Estrella', 717)
    graph.conecta('Cerro de la Estrella', 'UAM I', 1135)
    graph.conecta('UAM I', 'Constitución de 1917', 1137)

    # Linea 9
    graph.conecta('Pantitlán', 'Puebla', 1380)
    graph.conecta('Puebla', 'Ciudad Deportiva', 800)
    graph.conecta('Ciudad Deportiva', 'Velódromo', 1110)
    graph.conecta('Velódromo', 'Mixiuhca', 821)
    graph.conecta('Mixiuhca', 'Jamaica', 942)
    graph.conecta('Jamaica', 'Chabacano', 1031)
    graph.conecta('Chabacano', 'Lázaro Cardenas', 1000)
    graph.conecta('Lázaro Cardenas', 'Centro Médico', 1059)
    graph.conecta('Centro Médico', 'Chilpancingo', 1152)
    graph.conecta('Chilpancingo', 'Patriotismo', 955)
    graph.conecta('Patriotismo', 'Tacubaya', 1133)

    # Linea A
    graph.conecta('Pantitlán', 'Agrícola Oriental', 1409)
    graph.conecta('Agrícola Oriental', 'Canal de San Juan', 1093)
    graph.conecta('Canal de San Juan', 'Tepalcates', 1456)
    graph.conecta('Tepalcates', 'Guelatao', 1161)
    graph.conecta('Guelatao', 'Peñón Viejo', 2206)
    graph.conecta('Peñón Viejo', 'Acatitla', 1379)
    graph.conecta('Acatitla', 'Santa Marta', 1100)
    graph.conecta('Santa Marta', 'Los Reyes', 1783)
    graph.conecta('Los Reyes', 'La Paz', 1956)

    # Linea B
    graph.conecta('Ciudad Azteca', 'Plaza Aragón', 574)
    graph.conecta('Plaza Aragón', 'Olímpica', 709)
    graph.conecta('Olímpica', 'Ecatepec', 596)
    graph.conecta('Ecatepec', 'Múzquiz', 1485)
    graph.conecta('Múzquiz', 'Río de los Remedios', 1155)
    graph.conecta('Río de los Remedios', 'Impulsora', 436)
    graph.conecta('Impulsora', 'Nezahualcóyotl', 1393)
    graph.conecta('Nezahualcóyotl', 'Villa de Aragón', 1335)
    graph.conecta('Villa de Aragón', 'Bosques de Aragón', 784)
    graph.conecta('Bosques de Aragón', 'Deportivo Oceanía', 1165)
    graph.conecta('Deportivo Oceanía', 'Oceanía', 863)
    graph.conecta('Oceanía', 'Romero Rubio', 809)
    graph.conecta('Romero Rubio', 'Ricardo Flores Magón', 908)
    graph.conecta('Ricardo Flores Magón', 'San Lázaro', 907)
    graph.conecta('San Lázaro', 'Morelos', 1296)
    graph.conecta('Morelos', 'Tepito', 498)
    graph.conecta('Tepito', 'Lagunilla', 611)
    graph.conecta('Lagunilla', 'Garibaldi', 474)
    graph.conecta('Garibaldi', 'Guerrero', 757)
    graph.conecta('Guerrero', 'Buenavista', 521)

    # Linea 12
    graph.conecta('Tláhuac', 'Tlaltenco', 1298)
    graph.conecta('Tlaltenco', 'Zapotitlán', 1115)
    graph.conecta('Zapotitlán', 'Nopalera', 1276)
    graph.conecta('Nopalera', 'Olivos', 1360)
    graph.conecta('Olivos', 'Tezonco', 490)
    graph.conecta('Tezonco', 'Periférico Oriente', 1545)
    graph.conecta('Periférico Oriente', 'Calle 11', 1111)
    graph.conecta('Calle 11', 'Lomas Estrella', 906)
    graph.conecta('Lomas Estrella', 'San Andrés Tomatlán', 1060)
    graph.conecta('San Andrés Tomatlán', 'Culhuacán', 990)
    graph.conecta('Culhuacán', 'Atlalilco', 1671)
    graph.conecta('Atlalilco', 'Mexicaltzingo', 1922)
    graph.conecta('Mexicaltzingo', 'Ermita', 1805)
    graph.conecta('Ermita', 'Eje Central', 895)
    graph.conecta('Eje Central', 'Parque de los Venados', 1280)
    graph.conecta('Parque de los Venados', 'Zapata', 563)
    graph.conecta('Zapata', 'Hospital 20 de Noviembre', 450)
    graph.conecta('Hospital 20 de Noviembre', 'Insurgentes Sur', 725)
    graph.conecta('Insurgentes Sur', 'Mixcoac', 651)

    # graph.conecta('Pantitlán', 'Zaragoza', 1320)
    # graph.conecta('Atlalilco', 'Mexicaltzingo', 1922)

    graph.creaGrafo()

    heuristica = {}
    heuristica['Pantitlán'] = 7.44
    heuristica['Zaragoza'] = 6.53
    heuristica['Gómez Farías'] = 5.80 
    heuristica['Boulevard Puerto Aéreo'] = 5.27 
    heuristica['Balbuena'] = 4.76 
    heuristica['Moctezuma'] = 4.25 
    heuristica['San Lázaro'] = 4.15
    heuristica['Candelaria'] = 3.49 
    heuristica['Merced'] = 2.87 
    heuristica['Pino Suárez'] = 2.41 
    heuristica['Isabel la Católica'] = 2.25 
    heuristica['Salto del Agua'] = 2.24 
    heuristica['Balderas'] = 2.27 
    heuristica['Cuauhtémoc'] = 2.30 
    heuristica['Insurgentes'] = 2.65 
    heuristica['Sevilla'] = 3.19 
    heuristica['Chapultepec'] = 3.70 
    heuristica['Juanacatlán'] = 3.96 
    heuristica['Tacubaya'] = 4.53 
    heuristica['Cuatro Caminos'] = 9.47 
    heuristica['Panteones'] = 8.38 
    heuristica['Tacuba'] = 7.33 
    heuristica['Cuitláhuac'] = 6.76 
    heuristica['Popotla'] = 6.02 
    heuristica['Colegio Militar'] = 5.47 
    heuristica['Normal'] = 4.80 
    heuristica['San Cosme'] = 4.20 
    heuristica['Revolución'] = 3.70 
    heuristica['Hidalgo'] = 3.38 
    heuristica['Bellas Artes'] = 3.18 
    heuristica['Allende'] = 3.25 
    heuristica['Zócalo'] = 3.09 
    heuristica['San Antonio Abad'] = 1.43 
    heuristica['Chabacano'] = .969
    heuristica['Viaducto'] = 1.07 
    heuristica['Xola'] = 1.51 
    heuristica['Villa de Cortés'] = 2.26 
    heuristica['Nativitas'] = 3.11 
    heuristica['Portales'] = 4.18 
    heuristica['Ermita'] = 5.14 
    heuristica['General Anaya'] = 5.98 
    heuristica['Indios Verdes'] = 10.08 
    heuristica['Deportivo 18 de Marzo'] = 8.89 
    heuristica['Potrero'] = 7.90 
    heuristica['Tlatelolco'] = 5.32 
    heuristica['Guerrero'] = 4.17 
    heuristica['Juárez'] = 2.92 
    heuristica['Niños Héroes'] = 1.49 
    heuristica['Hospital General'] = 1.16 
    heuristica['Centro Médico'] = 1.11 
    heuristica['Etiopía/Plaza de la Transparencia'] = 1.74 
    heuristica['Eugenia'] = 2.68 
    heuristica['División del Norte'] = 3.49 
    heuristica['Zapata'] = 4.60 
    heuristica['Coyoacán'] = 5.80
    heuristica['Viveros/Derechos Humanos'] = 6.74
    heuristica['Miguel Ángel de Quevedo'] = 7.80
    heuristica['Copilco'] = 8.61
    heuristica['Santa Anita'] = 2.54 
    heuristica['Jamaica'] = 2.44 
    heuristica['Fray Servando'] = 2.99
    heuristica['Morelos'] = 4.55
    heuristica['Canal del Norte'] = 5.52 
    heuristica['Consulado'] = 6.51 
    heuristica['Bondojito'] = 7.28 
    heuristica['Talismán'] = 8.40 
    heuristica['Politécnico'] = 10.40 
    heuristica['Instituto del Petróleo'] = 9.13 
    heuristica['Autobuses del Norte'] = 7.98 
    heuristica['La Raza'] = 7.00 
    heuristica['Misterios'] = 6.40 
    heuristica['Valle Gómez'] = 6.32 
    heuristica['Eduardo Molina'] = 6.42 
    heuristica['Aragón'] = 7.06 
    heuristica['Oceanía'] = 7.37 
    heuristica['Terminal Aérea'] = 6.65 
    heuristica['Hangares'] = 6.21 
    heuristica['El Rosario'] = 11.97 
    heuristica['Tezozómoc'] = 11.14 
    heuristica['Azcapotzalco'] = 10.28 
    heuristica['Ferrería'] = 9.79 
    heuristica['Norte 45'] = 9.28 
    heuristica['Vallejo'] = 9.26 
    heuristica['Lindavista'] = 9.04 
    heuristica['La Villa – Basílica'] = 8.73 
    heuristica['Aquíles Serdán'] = 10.68 
    heuristica['Camarones'] = 9.28 
    heuristica['Refinería'] = 8.41 
    heuristica['San Joaquín'] = 6.49 
    heuristica['Polanco'] = 5.71 
    heuristica['Auditorio'] = 5.34 
    heuristica['Constituyentes'] = 4.93 
    heuristica['San Pedro de los Pinos'] = 4.66 
    heuristica['San Antonio'] = 5.05 
    heuristica['Mixcoac'] = 5.70 
    heuristica['Garibaldi'] = 4.12 
    heuristica['San Juan de Letrán'] = 2.73 
    heuristica['Doctores'] = 1.61 
    heuristica['Obrera'] = .667 
    heuristica['La Viga'] = 1.92 
    heuristica['Coyuya'] = 3.42 
    heuristica['Iztacalco'] = 3.98 
    heuristica['Apatlaco'] = 4.86 
    heuristica['Aculco'] = 5.42 
    heuristica['Escuadrón 201'] = 6.02 
    heuristica['Atlalilco'] = 7.24 
    heuristica['Iztapalapa'] = 7.70 
    heuristica['Cerro de la Estrella'] = 8.41 
    heuristica['UAM I'] = 9.63 
    heuristica['Puebla'] = 6.51 
    heuristica['Ciudad Deportiva'] = 5.59 
    heuristica['Velódromo'] = 4.35 
    heuristica['Mixiuhca'] = 3.30 
    heuristica['Lázaro Cardenas'] = 0
    heuristica['Chilpancingo'] = 2.51 
    heuristica['Patriotismo'] = 3.60 
    heuristica['Agrícola Oriental'] = 7.87 
    heuristica['Canal de San Juan'] = 8.99 
    heuristica['Tepalcates'] = 10.47 
    heuristica['Guelatao'] = 11.69 
    heuristica['Peñón Viejo'] = 13.89 
    heuristica['Acatitla'] = 15.33 
    heuristica['Santa Marta'] = 16.52 
    heuristica['Los Reyes'] = 18.39 
    heuristica['Ciudad Azteca'] = 18.75 
    heuristica['Plaza Aragón'] = 18.05 
    heuristica['Olímpica'] = 17.24 
    heuristica['Ecatepec'] = 16.58 
    heuristica['Múzquiz'] = 15.00 
    heuristica['Río de los Remedios'] = 13.87 
    heuristica['Impulsora'] = 13.28 
    heuristica['Nezahualcóyotl'] = 11.92 
    heuristica['Villa de Aragón'] = 10.63 
    heuristica['Bosques de Aragón'] = 9.72 
    heuristica['Deportivo Oceanía'] = 8.41 
    heuristica['Romero Rubio'] = 6.48
    heuristica['Ricardo Flores Magón'] = 5.39 
    heuristica['Tepito'] = 4.51 
    heuristica['Lagunilla'] = 4.23 
    heuristica['Tláhuac'] = 19.22 
    heuristica['Tlaltenco'] = 17.82 
    heuristica['Zapotitlán'] = 16.89 
    heuristica['Nopalera'] = 15.76 
    heuristica['Olivos'] = 14.52 
    heuristica['Tezonco'] = 13.98 
    heuristica['Periférico Oriente'] = 12.39 
    heuristica['Calle 11'] = 11.44 
    heuristica['Lomas Estrella'] = 10.76 
    heuristica['San Andrés Tomatlán'] = 9.75 
    heuristica['Culhuacán'] = 8.67 
    heuristica['Mexicaltzingo'] = 5.95 
    heuristica['Eje Central'] = 5.15 
    heuristica['Parque de los Venados'] = 4.32 
    heuristica['Hospital 20 de Noviembre'] = 4.83 
    heuristica['Insurgentes Sur'] = 5.18 

    ruta = BFSPM(graph, heuristica, 'Coyoacán', 'Lázaro Cardenas')
    print(ruta)

if __name__ == "__main__":
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tarea2_4.3Shanon
"""
__author__ = "ADLG & DJLP"

import math

def shannon(info):
    pila = {}
    simbolo = {}

    for c in info:
        pila[c] = round(info.count(c) / len(info), 5)
        simbolo[c] = info.count(c)
    print("\nFrecuencias de aparición de símbolos:\n")
    for symb in pila:
        print("{0} --> {1} -- {2}".format(symb, pila[symb], simbolo[symb]))
    return frecuencia(pila)


def frecuencia(simbolo):
    bit_set = [round(simbolo[symb] * math.log2(simbolo[symb]), 5) for symb in simbolo]
    entropia = -1 * (round(sum(bit_set), 5))
    return entropia


if __name__ == "__main__":
    mensaje = input("\nIngrese el mensaje: ")
    bits = shannon(mensaje)
    print("\nH(X) = {0} bits. Redondeado a {1} bits/simbolos, ".format(bits, round(bits)))
    print("Tomara {0} bits codificar '{1}'".format(len(mensaje) * round(bits), mensaje))
    print("\nEntropia de: %.5f" % (bits / len(mensaje)))
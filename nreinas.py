#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nreinas.py
------------

Ejemplo de las n_reinas con búsquedas locales

"""

__author__ = 'juliowaissman'


import blocales
import time
from random import shuffle
from random import sample
from itertools import combinations


class ProblemaNreinas(blocales.Problema):
    """
    Las N reinas en forma de búsqueda local se inicializa como

    entorno = ProblemaNreinas(n) donde n es el número de reinas a colocar

    Por default son las clásicas 8 reinas.

    """
    def __init__(self, n=8):
        self.n = n

    def estado_aleatorio(self):
        estado = list(range(self.n))
        shuffle(estado)
        return tuple(estado)

    @staticmethod
    def swap(x, i, j):
        """
        Intercambia los elemento i y j de la lista x

        """
        if not isinstance(x, type([1, 2])):
            raise TypeError("Este método solo se puede hacer con listas")
        x[i], x[j] = x[j], x[i]

    def vecinos(self, estado):
        """
        Generador vecinos de un estado, todas las 2 permutaciones

        @param estado: una tupla que describe un estado.

        @return: un generador de estados vecinos.

        """
        x = list(estado)
        for i, j in combinations(range(self.n), 2):
            self.swap(x, i, j)
            yield tuple(x)
            self.swap(x, i, j)

    def vecino_aleatorio(self, estado):
        """
        Genera un vecino de un estado intercambiando dos posiciones
        en forma aleatoria.

        @param estado: Una tupla que describe un estado

        @return: Una tupla con un estado vecino.

        """
        vecino = list(estado)
        i, j = sample(range(self.n), 2)
        self.swap(vecino, i, j)
        return tuple(vecino)

    def costo(self, estado):
        """
        Calcula el costo de un estado por el número de conflictos entre reinas

        @param estado: Una tupla que describe un estado

        @return: Un valor numérico, mientras más pequeño, mejor es el estado.

        """
        return sum((1 for (i, j) in combinations(range(self.n), 2)
                    if abs(estado[i] - estado[j]) == abs(i - j)))


def prueba_descenso_colinas(problema=ProblemaNreinas(8), repeticiones=10):
    """ Prueba el algoritmo de descenso de colinas con n repeticiones """

    print("\n\n" + "intento".center(10) +
          "estado".center(60) + "costo".center(10))
    for intento in range(repeticiones):
        solucion = blocales.descenso_colinas(problema)
        print(str(intento).center(10) +
              str(solucion).center(60) +
              str(problema.costo(solucion)).center(10))


def prueba_temple_simulado(problema=ProblemaNreinas(8)):
    """ Prueba el algoritmo de temple simulado """

    solucion = blocales.temple_simulado(problema)
    print("\n\nTemple simulado con calendarización To/(1 + i).")
    print("Costo de la solución: ", problema.costo(solucion))
    print("Y la solución es: ")
    print(solucion)

def prueba_temple_simulado_2(problema=ProblemaNreinas(8), calendarización=None):
    """ Prueba el algoritmo de temple simulado """

    solucion = blocales.temple_simulado(problema, calendarización)
    if calendarización is None: 
        print("\n\nTemple simulado con calendarización To/(1 + i).")
    elif calendarización is "Logaritmo":
        print("\n\nTemple simulado con calendarización T_ini/(1 + i*log(i)).")
    elif calendarización is "Exponencial":
        print("\n\nTemple simulado con calendarización T_ini * exp(-tol*i).")

    print("Costo de la solución: ", problema.costo(solucion))
    print("Y la solución es: ")
    print(solucion)

if __name__ == "__main__":
    
    t_inicial = time.time()
    prueba_descenso_colinas(ProblemaNreinas(64), 10)
    t_final = time.time()
    print("Tiempo de ejecución en segundos: {}".format(t_final - t_inicial))

    t_inicial = time.time()
    prueba_temple_simulado(ProblemaNreinas(64))
    t_final = time.time()
    print("Tiempo de ejecución en segundos: {}".format(t_final - t_inicial))

    t_inicial = time.time()
    prueba_temple_simulado_2(ProblemaNreinas(64), "Logaritmo")
    t_final = time.time()
    print("Tiempo de ejecución en segundos: {}".format(t_final - t_inicial))

    t_inicial = time.time()
    prueba_temple_simulado_2(ProblemaNreinas(64), "Exponencial")
    t_final = time.time()
    print("Tiempo de ejecución en segundos: {}".format(t_final - t_inicial))

    ##########################################################################
    #                          20 PUNTOS
    ##########################################################################
    #
    # ¿Cual es el máximo número de reinas que se puede resolver en
    # tiempo aceptable con el método de 10 reinicios aleatorios?
    #   El máximo número de reinas que se puede resolver en un
    #   tiempo aceptable (3 minuto con 40 segundos) es de n = 64.
    #
    # ¿Que valores para ajustar el temple simulado son los que mejor
    # resultado dan? ¿Cual es el mejor ajuste para el temple simulado
    # y hasta cuantas reinas puede resolver en un tiempo aceptable?
    #   La tolerancia que se esta utilizando parece ser adecuada
	#   ya que probando con diferentes valores para la tolerancia con 32 reinas y siempre se obtenia
    #   costo 0 con tol=0.001 y de manera rapido.
    #   
    #   En general para obtener mejores resultados del temple simulado,
    #   es necesario probar diferentes metdos de
    #   calendarización, prueba al menos otros dos métodos sencillos de
    #   calendarización y ajusta los parámetros para que funcionen de la
    #   mejor manera
    #
    #   El mejor calendarizador resulto ser el logaritmico y tardó aproximadamente 6 segundos con
    #   64 reinas. El exponencial tardó 8.6 segundos con 64 reinas.
    #
    # ------ IMPLEMENTA AQUI TU CÓDIGO ---------------------------------------



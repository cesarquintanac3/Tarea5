#!/usr/bin/ python
# encoding: UTF-8

import sys
import codecs
import math
import numpy as np
"""
Módulo que contiene la función para calcular el Chi².
Autores: María M. Ariza Acero y  César A. Quintana Cataño
Fecha de creación: Oct  9 23:08:53 COT 2013
"""


def calcular_chi(teoricos, reales): 

    """
    Calcula el Chi².
    
    Input: 
    -teoricos: arreglo, tipo float, que contiene los valores esperados
    -reales: arreglo, tipo float, que contiene los valores medidos 
    Output: valor de Chi²
    """
    n=len(teoricos)

    #Arreglo para guardar la resta en cada punto
    restas=np.zeros(n) 
    
    #Arreglo para guardar el resultado de la resta elevado al cuadrado 
    restas_2=np.zeros(n)  
 
    #Variable para guardar la suma de las restas elevadas al cuadrado
    suma=0 
 
    #Ciclo para calcular las restas 
    for i in range(n): 
        restas[i]=teoricos[i]-reales[i] 
        restas_2[i]=pow(restas[i],2) 

    #Ciclo para calcular la suma de las restas
    for i in range(n): 
        suma=suma+restas_2[i] 

    #Calculo del chi²
    chi_2=suma/n 
 
    return chi_2 
 

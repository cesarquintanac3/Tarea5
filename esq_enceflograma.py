#!/usr/bin/ python
# encoding: UTF-8

import sys
import codecs
import math
#import module_chi2 as mchi2

"""
Módulo que contiene la función para calcular el Chi².
Autores: María M. Ariza Acero y  César A. Quintana Cataño
Fecha de creación: Oct  9 23:57:25 COT 2013
"""


def cargar(datafile):

    """
    Lee el archivo con los datos de los electrodos en el encefalograma.

    Input: archivo de datos

    Output: arreglo con las líneas del archivo
    """

    data = np.loadtxt('archivoDeDatos')

    return data

def guardardatos(data):

    """
    Organiza los datos del archivo de entrada en arreglos para cada electrodo
    Input: el arreglo con los datos a organizar
    Output: un arreglo que contiene los arreglos con los datos de cada electrodo
    """

    #Arreglo que guarda los arreglos con la información de cada electrodo
    electrodos=[]

    #Ciclo para crear el arreglo dentro del arreglo para cada electrodo
    for i in range(len(data)):

        electrodos.append([])

    #Ciclo para guardar la información en cada arreglo
    for j in data:

        for i in range(len(electrodos)):

            (electrodos[i]).append(j[i])

def elementosFourier(data,periodo):

    """
    Halla la transformada de fourier de unos datos de entrada y la distribución de frecuencias asociada a esta.

    Input: rreglo con n datos.
    Output: dos arreglos: uno con los coeficientes de la expresión de la transformada de fourier en términos de números complejos y el segundo con la distribución de frecuencias asociada.
    """

    fft_data= data
    fft_freq= data

    return fft_data, fft_freq


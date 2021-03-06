#!/usr/bin/ python
# encoding: UTF-8

import sys
import codecs
import math
import numpy as np
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

    data = np.loadtxt(datafile)

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

        electrodos.append(data[i])

    #Ciclo para guardar la información en cada arreglo
    #for j in data:

       # for i in range(len(electrodos)):

        #    (electrodos[i]).append(j[i])

    return electrodos

def elementosFourier(data):

    """
    Halla la transformada de fourier de unos datos de entrada y la distribución de frecuencias asociada a esta.

    Input: arreglo con n datos
    Output: dos arreglos: uno con los coeficientes de la expresión de la transformada de fourier en términos de números complejos y el segundo con la distribución de frecuencias asociada.
    """
    
    fft_data= data
    fft_freq= data

    return fft_data, fft_freq

def LimpiarPuntos(fft_data, fft_freq):
    """
    Toma los diez puntos con mayor amplitud en su coeficiente de fourier asociado y los conserva, el resto las envía a cero y, a partir de la distribución una distribución de frecuencias, aplica la inversa de fourier para hallar una nueva distribucion de puntos.
    Input:Dos arreglos, uno con frecuencias en cada una de sus posiciones y otro con sus amplitudes asociadas.
    Output: nueva distribucion de puntos.
    """

    AmplitudesLimpias = fft_data
    puntosNuevos =np.ones(498)

    return puntosNuevos


def Graficas(fft_freqs,potencias,tiempo, puntosNuevos):

    """
    Genera todas las graficas requeridas por el programa:

    (1)Espectro de potencias para cada electrodo
    (2)gráfica de la señal en función del tiempo de los electrodos luego del proceso de filtrado para cada electrodo

    Input: 
    para (1): potencias y fft_freqs (arreglos con los productos de las funciones elementosFourier y potencias)
    para (2): puntosNuevos y tiempo (dis arreglos, uno con los productos de LimpiarPuntos y otro con el tiempo para un electrodo) 

    Output: graficas

    """

    return 

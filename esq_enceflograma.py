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
   Para un arreglo de frecuencias frecuencias(parametro) mayores a (1/20)(1/agnos) y menores a (1/2)(1/agnos) toma sus amplitudes correspondientes (parametro) y las vuelve cero. Luego a partir de los nuevos datos de frecuencias y amplitudes, y el uso de la transformada inversa de Fourier, retorna una nueva distribucion de datos.
    Input:Dos arreglos, uno con frecuencias en cada una de sus posiciones y otro con sus amplitudes asociadas.
    Output: nueva distribucion de puntos.
    """

    AmplitudesLimpias = fft_data
    puntosNuevos =np.ones(498)

    return puntosNuevos


def Graficas(fft_freqI,potenciasI,puntosNuevosI,fft_freqII,potenciasII,puntosNuevosII,fft_freqIII,potenciasIII,puntosNuevosIII,puntos, acumuladoMeses):

    """
    Genera todas las graficas requeridas por el programa:

    (1)Espectro de potencias que surge de la interpolacion constante
    (2)Espectro de potencias que surge de la interpolacion lineal
    (3)Espectro de potencias que surge de la interpolacion cubica
    (4)Comparacion puntos pre y post limpimpieza por interpolacion constante
    (5)Comparacion puntos pre y post limpimpieza por interpolacion lineal
    (6)Comparacion puntos pre y post limpimpieza por interpolacion cubica
   
    Input: 
    para (1): freqI y potenciasI
    para (2): freqII y potenciasII 
    para (3): freqIII y potenciasIII 
    para (4): puntosNuevosI, puntos y acumuladoMeses 
    para (5): puntosNuevosII, puntos y acumuladoMeses 
    para (6): puntosNuevosIII, puntos y acumuladoMeses 

    Output: graficas

    """

    return 

def estimarPeriodo(tiempo,puntos):
    """
    A partir de una distribucion de puntos que genera un patron periodico estima el periodo de la funcion.

    Input: Contiene dos arreglos; el primero es la variable independiente tiempo y el segundo es su distribucion asociada (en nuestro caso sera de numero de manchas solares)
    Output: La funcion devolvera un periodo estimado para el sistema

    """

    periodo= 100

    return periodo

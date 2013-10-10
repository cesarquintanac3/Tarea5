#!/usr/bin/ python
# encoding: UTF-8

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

"""
Definicion de las funciones a utilizar para procesar los datos en la funcion principal.
Presentado por María Margarita Ariza Acero (201124649) y César Augusto Quintana Catano (201125995)
Fecha de creación: 9 de octubre del 2013
"""

def cargar(archivoDeDatos):
    
    """
    Lee el archivo con los datos de manchas solares. 
    
    Input: archivo con los siguientes datos:
    
    Columna 1: agno
    Comluna 2: mes
    columna 3: dias de toma de datos
    columna 4: numero de manchas

    Output: Un arreglo donde en cada posición se encuentran los datos de una fila del archivo que entro como parametro.
    """
    # !head -n 498 archivoDeDatos
    data = np.loadtxt(archivoDeDatos)
    
    return data

def arreglarDatos(data):

    """
    La siguiente funcion separa los datos en arreglos distintos excluyendo los meses donde no se tomaron datos y arreglando un vector acumuladoMeses donde se guardan los meses acumulados donde se tomaron datos (evitando asi la perdida de informacion)

    Input:  Un arreglo donde en cada posicion se encuentran los datos de una fila del archivo con la informacion de las manchas solares. 

    Output: cuatro arreglos, uno para los agnos, el acumulado de los meses, el numero de manchas solares y el intervalo de medicion.

    """

    manchas=np.ones(498)
    acumuladoMeses=np.ones(498)
    intervaloMedicion=np.ones(498)
    year=np.ones(498)
    
    return manchas,acumuladoMeses,intervaloMedicion,year

def interpolacion(puntosx,puntosy,puntosz):

    """
    Interpola los datos de acumuladoMeses y manchas de tres maneras: constante, lineal y cubica.

    Input: puntos a tomar de cada funcion de interpolacion. 
    Output: Devuelve tres arreglos, cada uno con la evaluacion de los puntos parametro en la funcion de interpolacion
    """

    InterpolacionConsatante=np.ones(498) 
    InterpolacionLineal=np.ones(498)
    InterpolacionCubica=np.ones(498)
    
    return InterpolacionConsatante, InterpolacionLineal, InterpolacionCubica

def elementosFourier (datos):
    """
    Halla la transformada de fourier de unos datos de entrada y la distribucion de frecuencias asociada a esta.

    Input: Arreglo con n datos.
    Output: dos arreglos; uno con los coeficientes de la expresion de la transformada de fourier en terminos de numeros complejos y el segundo con la distribucion de frecuencias asociada.

    """

    fft_data= datos
    fft_freq= datos

    return fft_data, fft_freq

def Potencias(fft_data):

    """
    Toma una distribucion de numeros complejos, halla su norma y la eleva al cuadrado para proseguir mas adelante (en otra funcion) con el desarrollo de un espectro de potencias.

    input: Array con m numeros complejos.
    Output: Un array con m escalares representando la norma al cuadrado de los datos que entraron como parametro.
    """

    potencias= fft_data

    return potencias

def LimpiarPuntos(fft_data, fft_freq):
    """
   Para un arreglo de frecuencias frecuencias(parametro) mayores a (1/20)(1/agnos) y menores a (1/2)(1/agnos) toma sus amplitudes correspondientes (parametro) y las vuelve cero. Luego a partir de los nuevos datos de frecuencias y amplitudes, y el uso de la transformada inversa de fourier, retorna una nueva distribucion de datos.
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

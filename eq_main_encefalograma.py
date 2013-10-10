#!/usr/bin/ python
# encoding: UTF-8

import sys
import numpy as np
import potencias as pot 
import module_chi2 as mchi2
import esq_encefalograma as fcn

"""
Módulo que contiene la función para calcular el Chi².
Autores: María M. Ariza Acero y  César A. Quintana Cataño
Fecha de creación: Oct  10 12:05:25 COT 2013
"""
def main():

    """
    Toma los datos de cada electrodo durante la realización de un encefalograma y a partir de stos se hace un análisis de datos representado en gŕaficas
    """

    #Archivo de entrada
    ArchivoEntrada= 'encefalograma.dat'

    #Carga y organiza los datos
    datos = fcn.cargar(ArchivoEntrada)
    encefalograma=fcn.guardardatos(datos)

    #Arreglo de arregloa para los coeficientes de Fourier
    fft_data=np.ones(24)

    #Arreglo de arreglos para las frecuecnias 
    fft_freq=np.ones(24)

    #Arreglo con los minutos
    tiempo=arrange(1,400)

    #Aplica la transformada de Fourier    
    for i in range(len(encefalograma)):
        
        fft_data[i],fft_freq[i]=fcn.elementosFourier(encefalograma[i])
    
    #Espectro de potencias 
    potencias=np.ones(24)

    for i in range(len(fft_data)):
         """
        Calcula el espectro depotencias para cada arreglo producto de Fourier usando la función en el modulo de Potencias.
        """
        potencias[i]=pot.espectro_potencias(fft_data[i],fft_frecuencias[i])
       
    #Arreglo con los datos después de ser filtrados
        
    puntosNuevos=np.ones(24)

    #Se rescatan sólamente las 10 amplitudes mayores 

    for i in range(24):
        puntosNuevos[i]  = fcn.LimpiarPuntos(fft_data[i],fft_freq[i])
    
    #Genera las graficas requeridas para el analisis

    fcn.Graficas(fft_freq, potencias, tiempo,limpios)

if __name__ == "__main__":
    main()


#!/usr/bin/ python
# encoding: UTF-8

import sys
import codecs
import math
import module_chi2 as mchi2

"""
Módulo que contiene la función para calcular el Chi².
Autores: María M. Ariza Acero y  César A. Quintana Cataño
Fecha de creación: Oct  9 23:57:25 COT 2013
"""


def main(): 

    """
    Se obtiene una señal para cada electrodo en un encefalograma
    """

    #Cargar los datos 
    !head -n 5 sampled+ma0844az_1-1+_data.dat
    data = np.loadtxt('sampled+ma0844az_1-1+_data.dat')

    #arrays para la señal de cada electrodo con el tiempo

    electrodo1=[]
    electrodo2=[]
    electrodo3=[]
    electrodo4=[]
    electrodo5=[]
    electrodo6=[]
    electrodo7=[]
    electrodo8=[]
    electrodo9=[]
    electrodo10=[]
    electrodo11=[]
    electrodo12=[]
    electrodo13=[]
    electrodo14=[]
    electrodo15=[]
    electrodo16=[]
    electrodo17=[]
    electrodo18=[]
    electrodo19=[]
    electrodo20=[]
    electrodo21=[]
    electrodo22=[]
    electrodo23=[]
    electrodo24=[]

    #Array para guardar la información de cada electrodo 
    electrodos=[electrodo1, electrodo2, electrodo3, electrodo4,electrodo5, electrodo6, electrodo7, electrodo8,electrodo9, electrodo10, electrodo11, electrodo12,electrodo13, electrodo14, electrodo15, electrodo16,electrodo17, electrodo18, electrodo19, electrodo20,electrodo21, electrodo22, electrodo23, electrodo24]

    for i in data:

        """
        Ciclo para guardar la información en los arrays anteriores
        """
        for j in range(24):

            (electrodos[j]).append(i[j])
    
    

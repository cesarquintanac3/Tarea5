import funcionesEsqueleto as fe
import numpy as np

def main():

    """
    toma una serie de datos tomados respecto a el numero de manchas solares presentes en el sol a lo largo del tiempo y genera una serie de graficas utiles para la realizacion de un analisis de los datos. Entre estas graficas encontramos: espectros de potencias a partir de diferentes interpolaciones de los datos, y comparaciones entre los datos antes y despues de pasar por un proceso de filtrado referente a las frecuencias asociadas al sistema por la transformada de fourier.
    """

    #Archivo de entrada
    ArchivoEntrada= 'monthrg.dat'

    #Carga y organiza los datos
    datos = fe.cargar(ArchivoEntrada)
    manchas,acumuladoMeses,intervaloMedicion,agno = fe.arreglarDatos(datos)

    #Interpola la distribucion de puntos asociada a los datos anteriores
    
    x=np.ones(498)
    InterpolacionConstante, InterpolacionLineal, InterpolacionCubica = fe.interpolacion (x,x,x)

    #Aplica fourier a los datos y saca las potencias para el especro de potencias

    fft_datosI, fft_freqI = fe.elementosFourier(InterpolacionConstante)
    fft_datosII, fft_freqII = fe.elementosFourier(InterpolacionLineal)
    fft_datosIII, fft_freqIII = fe.elementosFourier(InterpolacionCubica)

    potenciasI = fe.Potencias(fft_datosI)
    potenciasII= fe.Potencias(fft_datosII)
    potenciasIII= fe.Potencias(fft_datosIII)

    #Limpia los las amplitudes con frecuencias que no son de nuestro interes y obtiene la distribucion de puntos asociada

    puntosNuevosI  = fe.LimpiarPuntos(fft_datosI,fft_freqI)
    puntosNuevosII = fe.LimpiarPuntos(fft_datosII,fft_freqII)
    puntosNuevosIII= fe.LimpiarPuntos(fft_datosIII,fft_freqIII)

    #Genera las graficas requeridas para el analisis

    fe.Graficas(fft_freqI,potenciasI,puntosNuevosI,fft_freqII,potenciasII,puntosNuevosII,fft_freqIII,potenciasIII,puntosNuevosIII,manchas, acumuladoMeses)

    #Estima un periodos para el ciclo solar

    periodo = fe.estimarPeriodo(manchas,acumuladoMeses)
    periodoFiltrado1 = fe.estimarPeriodo(x,puntosNuevosI)
    periodoFiltrado2 = fe.estimarPeriodo(x,puntosNuevosII)
    periodoFiltrado3 = fe.estimarPeriodo(x,puntosNuevosIII)

if __name__ == "__main__":
    main()

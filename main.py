from Clases import Palindromo
from Clases.Palindromo import *

def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar(1-3): "))
    if variable == 1:
        Palindromo.comprobar_palindromo()
    elif variable == 2:
        from Clases import ejercicio2
    elif variable == 3:
        from Clases import ejercicio3
    else:
        eleccion_ejercicio()

eleccion_ejercicio()
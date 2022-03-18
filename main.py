from Clases import Palindromo
from Clases.Palindromo import *

def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar(1-3): "))
    if variable == 1:
        dato=input("¿Qué palabra/número quieres comprobar?\n")
        Palindromo.comprobar_palindromo(dato)
    elif variable == 2:
        from Clases import ejercicio2
    elif variable == 3:
        from Clases import ejercicio3
    elif variable == 4:
        from Clases import ejercicio4
    else:
        eleccion_ejercicio()

eleccion_ejercicio()
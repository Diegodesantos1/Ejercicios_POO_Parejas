from Clases import Palindromo
from Clases.Palindromo import *
from Clases import Logger
from Clases.Logger import *
from Clases import Instancia
from Clases.Instancia import *

def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n -->1: Palíndromo(método de clase)\n -->2: Palíndromo(método de instancias)\n -->3: Logger \n"))
    if variable == 1:
        dato = input("¿Qué palabra/número quieres comprobar? \n")
        print(comprobar_palindromo(dato))
    elif variable == 2:
      palabra = str(input('Introduce la palabra a comprobar: '))
      print(Instancia.Palindromo(palabra).test())
    elif variable == 3:
        numero=int(input("¿Cuántos mensajes quieres? \n"))
        Logger.llamada(numero)
    else:
        eleccion_ejercicio()

eleccion_ejercicio()
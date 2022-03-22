from Clases import Palindromo
from Clases.Palindromo import *
from Clases import Logger
from Clases.Logger import *
from Clases import Puzzle
from Clases.Puzzle import *
def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n -->1: Palíndromo(método de clase)\n -->2: Palíndromo(método de instancias) \n -->3: Puzle \n -->4: Logger \n"))
    if variable == 1:
        palabra=input("¿Qué palabra/número quieres comprobar? \n")
        print(Palindromo.comprobar_palindromo(palabra))
    elif variable == 2:
        from Clases import Instancia
    elif variable == 3:
        from Clases import Puzzle
    elif variable == 4:
        numero=int(input("¿Cuántos mensajes quieres? \n"))
        Logger.llamada(numero)
    else:
        eleccion_ejercicio()

eleccion_ejercicio()
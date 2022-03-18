import os
import time

class Logger:
    def llamada(n):
        print("Se va a generar el fichero de texto en unos instantes...")
        fichero = open("Logger.txt", "a")
        fichero.write("--Start log--")
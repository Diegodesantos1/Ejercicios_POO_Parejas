import os
import time
class Logger:
    def llamada(numero):
        mensaje=str(input("Qué mensaje quieres escribir\n"))
        print("Se va a generar el fichero de texto en unos instantes...")
        fichero = open("Logger.txt", "a")
        fichero.write("--Start log--")
        for  i in range(1, numero+1):
            fichero.write(f" \n {str(i)} {mensaje}")
        fichero.write(f"\n--End log: {str(numero)} log(s)--")
        fichero.close()
        time.sleep (10) #se borra tras 10 segundos
        os.remove("Logger.txt")
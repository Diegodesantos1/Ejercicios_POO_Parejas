class Logger:
    def llamada(n):
        mensaje=input("Qué mensaje quieres escribir")
        print("Se va a generar el fichero de texto en unos instantes...")
        fichero = open("Logger.txt", "a")
        fichero.write("--Start log--")
        for  i in range(1, n+1):
            if i == 1:
                fichero.write(f"\n {mensaje}.")
            else:
                fichero.write(f" \n {(i)} {mensaje}.")
        fichero.write(f"\n--End log: {(n)} log(s)--")
        fichero.close()
Logger.llamada(input("¿Cuántos mensajes quieres?"))
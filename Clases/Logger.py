class Logger:
    def llamada(numero):
        mensaje=input("Qué mensaje quieres escribir\n")
        print("Se va a generar el fichero de texto en unos instantes...")
        fichero = open("Logger.txt", "a")
        fichero.write("--Start log--")
        for  i in range(1, numero+1):
            if i == 1:
                fichero.write(f"\n {mensaje}.")
            else:
                fichero.write(f" \n {(i)} {mensaje}.")
        fichero.write(f"\n--End log: {(numero)} log(s)--")
        fichero.close()
Logger.llamada(input("¿Cuántos mensajes quieres?\n"))
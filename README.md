<h1 align="center">Ejercicios de POO parejas</h1>

*Hemos usado la POO para poder resolver estos ejercicios*

***

<h2>Repositorio</h2>

Este es el link del [Repositorio](https://github.com/Diegodesantos1/Ejercicios_POO_Parejas)

***

<h2>Integrantes</h2>

1. [Martín](https://github.com/mat0ta)
2. [Diego](https://github.com/Diegodesantos1)

***

<h2>Ejercicio 1: Palíndromo: método de clase</h2>

***
Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159012959-12847b6d-df9b-4df5-bee9-b5913c77b071.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Parejas/blob/main/UML/Ejercicio1.drawio)

El código empleado para resolverlo es el siguiente:

```python
class Palindromo:
    def comprobar_palindromo(dato):
        i,j = "áéíóúñÁÉÍÓÚÑ" , "aeiounAEIOUN"
        acento=str.maketrans(i,j)
        dato=dato.translate(acento)
        dato=dato.lower() #Se transforma todo en minúsculas
        dato=dato.replace(" ", "") #Se quitan los espacios para que sea más sencillo
        lista=list(dato)
        listafinal= list(reversed(dato))
        if len(dato) < 1:
            print(True) #Caso para una sola letra o número
        else:
            if dato[0] == dato [-1]:
                Palindromo.comprobar_palindromo(dato[1:-1])
            else:
                print(False)
```
<h2>Ejercicio 2:</h2>

El código empleado para resolverlo es el siguiente:

<h2>Ejercicio 3:</h2>

El código empleado para resolverlo es el siguiente:

<h2>Ejercicio 4: Logger</h2>

***

Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159013115-8d23095a-1086-46f2-8550-d400eb1dfd5e.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Parejas/blob/main/UML/Ejercicio4.drawio)

El código empleado para resolverlo es el siguiente:

```python
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
        time.sleep (10) #se borra tras 15 segundos
        os.remove("Logger.txt")
```

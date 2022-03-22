<h1 align="center">Ejercicios de POO Parejas</h1>

*Hemos usado la POO para poder resolver estos ejercicios, junto con los contenidos teóricos del aula virtual*

***

<h2>Repositorio</h2>

Este es el link del [Repositorio](https://github.com/Diegodesantos1/Ejercicios_POO_Parejas)

***

<h2>Integrantes</h2>

1. [@mat0ta](https://github.com/mat0ta)
2. [@diegodesantos1](https://github.com/Diegodesantos1)

***

<h2>Ejercicio 1: Palíndromo: método de clase</h2>

***

Enunciado: crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos.

Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159435817-c9bf780f-ee80-476f-a5dc-2fa982aa4500.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Parejas/blob/main/UML/Ejercicio1.drawio)

El código empleado para resolverlo es el siguiente:

```python
import unidecode

class Palindromo:
    def comprobar_palindromo(palabra):
      palabra = unidecode.unidecode(palabra.replace(" ", ""))
      palabra_upper = palabra.upper().split()
      if ''.join(palabra_upper) == ''.join(palabra_upper)[::-1]:
        return True
      else:
        return False
```
<h2>Ejercicio 2:</h2>

*** 

Enunciado: en esta misma clase Palindromo, añada un atributo que se inicializará en el constructor. Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. Además, al destruir la instancia, muestre el atributo en mayúsculas.


Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159438523-67715286-7968-45af-b484-f9b1607a1b41.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Parejas/blob/main/UML/Ejercicio2.drawio)

El código empleado para resolverlo es el siguiente:

```python
import unidecode

class Palindromo:
    def __init__(self, palabra):
      self.palabra = palabra
    def test(self):
      palabra = self.palabra
      palabra = unidecode.unidecode(palabra.replace(" ", ""))
      palabra_upper = palabra.upper().split()
      if ''.join(palabra_upper) == ''.join(palabra_upper)[::-1]:
        return True
      else:
        return False

# p = Palindromo("radar") 
# print(p.test())
``` 
Pregunta adicional: ¿por qué se muestra RADAR después de la instanciación Palindromo("sonar")?

```python
print("RADAR es un palindromo y SONAR no, cuando la instancia SI es un palíndromo no la destruye,
por lo tanto que espera a la siguiente instancia para ello,
mientras que si NO es un palindromo es probable que inmediatamente la destruya;
al destruir, el codigo muestra el dato, eso explica por qué RADAR se muestra despues de instanciar SONAR.")
```

<h2>Ejercicio 3:</h2>

***

Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159438111-2c273795-3d79-424e-bc42-b2724c0a1469.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Parejas/blob/main/UML/Ejercicio3.drawio)

El código empleado para resolverlo es el siguiente:

```python
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z')))

""" Output
<class '__main__.A'>
False0
1
2
3
"""
```

<h2>Ejercicio 4: Logger</h2>

*** 

Enunciado: escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada() de una clase Test.

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
        time.sleep (10) #se borra tras 10 segundos
        os.remove("Logger.txt")
```

class Palindromo:
    print("¿Que palabra, frase o número quieres comprobar para ver si es un palíndromo?")
    dato=input()

    i,j = "áéíóúñÁÉÍÓÚÑ" , "aeiounAEIOUN"
    acento=str.maketrans(i,j)
    dato=dato.translate(acento)
    dato=dato.lower() #Se transforma todo en minúsculas
    dato=dato.replace(" ", "") #Se quitan los espacios para que sea más sencillo
    lista = list(dato)
    listafinal= list(reversed(dato))
    def comprobar_palindromo(dato):
        if len(dato) < 1:
            print(f"La palabra o número es un palíndromo") #Caso para una sola letra o número
        else:
            if dato[0] == dato [-1]:
                Palindromo.comprobar_palindromo(dato[1:-1])
            else:
                print(f"La palabra o número no es un palíndromo")
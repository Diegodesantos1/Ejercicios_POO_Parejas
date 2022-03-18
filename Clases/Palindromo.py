class Palindromo:
    def __init__(self,dato):
        self.dato=dato
    def comprobar_palindromo():
        dato=input(print("¿Qué palabra/número quieres comprobar?"))
        i,j = "áéíóúñÁÉÍÓÚÑ" , "aeiounAEIOUN"
        acento=str.maketrans(i,j)
        dato=dato.translate(acento)
        dato=dato.lower() #Se transforma todo en minúsculas
        dato=dato.replace(" ", "") #Se quitan los espacios para que sea más sencillo
        print(dato)
        lista = list(dato)
        listafinal= list(reversed(dato))
        if len(dato) < 1:
            print(f"La palabra o número es un palíndromo") #Caso para una sola letra o número
        else:
            if dato[0] == dato [-1]:
                Palindromo.comprobar_palindromo(dato[1:-1])
            else:
                print(f"La palabra o número no es un palíndromo")
Palindromo.comprobar_palindromo()
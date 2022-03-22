import unidecode

def comprobar_palindromo(palabra):
  palabra = unidecode.unidecode(palabra.replace(" ", ""))
  palabra_upper = palabra.upper().split()
  if ''.join(palabra_upper) == ''.join(palabra_upper)[::-1]:
    return True
  else:
    return False
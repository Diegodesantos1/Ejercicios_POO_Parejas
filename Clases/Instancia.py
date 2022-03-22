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
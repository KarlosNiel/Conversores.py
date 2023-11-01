lista_letras = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç", "0", "1", "2", "3", "4", "5", "6" "7", "8", "9", "?", "!", ".", ",", ";", ":"]

lista_braille = ["⠁", "⠃", "⠉", "⠙", "⠋", "⠛", "⠓", "⠊", "⠚", "⠅", "⠇", "⠍", "⠝", "⠕", "⠏", "⠟", "⠗", "⠎", "⠞", "⠥", "⠧", "⠺", "⠭", "⠽", "⠵", "⠯", "⠚", "⠁", "⠃", "⠉", "⠙", "⠑", "⠋" "⠛", "⠓", "⠊", "⠢", "⠖", "⠄", ",", "⠆", "⠒"]

entrada = str(input())
conversor = ""

for caractere in entrada:
    if caractere in lista_letras:
        comparaçao = lista_letras.index(caractere)
        conversor += lista_braille[comparaçao]
print(f"{conversor}", end="")
        
palavra = str(input())
palavra2 = ""

for digito in palavra:
    conversao = ord(digito)
    print(f"{conversao}", end= "")
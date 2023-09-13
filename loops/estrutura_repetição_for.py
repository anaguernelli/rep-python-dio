text = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in text:
    if letra.upper() in VOGAIS:
        print(letra, end=" - ")

else:
    print("\nFim")

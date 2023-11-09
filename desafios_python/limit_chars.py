''' 
TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
'''

T = input('blabal: ')
qtd_T = len(T)
print(qtd_T)

if qtd_T >= 1 and qtd_T <= 140:
    print("TWEET")
else:
    print("MUTE")

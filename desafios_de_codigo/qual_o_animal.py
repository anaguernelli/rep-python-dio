''' 
TODO Crie as condições necessárias para definir o tipo de animal possível seguindo
o esquema da imagem.
TODO Imprima, de acordo com as condições, o animal identificado.
'''

dicionario = {
    "vertebrado":
    {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
        }
    }

a = input()
b = input()
c = input()

print(dicionario[a][b][c])


# Tentativa 1
# if a == 'vertebrado':
#   if b == 'ave' and c == 'carnivoro':
#     print('aguia')
#   if b == 'ave' and c == 'onivoro'
#   if b == mamifero
# elif a == 'invertebrado':
#    ...

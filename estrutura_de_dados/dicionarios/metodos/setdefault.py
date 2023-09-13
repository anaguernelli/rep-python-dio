contato = {"nome": "Pedro", "idade": 21}

# Se o atributo não estiver no dicionário
contato.setdefault("nome", "Ana")
print(contato)


# Como não há chave telefone no nosso dict, ele o inclui
contato.setdefault("telefone", "84846-3737")
print(contato)

# Imagine uma situação em que precise verificar
# se existe ou não uma chave, o setdefault() é útil

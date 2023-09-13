# Fromkeys cria chaves com valor None/vazio

contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"}
}

print(contatos.fromkeys(["name", "telefone"]))

# Use dict caso o dicionário for inexistente
print(dict.fromkeys(["age", "telefone"], "vazio!"))

contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"}
}

# Ele remove e retorna o valor que removeu
print(contatos.pop("alo@gmail.com"))
print(contatos.pop("alo@gmail.com", {}))

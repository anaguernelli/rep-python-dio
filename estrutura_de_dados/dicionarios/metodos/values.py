# Retorna todos e somente os valores da chave

contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"},
    "anao@gmail.com": {"nome": "Bia", "idade": 30, "celular": "98832-8321"},
    "gui@yahoo.com": {"nome": "Gui", "idade": 18, "celular": "92932-8321"},
    "pedr@gmail.com": {"nome": "Pedro", "idade": 26, "celular": "92802-8321", "extra": {"a": "oi"}},
}

print(contatos.values())

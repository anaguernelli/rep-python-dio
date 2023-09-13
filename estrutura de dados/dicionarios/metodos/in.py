contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"},
    "anao@gmail.com": {"nome": "Bia", "idade": 30, "celular": "98832-8321"},
    "gui@yahoo.com": {"nome": "Gui", "idade": 18, "celular": "92932-8321"},
    "pedr@gmail.com": {"nome": "Pedro", "idade": 26, "celular": "92802-8321", "extra": {"a": "oi"}},
}

result = "gui@yahoo.com" in contatos    # True
print(result)

result = "megui@yahoo.com" in contatos  # False
print(result)

result = "idade" in contatos["anao@gmail.com"] # True
print(result)

result = "extra" in contatos["pedr@gmail.com"] # True
print(result)

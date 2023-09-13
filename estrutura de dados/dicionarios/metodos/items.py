# Retorna uma lista de tuplas
# Muito útil para quando utilizar o for e
# quiser iterar sobre esse valores do dicionário

contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"}
}

print(contatos.items())
# dict_items([('alo@gmail.com', {'nome': 'Ana', 'idade': 21, 'celular': '92832-8321'})])

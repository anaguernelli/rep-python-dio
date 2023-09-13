# Quando não temos certeza se uma chave existe ou não no dicionário
# Com isso, informamos a chave e se não encontrá-la
# Retorna None ou podemos passar um valor default. Ex.: {}

contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"}
}

# contatos["chave"]   KeyError

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("alo@gmail.com", {}))

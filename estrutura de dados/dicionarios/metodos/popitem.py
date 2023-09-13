# A diferença do pop(), é que aqui não informamos qualquer chave
# Este vai retirando os itens na sequência

contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"}
}

print(contatos.popitem())
# print(contatos.popitem()) KeyError

contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"}
}


contatos.update({"alo@gmail.com": {"nome": "Gui"}})
print(contatos)

# Se uma chave que não existe no dicionário,
# ele atualizar com a nova chave
contatos.update({"giovanna@gmail.com": {"nome": "Gio", "idade": 18}})
print(contatos)


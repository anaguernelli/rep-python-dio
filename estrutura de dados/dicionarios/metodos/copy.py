contatos = {
    "alo@gmail.com": {"nome": "Ana", "idade": 21, "celular": "92832-8321"},
}

copia = contatos.copy()
copia["alo@gmail.com"] = {"nome": "Gui"}

print(contatos["alo@gmail.com"])
print(copia["alo@gmail.com"])

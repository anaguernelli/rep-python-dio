def exibir_poema(data_extenso, *args, **kwargs):
    # Aqui pegamos todos os valores que tenham args pulando linha

    texto = "\n".join(args)

    # Depois recebemos o dicionario e o .items()
    # vai entregar uma lista de tuplas com chave:valor
    # E iteramos essa lista de tuplas

    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    print(mensagem)


# Os valores normais, em vírgulas, são considerados os args
# Os valores como chave:valor, dos kwargs
exibir_poema("Terça-feira, 12 de setembro de 2023",
             "Zen of Python",
             "Beautiful is better than Ugly",
             autoru="Tim Peters",
             ano=1999,
             )

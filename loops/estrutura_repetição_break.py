while True:
    # Loop infinito
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
        # Aqui a execução finaliza

    if numero % 2 == 0:
        continue

    print(numero)

print("-" * 15)

# for numero in range(20):
#     if numero == 12:
#         break

#     print(numero)

# for numero in range(20):
#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
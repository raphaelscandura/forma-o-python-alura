codigo_conta = [13,15,38,25,36]
codigo_conta_dolar = [13,25,75,64,36]

todos_os_codigos = []
todos_os_codigos = codigo_conta.copy()
todos_os_codigos.extend(codigo_conta_dolar)

print(todos_os_codigos)

conjunto_de_codigos = set(todos_os_codigos)

print(conjunto_de_codigos)
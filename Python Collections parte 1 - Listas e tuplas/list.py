idades = []

idades.append(15)
idades.extend([18,75,14,35,26,98,56])
print(idades)

idades_no_ano_que_vem = []

for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)
print(idades_no_ano_que_vem)

idades_daqui_dois_anos = [(idade + 2) for idade in idades]

print(idades_daqui_dois_anos)

maiores_de_idade = [(idade) for idade in idades if idade >= 18]

print(maiores_de_idade)
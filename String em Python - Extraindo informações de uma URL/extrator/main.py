url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

index_interrogacao = url.find('?')

url_base = url[:index_interrogacao]
print(url_base)

url_parametros = url[index_interrogacao + 1:]
print(url_parametros)

print(url)

parametro_origem = 'moedaOrigem'
indice_primeiro_parametro = url.find(parametro_origem)
indice_moeda_origem = indice_primeiro_parametro + len(parametro_origem) + 1
primeiro_parametro = url[indice_moeda_origem:]

print(primeiro_parametro)
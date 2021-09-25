from ExtratorURL import ExtratorURL
from ExtratorCEP import ExtratorCEP

url = ExtratorURL("https://bytebank.com/busca?moedaOrigem=real&quantidade=1000&moedaDestino=dolar")

print(url.get_url_base())
print(url.get_url_parametros())
print(url.get_valor_parametro("quantidade"))

cep = ExtratorCEP("R. Goitacazes, 71 - CentroSão Caetano do Sul - SP, 09510-300")
print(cep.extrai_cep())
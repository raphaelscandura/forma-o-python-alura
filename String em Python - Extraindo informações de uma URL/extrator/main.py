from ExtratorURL import ExtratorURL

url = ExtratorURL(None)

print(url.get_url_base())
print(url.get_url_parametros())
print(url.get_valor_parametro("quantidade"))
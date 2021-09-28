texto = "bom dia senhoras e senhores no dia de hoje teremos bom senhores e boa senhoras"
print(set(texto.split()))

quantidade_de_aparicoes = {
    "bom" : 2,
    "senhores" : 2,
    "senhoras" : 2,
    "dia" : 2,
    "hoje" : 1,
    "e" : 1
}

print(type(quantidade_de_aparicoes))
print(quantidade_de_aparicoes["bom"])
print(quantidade_de_aparicoes.get("e"))

quantidade_de_aparicoes = dict(Bom = 2, dia = 1)
print(quantidade_de_aparicoes)
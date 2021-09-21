# Entendendo sintaxe, variáveis dinâmicas etc.

pais = "brasil"
print(type(pais))
titulos = 5
print(type(titulos))
print(pais, "tem", titulos, "titulos de copa do mundo")
pais = 5
print(type(pais))
titulos = "brasil"
print(type(titulos))

print("Data: {:02d}/{:02d}".format(14,6))
print("Dinheiro: R${:3.2f}".format(52.4))
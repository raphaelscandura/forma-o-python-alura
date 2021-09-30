from dominio import Leilao, Lance, Usuario

pedro = Usuario("Pedro")
gabriel = Usuario("Gabriel")

lance_do_pedro = Lance(pedro, 1500)
lance_do_gabriel = Lance(gabriel, 1700)

leilao = Leilao("Televisão")

leilao.adicionar_lance(lance_do_pedro)
leilao.adicionar_lance(lance_do_gabriel)

leilao.imprimir_lances()
from src.dominio import Leilao, Lance, Usuario

pedro = Usuario("Pedro")
gabriel = Usuario("Gabriel")

lance_do_pedro = Lance(pedro, 150.0)
lance_do_gabriel = Lance(gabriel, 1080.0)

leilao = Leilao("Televisão")

leilao.adicionar_lance(lance_do_pedro)
leilao.adicionar_lance(lance_do_gabriel)

leilao.imprimir_todos_os_lances()

leilao.imprimir_maior_e_menor_lances()
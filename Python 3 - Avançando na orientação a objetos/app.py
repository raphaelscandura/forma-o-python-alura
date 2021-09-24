from Filme import Filme
from Serie import Serie

vingadores = Filme("Vingadores", 2017, 1568, 125)

bakas = Serie("Sussy Bakas", 2020, 563, 4)

playlist = [vingadores, bakas]

for programa in playlist:
    print(programa)
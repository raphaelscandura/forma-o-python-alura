from Filme import Filme
from Serie import Serie
from Playlist import Playlist

vingadores = Filme("Vingadores", 2017, 1568, 125)

bakas = Serie("Sussy Bakas", 2020, 563, 4)

filmes_e_series = [vingadores, bakas]

playlist = Playlist("Da night", filmes_e_series)

for programa in playlist:
    print(programa)

print(f'Tamanho da playlist - {playlist.nome}: {len(playlist)}')

print(f'Is bakas on that playlist? {bakas in playlist}')
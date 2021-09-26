import array as arr
import numpy as np

# Evitamos usar array, se precisamos de eficiência com números usamos o numpy

array = arr.array('d', [1,3.5])

print(array)

numeros = np.array([1,3.5])

print(numeros)

print(numeros + 7)

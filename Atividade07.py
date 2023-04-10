import numpy as np

matriz = np.array([[3, 4, 1], [3, 1, 2]])

soma_total = 0

for linha in matriz:
    for elemento in linha:
        soma_total += elemento

print("A soma de todos os elementos da matriz é:", soma_total)

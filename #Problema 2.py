# Problema 2
# Crear 3 matrices donde la cantidad de filas y columnas
# Se generan martrices 3x3
import random

# Genera matriz en consola 3x3
matriz_aleatoria = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

# GGenera matriz en consola del 1 al 10
matriz_1_al_10 = [[num for num in range(1, 10+i)] for i in range(0, 9, 3)]

# Generar matriz del 11 al 30
matriz_11_al_30 = [[num for num in range(11+i, 14+i)] for i in range(0, 18, 3)]

# Generar matriz del -1 al -10
matriz_menos_1_al_menos_10 = [[num for num in range(-1-i, -4-i, -1)] for i in range(0, 9, 3)]

# Imprimir las matrices
print("Matriz aleatoria:")
for fila in matriz_aleatoria:
    print(fila)

print("\nMatriz del 1 al 10:")
for fila in matriz_1_al_10:
    print(fila)

print("\nMatriz del 11 al 30:")
for fila in matriz_11_al_30:
    print(fila)

print("\nMatriz del -1 al -10:")
for fila in matriz_menos_1_al_menos_10:
    print(fila)


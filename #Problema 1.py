#Problema 1


import numpy as np

# Se generan matrices aleatorias A, B y C
A = np.random.randint(0, 11, (4, 4))
B = np.random.randint(0, 11, (4, 4))
C = np.random.randint(0, 11, (4, 4))

# Se calcula la matriz resultante
result = np.dot(np.dot(A^3, B^-1), C) + A^-1

print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)
print("\nMatriz C:")
print(C)
print("\nMatriz Resultante:")
print(result)


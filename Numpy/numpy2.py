# Calentamiento: Crea estos arrays usando funciones de NumPy (NO listas)
import numpy as np

# 1. Un array de 10 ceros
ceros = np.zeros((10))

# 2. Un array de 5 unos
unos = np.ones((5))

# 3. Un array del 0 al 9 (10 elementos)
secuencia = np.arange(10)

# 4. Un array de 5 valores equidistantes entre 0 y 1
lineal = np.linspace(0, 1, 5)

# 5. Una matriz 3x4 de numeros aleatorios enteros entre 1 y 100          (start, stop, size) El start es inclusivo y el stop es exclusivo.
matriz = np.random.randint(1, 101, size=(3,4)) # matriz = np.random.randint(1, 101, (3, 4))

# Verifica las formas
print(f"ceros: {ceros.shape}")
print(f"unos: {unos.shape}")
print(f"secuencia: {secuencia.shape}")
print(f"lineal: {lineal}")
print(f"matriz shape: {matriz.shape}")
experimentos = {
"exp_001": {
"modelo": "ResNet50",
"dataset": "ImageNet",
"metricas": {"accuracy": [0.65, 0.72, 0.78, 0.82], "loss": [1.2,
0.9, 0.7, 0.5]},
"dependencias": {"torch", "numpy", "pillow"}
},
"exp_002": {
"modelo": "VGG16",
"dataset": "CIFAR10",
"metricas": {"accuracy": [0.60, 0.68, 0.71, 0.73], "loss": [1.5,
1.1, 0.95, 0.88]},
"dependencias": {"torch", "numpy"}
},
"exp_003": {
"modelo": "MobileNet",
"dataset": "ImageNet",
"metricas": {"accuracy": [0.55, 0.63, 0.69, 0.74], "loss": [1.8,
1.3, 1.0, 0.82]},
"dependencias": {"torch", "numpy", "opencv"}
}
}

# Ejercicio 1.1: Acceso a diccionarios anidados
# a)
accuracy_final = experimentos['exp_002']['modelo']
print(accuracy_final)
# b)
modelo = experimentos["exp_001"]['metricas']['accuracy'][-1]
print(modelo)

#lista_completa = experimentos["exp_003"]['metricas']['loss']
#print(lista_completa)

# Ejercicio 1.2: Operaciones con sets
# a)
comunes = (experimentos['exp_001']['dependencias'] & experimentos['exp_002']['dependencias']) & experimentos['exp_003']['dependencias']
print(comunes)
# b)
todas = experimentos['exp_001']['dependencias'] | experimentos['exp_002']['dependencias'] | experimentos['exp_003']['dependencias']
print(todas)
# c)
exclusivas = experimentos['exp_001']['dependencias'] - experimentos['exp_002']['dependencias']
print(exclusivas)
# Ejercicio 1.3: Slicing y agregación
losses = [2.3, 1.8, 1.5, 1.2, 0.95, 0.87, 0.81, 0.78, 0.76, 0.75]
# a)
ultimas_3 = losses[-3:]
print(ultimas_3)
# b)
primeras_5 = losses[5:]
print(primeras_5)
# d)
ultimas_5 = losses[-5:]
promedio_final = sum(ultimas_5) / len(ultimas_5)
print(promedio_final)
# Ejercicio 2.1: List Comprehensions
# a)
cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)
# b)
accuracies = [0.65, 0.72, 0.78, 0.82, 0.71, 0.88]
altas = []
for accuracy in accuracies:
    if accuracy > 0.75:
        altas.append(accuracy)
print(altas)
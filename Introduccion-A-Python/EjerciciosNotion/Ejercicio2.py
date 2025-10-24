"""
- Ejercicio 2: Evaluación del rendimiento de un algoritmo de clasificación (operadores)
    
    Descripción: Imagina que estás trabajando en un algoritmo de clasificación para predecir si un paciente tiene o no una enfermedad basándose en sus niveles de glucosa y presión arterial. 
    Se te han proporcionado los datos de un paciente, y el sistema predice si el paciente tiene o no la enfermedad (con una predicción de "1" si la predicción es positiva y "0" si es negativa).
    
    Tu tarea es evaluar el rendimiento del sistema de predicción, calculando el error absoluto y el error relativo, pero además, debes comparar los valores reales con los predichos 
    para determinar si el modelo ha subestimado o sobreestimado la condición del paciente.
    
    ### Instrucciones:
    
    1. Recibe las entradas de la glucosa real y la presión arterial real del paciente, junto con las predicciones del modelo (en formato 1 o 0).
    2. Calcula el error absoluto de cada característica (glucosa y presión arterial). El error absoluto es la diferencia entre el valor real y el valor estimado,
        sin importar si es positiva o negativa (usa `abs()`).
    3. Calcula el error relativo para ambas características (glucosa y presión arterial), usando la fórmula: `Error Relativo=(Error Absoluto / Valor Real)x100`
    4. Calcula el rendimiento del modelo basado en las predicciones. Si las predicciones son correctas (es decir, el modelo predijo correctamente el diagnóstico del paciente),
        asigna un punto al rendimiento. Si la predicción fue incorrecta, no se asignan puntos.
    5. Calcula el puntaje final de rendimiento sumando los puntos por las predicciones correctas.
"""

import random

glucosaReal = -1
presionReal = -1

while glucosaReal < 0 or glucosaReal > 1:
    try:
        glucosaReal = int(input("Introduce la glucosa del paciente(1, 0): "))
    except ValueError:
        print("Introduce un número válido")

while presionReal < 0 or presionReal > 1:
    try:
        presionReal = int(input("Introduce la presion arterial del paciente(1, 0): "))
    except ValueError:
        print("Introduce un número válido")

glucosaPred = random.randint(0,1)
presionPred = random.randint(0,1)

glucosaAbs = abs(glucosaPred - glucosaReal)

presionAbs = abs(presionPred - presionReal)

print("Predicción de glucosa: ",glucosaPred)
print("Predicción de presión arterial: ",presionPred)
print("Error absoluto en la glucosa: ", glucosaAbs)
print("Error absoluto en la presión arterial: ",presionAbs)
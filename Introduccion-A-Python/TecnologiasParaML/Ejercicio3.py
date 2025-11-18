"""
- Ejercicio 3: Procesamiento de métricas de entrenamiento (LISTAS)

Durante el entrenamiento de una red neuronal, se registran valores de loss y accuracy en cada época. Debes implementar funciones para analizar estos resultados.
"""

training_losses = [2.3, 1.8, 1.5, 1.2, 0.95, 0.87, 0.81, 0.78, 0.76, 0.75]
validation_losses = [2.4, 1.9, 1.6, 1.4, 1.1, 0.98, 0.92, 0.89, 0.88, 0.87]

"""
1. Calcula la diferencia entre training loss y validation loss para cada época. Utiliza list comprehension.
2. Identifica en qué épocas el validation loss fue mayor que el training loss en más de 0.15 unidades. Esto puede indicar overfitting.
3. Calcula la tasa de mejora promedio del training loss entre épocas consecutivas. Fórmula: `(loss[i] - loss[i+1]) / loss[i]`
4. Genera una lista con las últimas 5 épocas donde el training loss haya mejorado respecto a la época anterior. Utiliza slicing y operaciones de filtrado.
"""
def calcular_diferencias(train_losses: list, val_losses: list) -> list:
    """Retorna lista con diferencias (val_loss - train_loss) para cada época"""
    return [val - train for train, val in zip(train_losses, val_losses)]
    pass

def detectar_overfitting(train_losses: list, val_losses: list, threshold: float = 0.15) -> list:
    """Retorna lista de índices de épocas donde se detecta posible overfitting"""
    return [val - train for train, val in zip(train_losses, val_losses) if (val - train) > threshold]
    pass

def tasa_mejora_promedio(losses: list) -> float:
    """Calcula la tasa de mejora promedio entre épocas consecutivas"""

    """
    training_losses = [2.3, 1.8, 1.5, 1.2, 0.95, 0.87, 0.81, 0.78, 0.76, 0.75]
    mejoras = [(2.3 - 1.8) / 2.3,
                (1.8 - 1.5) / 1.8,
                (1.5 - 1.2) / 1.5,
                (1.2 - 0.95) / 1.2,
                (0.95 - 0.87) / 0.95,
                (0.87 - 0.81) / 0.87,
                (0.81 - 0.78) / 0.81,
                (0.78 - 0.76) / 0.78,
                (0.76 - 0.75) / 0.76]
    """

    mejoras = [(losses[i] - losses[i + 1]) / losses[i] for i in range(len(losses) - 1)]

    return sum(mejoras) / len(mejoras)
    pass


# 1. Diferencias entre training loss y validation loss
diferencias = calcular_diferencias(training_losses, validation_losses)
print(f"\nDiferencias por cada época: {diferencias}")

# 2. Épocas con posible overfitting
overfitting = detectar_overfitting(training_losses, validation_losses)
print(f"\nÉpocas con posible overfitting: {overfitting}")

# 3. Tasa de mejora promedio del training loss
tasa_mejora = tasa_mejora_promedio(training_losses)
print(f"\nTasa de mejora promedio del training loss: {tasa_mejora} ({tasa_mejora*100:.2f}%)")

# 4. Últimas 5 épocas con mejora en training loss
mejoras_training = [i for i in range(1, len(training_losses)) if training_losses[i] < training_losses[i - 1]]
ultimas_5_mejoras = mejoras_training[-5:]
print(f"\nÚltimas 5 épocas con mejora en training loss: {ultimas_5_mejoras}")
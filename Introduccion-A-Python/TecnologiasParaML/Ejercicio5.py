"""
- Ejercicio 5: Gestión de hiperparámetros y resultados (DICCIONARIOS)
    
    En un experimento de búsqueda de hiperparámetros, se prueban diferentes configuraciones de modelos. Debes analizar y comparar resultados.
"""

experimentos = {
    "exp_001": {"learning_rate": 0.001, "batch_size": 32, "optimizer": "Adam", "accuracy": 0.87, "loss": 0.42},
    "exp_002": {"learning_rate": 0.01, "batch_size": 64, "optimizer": "SGD", "accuracy": 0.82, "loss": 0.51},
    "exp_003": {"learning_rate": 0.001, "batch_size": 16, "optimizer": "Adam", "accuracy": 0.91, "loss": 0.28},
    "exp_004": {"learning_rate": 0.0001, "batch_size": 32, "optimizer": "RMSprop", "accuracy": 0.89, "loss": 0.35}
}

"""
1. Identifica el experimento con mayor accuracy. Retorna un diccionario con el ID del experimento y sus parámetros completos.
2. Filtra los experimentos que usan el optimizador "Adam" y tienen accuracy superior a 0.85. Utiliza dictionary comprehension.
3. Crea un diccionario que mapee cada optimizer único a una lista de accuracies obtenidas con ese optimizer.
4. Calcula el promedio de accuracy y loss para cada combinación de `learning_rate` y `batch_size`. Retorna un diccionario anidado con la estructura: `{(lr, bs): {"avg_accuracy": X, "avg_loss": Y}}`
5. Genera un ranking de los 3 mejores experimentos basado en la métrica F1-score aproximado: `2 * (accuracy * (1 - loss)) / (accuracy + (1 - loss))`. Retorna una lista de tuplas `[(exp_id, f1_score), ...]` ordenada descendentemente.
"""

def mejor_experimento(experimentos: dict) -> dict:
    """Retorna diccionario con ID y parámetros del mejor experimento por accuracy"""
    best_acc = -1

    for exp_id, params in experimentos.items():
        if params["accuracy"] > best_acc:
            best_acc = params["accuracy"]
            best_exp = {exp_id: params}
    return best_exp
    pass

def agrupar_por_optimizer(experimentos: dict) -> dict:
    """Retorna diccionario {optimizer: [accuracies]}"""
    resultado = {}
    
    for exp_id, params in experimentos.items():
        optimizer = params["optimizer"]
        accuracy = params["accuracy"]
        
        if optimizer not in resultado:
            resultado[optimizer] = []
        
        resultado[optimizer].append(accuracy)
    
    return resultado
    pass

def calcular_f1_aproximado(accuracy: float, loss: float) -> float:
    """Calcula F1-score aproximado basado en accuracy y loss"""
    numerador = 2 * (accuracy * (1 - loss))
    denominador = accuracy + (1 - loss)
    
    if denominador == 0:
        return 0.0
    
    return numerador / denominador
    pass

def ranking_experimentos(experimentos: dict, top_n: int = 3) -> list:
    """Retorna lista de tuplas (exp_id, f1_score) ordenadas por f1_score"""
    f1_scores = []
    
    for exp_id, params in experimentos.items():
        f1 = calcular_f1_aproximado(params["accuracy"], params["loss"])
        f1_scores.append((exp_id, f1))
    
    f1_scores.sort(key=lambda x: x[1], reverse=True)
    
    return f1_scores[:top_n]
    pass

# 1. Mejor experimento por accuracy
best_experiment = mejor_experimento(experimentos)
print(f"Mejor experimento por accuracy: {best_experiment}")

# 2. Filtrar experimentos con Adam y accuracy > 0.85 (usando dict comprehension)
adam_filtered = {
    exp_id: params
    for exp_id, params in experimentos.items()
    if params["optimizer"] == "Adam" and params["accuracy"] > 0.85
}
print(f"2. Experimentos con Adam y accuracy > 0.85:")
for exp_id, params in adam_filtered.items():
    print(f"   {exp_id}: {params}")
print()

# 3. Agrupar accuracies por optimizer
optimizer_accuracies = agrupar_por_optimizer(experimentos)
print(f"3. Accuracies agrupadas por optimizer:")
for optimizer, accuracies in optimizer_accuracies.items():
    print(f"   {optimizer}: {accuracies}")
print()

# 4. Promedios por configuración (learning_rate, batch_size)
configs = {}
for exp_id, params in experimentos.items():
    lr = params["learning_rate"]
    bs = params["batch_size"]
    key = (lr, bs)
    
    if key not in configs:
        configs[key] = {"accuracies": [], "losses": []}
    
    configs[key]["accuracies"].append(params["accuracy"])
    configs[key]["losses"].append(params["loss"])

# Calcular promedios
promedios = {}
for key, valores in configs.items():
    avg_accuracy = sum(valores["accuracies"]) / len(valores["accuracies"])
    avg_loss = sum(valores["losses"]) / len(valores["losses"])
    promedios[key] = {"avg_accuracy": avg_accuracy, "avg_loss": avg_loss}

print(f"4. Promedios por (learning_rate, batch_size):")
for config, stats in promedios.items():
    lr, bs = config
    print(f"   LR={lr}, BS={bs}: avg_accuracy={stats['avg_accuracy']:.4f}, avg_loss={stats['avg_loss']:.4f}")
print()

# 5. Ranking por F1-score
ranking = ranking_experimentos(experimentos, top_n=3)
print(f"5. Top 3 experimentos por F1-score:")
for i, (exp_id, f1) in enumerate(ranking, 1):
    print(f"   {i}. {exp_id}: F1-score = {f1:.4f}")
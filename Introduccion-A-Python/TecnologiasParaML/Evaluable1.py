"""
- **EVALUABLE 1:** Colecciones de datos
    
    Trabajas en el equipo de MLOps de una empresa que entrena múltiples modelos de deep learning simultáneamente.
    Necesitas implementar un sistema de gestión de experimentos que permita rastrear, validar y analizar resultados de diferentes arquitecturas, 
    datasets y configuraciones de hiperparámetros.
    
    El sistema debe manejar:
    
    - **Configuraciones de experimentos** (diccionarios)
    - **Historial de métricas por época** (listas)
    - **Metadatos inmutables de modelos** (tuplas)
    - **Validación de recursos y dependencias** (sets)
"""

# Base de datos de experimentos ejecutados
experimentos_db = {
    "exp_20241101_001": {
        "modelo": "ResNet50",
        "dataset": "ImageNet",
        "metadata": (224, 224, 3, 1000),  # (height, width, channels, num_classes)
        "hiperparametros": {
            "learning_rate": 0.001,
            "batch_size": 32,
            "optimizer": "Adam",
            "epochs": 100
        },
        "metricas_entrenamiento": {
            "loss": [1.2, 1.0, 0.9, 0.85, 0.80, 0.78, 0.75, 0.73, 0.70, 0.68],
            "accuracy": [0.45, 0.58, 0.65, 0.71, 0.76, 0.79, 0.82, 0.84, 0.85, 0.86]
        },
        "metricas_validacion": {
            "loss": [1.3, 1.2, 1.25, 1.3, 1.35, 1.37, 1.38, 1.39, 1.40, 1.41],
            "accuracy": [0.43, 0.56, 0.63, 0.69, 0.74, 0.77, 0.80, 0.82, 0.83, 0.84]
        },
        "dependencias": {"torch", "torchvision", "numpy", "pillow"},
        "gpu_usado": "NVIDIA_A100",
        "tiempo_total_minutos": 245
    },
    "exp_20241101_002": {
        "modelo": "VGG16",
        "dataset": "CIFAR10",
        "metadata": (32, 32, 3, 10),
        "hiperparametros": {
            "learning_rate": 0.01,
            "batch_size": 64,
            "optimizer": "SGD",
            "epochs": 50
        },
        "metricas_entrenamiento": {
            "loss": [2.1, 1.6, 1.3, 1.0, 0.85, 0.72, 0.65, 0.61, 0.58, 0.56],
            "accuracy": [0.35, 0.52, 0.61, 0.68, 0.73, 0.77, 0.80, 0.82, 0.83, 0.84]
        },
        "metricas_validacion": {
            "loss": [2.2, 1.7, 1.4, 1.2, 1.0, 0.88, 0.82, 0.80, 0.79, 0.78],
            "accuracy": [0.33, 0.50, 0.59, 0.65, 0.70, 0.74, 0.77, 0.78, 0.79, 0.80]
        },
        "dependencias": {"torch", "torchvision", "numpy"},
        "gpu_usado": "NVIDIA_V100",
        "tiempo_total_minutos": 120
    },
    "exp_20241102_001": {
        "modelo": "MobileNetV2",
        "dataset": "ImageNet",
        "metadata": (224, 224, 3, 1000),
        "hiperparametros": {
            "learning_rate": 0.001,
            "batch_size": 128,
            "optimizer": "Adam",
            "epochs": 150
        },
        "metricas_entrenamiento": {
            "loss": [2.5, 2.0, 1.7, 1.4, 1.2, 1.0, 0.92, 0.86, 0.82, 0.79],
            "accuracy": [0.40, 0.52, 0.60, 0.67, 0.72, 0.76, 0.79, 0.81, 0.83, 0.84]
        },
        "metricas_validacion": {
            "loss": [2.6, 2.1, 1.8, 1.5, 1.3, 1.1, 1.0, 0.95, 0.92, 0.90],
            "accuracy": [0.38, 0.50, 0.58, 0.65, 0.70, 0.74, 0.77, 0.79, 0.80, 0.81]
        },
        "dependencias": {"torch", "torchvision", "numpy", "pillow", "opencv"},
        "gpu_usado": "NVIDIA_A100",
        "tiempo_total_minutos": 380
    },
    "exp_20241102_002": {
        "modelo": "ResNet50",
        "dataset": "CIFAR100",
        "metadata": (32, 32, 3, 100),
        "hiperparametros": {
            "learning_rate": 0.0001,
            "batch_size": 32,
            "optimizer": "RMSprop",
            "epochs": 200
        },
        "metricas_entrenamiento": {
            "loss": [3.2, 2.5, 2.0, 1.7, 1.5, 1.3, 1.2, 1.1, 1.05, 1.0],
            "accuracy": [0.25, 0.38, 0.48, 0.55, 0.60, 0.64, 0.67, 0.70, 0.72, 0.74]
        },
        "metricas_validacion": {
            "loss": [3.3, 2.6, 2.1, 1.8, 1.6, 1.5, 1.4, 1.35, 1.32, 1.30],
            "accuracy": [0.23, 0.36, 0.46, 0.53, 0.58, 0.61, 0.63, 0.65, 0.66, 0.67]
        },
        "dependencias": {"torch", "torchvision", "numpy", "albumentations"},
        "gpu_usado": "NVIDIA_V100",
        "tiempo_total_minutos": 420
    },
    "exp_20241103_001": {
        "modelo": "EfficientNetB0",
        "dataset": "ImageNet",
        "metadata": (224, 224, 3, 1000),
        "hiperparametros": {
            "learning_rate": 0.005,
            "batch_size": 64,
            "optimizer": "SGD",
            "epochs": 120
        },
        "metricas_entrenamiento": {
            "loss": [2.2, 1.7, 1.4, 1.1, 0.95, 0.83, 0.75, 0.70, 0.66, 0.63],
            "accuracy": [0.48, 0.60, 0.68, 0.74, 0.78, 0.81, 0.84, 0.86, 0.87, 0.88]
        },
        "metricas_validacion": {
            "loss": [2.3, 1.8, 1.5, 1.2, 1.0, 0.90, 0.83, 0.79, 0.77, 0.75],
            "accuracy": [0.46, 0.58, 0.66, 0.72, 0.76, 0.79, 0.82, 0.84, 0.85, 0.86]
        },
        "dependencias": {"torch", "torchvision", "numpy", "pillow"},
        "gpu_usado": "NVIDIA_A100",
        "tiempo_total_minutos": 290
    }
}

"""
## Parte 3: Optimización de Configuraciones (DICCIONARIOS - 30%)

Analiza y optimiza configuraciones de hiperparámetros basándote en resultados históricos.

**Funciones requeridas:**
"""

def ranking_experimentos(experimentos_db: dict, criterio: str = "accuracy_final") -> list:
    """
    Genera ranking de experimentos según diferentes criterios.

    Criterios disponibles:
    - "accuracy_final": Mayor accuracy de validación en última época
    - "convergencia": Menor número de épocas para alcanzar 80% accuracy val
    - "eficiencia": Mejor ratio accuracy_final / tiempo_total
    - "estabilidad": Menor varianza en validation loss últimas 5 épocas

    Returns:
        Lista de tuplas: [(exp_id, valor_metrica), ...] ordenada descendente
    """

    for exp_id, exp_data in experimentos_db.items():
        # [-1] Obtiene el último elemenento de la lista para cada experimento
        if criterio == "accuracy_final":
            accuracy = exp_data["metricas_validacion"]["accuracy"][-1]
        elif criterio == "convergencia":
            convergencia = exp_data["metricas_validacion"]["accuracy"]
    pass



    rank_experimentos = ranking_experimentos(experimentos_db, "accuracy_final")

    print("=" * 70)
    print(f" Experimento: {exp_id}")
    print(f" Modelo: {exp_data['modelo']}")
    print(f" Dataset: {exp_data['dataset']}\n")

    print(rank_experimentos)
    print("=" * 70)

def mejores_hiperparametros_por_dataset(experimentos_db: dict) -> dict:
    """
    Identifica las mejores configuraciones de hiperparámetros por dataset.

    Para cada dataset, encuentra el experimento con mejor accuracy final
    y extrae sus hiperparámetros.

    Returns:
        {
            "dataset_name": {
                "mejor_exp_id": str,
                "hiperparametros": dict,
                "accuracy_alcanzada": float
            },
            ...
        }
    """
    pass

def analisis_impacto_hiperparametros(experimentos_db: dict) -> dict:
    """
    Analiza el impacto de cada hiperparámetro en el rendimiento.

    Agrupa experimentos por valor de hiperparámetro y calcula
    accuracy promedio para cada valor único.

    Returns:
        {
            "learning_rate": {
                0.001: {"avg_accuracy": X, "num_experimentos": N},
                0.01: {"avg_accuracy": Y, "num_experimentos": M},
                ...
            },
            "batch_size": {...},
            "optimizer": {...}
        }
    """
    pass

def generar_configuracion_optima(experimentos_db: dict, dataset: str, modelo: str) -> dict:
    """
    Genera configuración óptima para un par dataset-modelo basándose en histórico.

    Si existe experimento exacto con ese dataset y modelo:
        - Usa esos hiperparámetros
    Si no:
        - Usa hiperparámetros más frecuentes en experimentos del dataset
        - Si no hay del dataset, usa promedios globales

    Returns:
        {
            "hiperparametros_sugeridos": dict,
            "confianza": str ("alta", "media", "baja"),
            "experimentos_referencia": list de exp_ids usados
        }
    """
    pass

"""
## Parte 4: Gestión de Dependencias y Recursos (SETS - 25%)

Valida compatibilidad de entornos y optimiza el uso de recursos computacionales.

**Funciones requeridas:**
"""

def conflictos_dependencias(experimentos_a_ejecutar: list, experimentos_db: dict) -> dict:
    """
    Detecta posibles conflictos si se ejecutan múltiples experimentos simultáneamente.

    Args:
        experimentos_a_ejecutar: Lista de exp_ids a ejecutar en paralelo

    Returns:
        {
            "puede_parallelizar": bool,
            "dependencias_conflictivas": set,  # Dependencias que no coinciden
            "gpu_compartida": bool,  # True si requieren misma GPU
            "recomendacion": str
        }
    """
    pass



"""
## Función Integradora Final (BONUS - 20% extra)

Implementa una función que use TODAS las colecciones de datos de forma integrada:
"""

def informe_completo_experimento(exp_id: str, experimentos_db: dict) -> dict:
    """
    Genera un informe completo de un experimento usando todas las colecciones.

    El informe debe incluir:

    1. Metadata del modelo (TUPLA):
       - Dimensiones de entrada
       - Complejidad calculada

    2. Análisis de convergencia (LISTAS):
       - Tasa de convergencia
       - Overfitting detectado
       - Épocas críticas

    3. Contexto comparativo (DICCIONARIOS):
       - Posición en ranking general
       - Comparación con otros experimentos del mismo dataset
       - Comparación con otros experimentos del mismo modelo

    4. Validación de entorno (SETS):
       - Dependencias únicas de este experimento
       - Dependencias compartidas con otros experimentos exitosos
       - Compatibilidad con entorno estándar

    Returns:
        Diccionario estructurado con toda la información analizada
    """
    pass
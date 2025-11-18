"""
- Ejercicio 6: Análisis de vocabulario en NLP (SETS)

    En procesamiento de lenguaje natural, es fundamental analizar vocabularios, tokens únicos y diferencias entre corpus de texto. Trabajarás con sets para realizar operaciones eficientes.
"""

corpus_entrenamiento = [
    "machine learning is transforming artificial intelligence",
    "deep learning neural networks require large datasets",
    "natural language processing uses machine learning algorithms",
    "computer vision and image recognition are ai applications"
]

corpus_validacion = [
    "neural networks power modern artificial intelligence systems",
    "machine learning algorithms analyze large datasets efficiently",
    "deep learning transforms computer vision applications",
    "natural language understanding requires advanced ai techniques"
]

"""
1. Extrae el vocabulario único de cada corpus (convierte todo a minúsculas y separa por espacios). Almacena cada vocabulario como un set.
2. Identifica las palabras que aparecen en ambos corpus (intersección). Estas son palabras del dominio común.
3. Encuentra las palabras que aparecen únicamente en el corpus de entrenamiento pero no en validación. Esto puede indicar términos subrepresentados.
4. Calcula el índice de Jaccard entre ambos vocabularios: `|intersección| / |unión|`. Este índice mide la similitud entre conjuntos (valor entre 0 y 1).
5. Genera un diccionario que mapee cada palabra del vocabulario total a su frecuencia de aparición en el corpus de entrenamiento. Utiliza un contador manual (sin librerías externas como Counter).
6. Identifica palabras que aparecen en al menos 2 documentos del corpus de entrenamiento. Estas son palabras potencialmente importantes para el modelo.
"""

def extraer_vocabulario(corpus: list) -> set:
    """Extrae conjunto de palabras únicas del corpus"""
    vocab = set()
    for doc in corpus:
        words = doc.lower().split()
        vocab.update(words)
    return vocab
    pass

def calcular_jaccard(set_a: set, set_b: set) -> float:
    """Calcula índice de Jaccard entre dos conjuntos"""
    interseccion = set_a.intersection(set_b)
    union = set_a.union(set_b)
    
    return len(interseccion) / len(union)
    pass

def palabras_frecuentes(corpus: list, min_docs: int = 2) -> set:
    """Retorna palabras que aparecen en al menos min_docs documentos"""
    word_count = {}
    for doc in corpus:
        words = set(doc.lower().split())
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    resultado = {word for word, count in word_count.items() if count >= min_docs}
    return resultado

    pass

def contar_frecuencias(corpus: list, vocabulario: set) -> dict:
    """Retorna diccionario {palabra: frecuencia_total}"""
    word_count = {}
    for doc in corpus:
        words = set(doc.lower().split())
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return {word for words, count in word_count.items() if count >= 1}
    pass

# 1. Extracción de vocabulario único
vocab_entrenamiento = extraer_vocabulario(corpus_entrenamiento)
print(f"Vocabulario Entrenamiento: {vocab_entrenamiento}\n")
vocab_validacion = extraer_vocabulario(corpus_validacion)
print(f"Vocabulario Validación: {vocab_validacion}\n")

# 2. Palabras en ambos corpus (intersección)
palabras_comunes = vocab_entrenamiento.intersection(vocab_validacion)
print(f"Palabras comunes en ambos corpus: {palabras_comunes}\n")

# 3. Palabras corpus entrenamiento únicas
palabras_unicas_entrenamiento = vocab_entrenamiento - vocab_validacion
print(f"Palabras únicas en Entrenamiento: {palabras_unicas_entrenamiento}\n")

# 4. Índice de Jaccard entre vocabularios
interseccion_vocab = calcular_jaccard(vocab_entrenamiento, vocab_validacion)
print(f"Palabras en ambos corpus: {interseccion_vocab}\n")

# 5. Frecuencia de palabras en corpus de entrenamiento
frecuencias_entrenamiento = palabras_frecuentes(corpus_entrenamiento)
print(f"Frecuencias en Entrenamiento: {frecuencias_entrenamiento}\n")

# 6. Palabras en al menos 2 documentos del corpus de entrenamiento
palabras_importantes = contar_frecuencias(corpus_entrenamiento, vocab_entrenamiento)
print(f"Palabras en al menos 2 documentos: {palabras_importantes}\n")

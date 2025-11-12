import spacy # NLTK

# Cargar el modelo de idioma en español
nlp = spacy.load("es_core_news_sm")

# Texto de entrada
texto= "Gabriel García Márquez fue un escritor colombiano, conocido por obras como Cien años de soledad y El amor en los tiempos del cólera."

# Procesar el texto
doc = nlp(texto)

# Imprimir tokens con sus etiquetas morfosintácticas
print(" Análisis morfosintáctico:")
for token in doc:
    print(f"{token.text:<15} {token.pos_:<10} {token.dep_:<15}")

# Extraer las entidades nombradas
print("\n Entidades nombradas:")
for ent in doc.ents:
    print(f"{ent.text:<30} {ent.label_}")
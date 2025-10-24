"""
- Ejercicio 1: Evaluación del desempeño de un sistema de recomendación (operadores)
    
    Estás trabajando en un **sistema de recomendación** que predice la calificación que un usuario le dará a una película.
    El sistema genera una **predicción** de la calificación, pero deseas **evaluar su precisión** comparando las calificaciones reales dadas por el usuario con las predicciones.
    
    Tu tarea es calcular el **error absoluto** y el **error relativo** entre las calificaciones reales y las predicciones.
    Además, debes determinar si la **predicción fue superior o inferior** a la calificación real.
    
    ### **Instrucciones:**
    
    1. Recibe los datos de la calificación real (de 1 a 5) y la predicción del sistema (de 1 a 5) como entradas desde el usuario.
    2. Calcula el error absoluto entre la calificación real y la predicción. El error absoluto es la diferencia entre ambos valores,
        sin importar si es positiva o negativa (utiliza `abs()`).
    3. Calcula el error relativo como un porcentaje, usando la fórmula: `Error Relativo =(ErrorAbsoluto / CalificacionReal )x100`
    4. Determina si la predicción fue superior o inferior a la calificación real. Si la predicción es mayor, el sistema sobreestimó la calificación.
        Si la predicción es menor, el sistema subestimó la calificación. Almacena el resultado como un valor booleano y muestra el mensaje correspondiente.
    5. Usa operadores de asignación para ajustar un puntaje de confianza en el sistema. Si la predicción es exacta (sin error absoluto), añade 10 puntos al puntaje de confianza.
    Si el error absoluto es menor o igual a 1, añade 5 puntos. Si el error absoluto es mayor que 1, no añades puntos.
"""
import random

nRandom = random.randint(1, 5)
nReal = 0
puntuaje = 0

while nReal < 1 or nReal > 5:
    nReal = int(input("Introduce la valoración que le das a la película entre 1 y 5: "))

errorAbs = nReal - nRandom

print("Prediccion de calificacion: ",nRandom)

print("Error absoluto: ",abs(errorAbs))

errorRelativo = (errorAbs / nReal) * 100

print("Error relativo: ",errorRelativo)

if nRandom>nReal:
    booleano = bool(1)

if bool==1:
    print("El sistema sobreestimo la calificacion")
elif bool == 0:
    print("El sistema subestimo la calificacion")

if errorAbs == 0:
    puntuaje += 10
elif errorAbs == 1: # He puesto que en lugar de ser menor o igual, sea solo igual, por que de ser menor le daría 10 puntos, y me interpreta mal si pongo el menor
    puntuaje += 5

print(puntuaje)

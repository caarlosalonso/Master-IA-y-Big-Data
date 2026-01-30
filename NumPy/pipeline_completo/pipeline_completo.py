import numpy as np

# Semilla para reproducibilidad
np.random.seed(42)

n = 365

# Variables independientes
temperatura = np.random.normal(18, 8, n)
temperatura = np.clip(temperatura, -2, 38)

humedad = np.random.normal(55, 15, n)
humedad = np.clip(humedad, 20, 95)

viento = np.random.exponential(12, n)
viento = np.clip(viento, 0, 45)

lluvia = np.random.exponential(3, n)
lluvia = np.clip(lluvia, 0, 35)

festivo = np.random.binomial(1, 0.08, n)
fin_semana = np.random.binomial(1, 2/7, n)

# Variable objetivo (con relación real + ruido)
alquileres = (
    2200                           # base
    + 45 * temperatura             # más calor = más alquileres
    - 8 * humedad                  # humedad alta = menos
    - 15 * viento                  # viento = menos
    - 40 * lluvia                  # lluvia = mucho menos
    - 300 * festivo                # festivos = menos (gente fuera)
    + 400 * fin_semana             # fines de semana = más (ocio)
    + np.random.normal(0, 150, n)  # ruido
)
alquileres = np.clip(alquileres, 800, 4500).astype(int)

# Crear matriz de datos
datos = np.column_stack([
    temperatura, humedad, viento, lluvia, festivo, fin_semana, alquileres
])

# Guardar CSV
np.savetxt(
    'madridbici.csv',
    datos,
    delimiter=',',
    header='temperatura,humedad,viento,lluvia,festivo,fin_semana,alquileres',
    comments='',
    fmt=['%.1f', '%.1f', '%.1f', '%.1f', '%d', '%d', '%d']
)

print("Dataset guardado: madridbici.csv")
print(f"Dimensiones: {datos.shape}")

'''
### Fase 1: Exploración

1. Cargad el CSV con `np.genfromtxt()` (skip_header=1, delimiter=',')
2. Verificad las dimensiones con `.shape`
3. Separad las features (columnas 0-5) del target (columna 6)
4. Para cada variable, calculad e imprimid:
    - Media
    - Desviacion tipica
    - Minimo y maximo
5. Responded a estas preguntas en comentarios:
    - ¿Cual es el rango de alquileres?
    - ¿Que variable tiene mayor dispersion relativa (std/mean)?
    - ¿Hay algun valor que parezca anomalo?

### Fase 2: Limpieza

1. Comprobad si hay valores NaN: `np.isnan(datos).sum()`
2. Aplicad clip a las variables continuas para eliminar outliers extremos:
    - temperatura: [-5, 40]
    - humedad: [15, 100]
    - viento: [0, 50]
    - lluvia: [0, 40]
3. Verificad cuantos valores fueron modificados por el clip
'''
### Fase 1: Exploración
# 1. Cargad el CSV
datos_cargados = np.genfromtxt('madridbici.csv', delimiter=',', skip_header=1)
# 2. Verificad las dimensiones
print(f"Dimensiones del dataset cargado: {datos_cargados.shape}")
# 3. Separad features y target
features = datos_cargados[:, :-1]
target = datos_cargados[:, -1]
# 4. Estadísticas por variable
nombres_variables = ['temperatura', 'humedad', 'viento', 'lluvia', 'festivo', 'fin_semana', 'alquileres']
for i, nombre in enumerate(nombres_variables):
    columna = datos_cargados[:, i]
    media = np.mean(columna)
    std = np.std(columna)
    minimo = np.min(columna)
    maximo = np.max(columna)
    print(f"{nombre}: media={media:.2f}, std={std:.2f}, min={minimo:.2f}, max={maximo:.2f}")

### Fase 2: Limpieza
# 1. Comprobad si hay valores NaN: `np.isnan(datos).sum()`
nan_count = np.isnan(datos_cargados).sum()
print(f"Número de valores NaN: {nan_count}")
# 2. Aplicad clip a las variables continuas para eliminar outliers extremos
print("\n--- Verificando valores modificados por clip ---")

# Temperatura [-5, 40]
print(f"Temperatura: {(temperatura<-5).sum()} valores < -5, {(temperatura>40).sum()} valores > 40")

# Humedad [15, 100]
print(f"Humedad: {(humedad<15).sum()} valores < 15, {(humedad>100).sum()} valores > 100")

# Viento [0, 50]
print(f"Viento: {(viento<0).sum()} valores < 0, {(viento>50).sum()} valores > 50")

# Lluvia [0, 40]
print(f"Lluvia: {(lluvia<0).sum()} valores < 0, {(lluvia>40).sum()} valores > 40")

temperatura_limpio = np.clip(temperatura, -5, 40)
humedad_limpio = np.clip(humedad, 15, 100)
viento_limpio = np.clip(viento, 0, 50)
lluvia_limpio = np.clip(lluvia, 0, 40)

# 1. Dividid en train (80%) y test (20%)
n = len(temperatura)
index = int(n * 0.8)

temp_train, temp_test = temperatura[:index], temperatura[index:]
hum_train, hum_test = humedad[:index], humedad[index:]
viento_train, viento_test = viento[:index], viento[index:]
lluvia_train, lluvia_test = lluvia[:index], lluvia[index:]
festivo_train, festivo_test = festivo[:index], festivo[index:]
finsem_train, finsem_test = fin_semana[:index], fin_semana[index:]

print(f"\nTamaño train: {len(temp_train)}, tamaño test: {len(temp_test)}")


temp_train_mean = np.mean(temp_train)
temp_train_std = np.std(temp_train)
print(f"temp_train_mean={temp_train_mean}, temp_train_std={temp_train_std}")

# 2. Calculad la media y std de cada feature SOLO con datos de train
temp_train_mean = np.mean(temp_train)
temp_train_std = np.std(temp_train)
print(f"Train temperatura: Media = {temp_train_mean} std = {temp_train_std}")
hum_train_mean = np.mean(hum_train)
hum_train_std = np.std(hum_train)
print(f"Train humedad: Media = {hum_train_mean} std = {hum_train_std}")
viento_train_mean = np.mean(viento_train)
viento_train_std = np.std(viento_train)
print(f"Train viento: Media = {viento_train_mean} std = {viento_train_std}")
lluvia_train_mean = np.mean(lluvia_train)
lluvia_train_std = np.std(lluvia_train)
print(f"Train lluvia: Media = {lluvia_train_mean} std = {lluvia_train_std}")

# Normalizad train y test usando las estadísticas de train:
temp_train_norm = (temp_train - temp_train_mean) / temp_train_std
temp_test_norm = (temp_test - temp_train_mean) / temp_train_std
print(f"Train: media={temp_train_norm.mean():.2f}, std={temp_train_norm.std():.2f}")
hum_train_norm = (hum_train - hum_train_mean) / hum_train_std
hum_test_norm = (hum_test - hum_train_mean) / hum_train_std
print(f"Train: media={hum_train_norm.mean():.2f}, std={hum_train_norm.std():.2f}")
viento_train_norm = (viento_train - viento_train_mean) / viento_train_std
viento_test_norm = (viento_test - viento_train_mean) / viento_train_std
print(f"Train: media={viento_train_norm.mean():.2f}, std={viento_train_norm.std():.2f}")
lluvia_train_norm = (lluvia_train - lluvia_train_mean) / lluvia_train_std
lluvia_test_norm = (lluvia_test - lluvia_train_mean) / lluvia_train_std
print(f"Train: media={lluvia_train_norm.mean():.2f}, std={lluvia_train_norm.std():.2f}")

# Construir X_train: columna de 1s + features normalizadas
X_train = np.column_stack([
    np.ones(len(temp_train)),      # intercepto
    temp_train_norm,               # temperatura normalizada
    hum_train_norm,                # humedad normalizada
    viento_train_norm,             # viento normalizado
    lluvia_train_norm,             # lluvia normalizada
    festivo_train,                 # festivo (categórico)
    finsem_train                   # fin de semana (categórico)
])

# Construir X_test con la misma estructura
X_test = np.column_stack([
    np.ones(len(temp_test)),       # intercepto
    temp_test_norm,                # temperatura normalizada
    hum_test_norm,                 # humedad normalizada
    viento_test_norm,              # viento normalizado
    lluvia_test_norm,              # lluvia normalizada
    festivo_test,                  # festivo (categórico)
    finsem_test                    # fin de semana (categórico)
])

# Construir y_train e y_test
y_train = target[:index]
y_test = target[index:]

print(f"\nX_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

'''
Fase 6: Simulación
Escenario: Se prevé una ola de calor para la próxima semana. Queréis estimar la demanda esperada para un día con temperatura alta pero incierta.

Definid el escenario:

Temperatura esperada: 35°C con incertidumbre de 3°C
Humedad: 40% (fija)
Viento: 5 km/h (fijo)
Lluvia: 0 mm (fijo)
Día laborable normal
Generad 10000 escenarios de temperatura:

Normalizad las temperaturas simuladas con las estadísticas de train

Construid X para cada escenario y calculad predicciones

Calculad percentiles 5, 50 y 95

Responded en comentarios:

¿Cuántas bicicletas debería preparar operaciones si quiere cubrir el 95% de los escenarios?
¿Cuál es el rango de incertidumbre (P95 - P5)?
¿Es un rango aceptable para planificación?
'''
#1 Definid el escenario
temp_esperada = 35
temp_incertidumbre = 3
humedad_fija = 40
viento_fijo = 5
lluvia_fija = 0
festivo_fijo = 0
finsem_fijo = 0
#2 Generad 10000 escenarios de temperatura
n_escenarios = 10000
temp_simulada = np.random.normal(temp_esperada, temp_incertidumbre, n_escenarios)
# Normalizad las temperaturas simuladas
temp_simulada_norm = (temp_simulada - temp_train_mean) / temp_train_std
# Construid X para cada escenario
X_escenarios = np.column_stack([
    np.ones(n_escenarios),
    temp_simulada_norm,
    np.full(n_escenarios, (humedad_fija - hum_train_mean) / hum_train_std),
    np.full(n_escenarios, (viento_fijo - viento_train_mean) / viento_train_std),
    np.full(n_escenarios, (lluvia_fija - lluvia_train_mean) / lluvia_train_std),
])
# 5. Calculad percentiles 5, 50 y 95
# Supongamos coeficientes de regresión entrenados (aleatorios para este ejemplo)
coeficientes = np.array([2200, 45, -8, -15, -40, -300, 400])
predicciones = X_escenarios @ coeficientes
p5 = np.percentile(predicciones, 5)
p50 = np.percentile(predicciones, 50)
p95 = np.percentile(predicciones, 95)
"""
- Ejercicio 4: Configuración de arquitecturas de red (TUPLAS)

    Las dimensiones de tensores en redes neuronales se representan típicamente como tuplas inmutables. Debes trabajar con arquitecturas de diferentes redes convolucionales.
"""
resnet50_shape = (32, 224, 224, 3)  # batch_size, height, width, channels
mobilenet_shape = (16, 192, 192, 3)
vgg16_shape = (64, 224, 224, 3)

"""
1. Extrae mediante unpacking los valores de batch_size, height, width y channels de cada arquitectura.
2. Calcula el número total de píxeles que procesa cada modelo en un batch completo. Fórmula: `batch_size * height * width * channels`
3. Crea una función que retorne una tupla con la información: `(nombre_modelo, total_pixeles, ratio_aspecto)` donde ratio_aspecto = `height / width`
4. Genera una lista de tuplas ordenada por número total de píxeles procesados, de menor a mayor. Cada tupla debe contener `(nombre_modelo, total_pixeles)`.
5. Implementa una función que reciba una tupla de dimensiones y retorne una nueva tupla con las dimensiones duplicadas (útil para upsampling). Ejemplo: `(32, 112, 112, 3)` → `(32, 224, 224, 3)`
"""

def calcular_carga_computacional(model_name: str, shape: tuple) -> tuple:
    """Retorna (nombre_modelo, total_pixeles, ratio_aspecto)"""
    
    batch_size, height, width, channels = shape

    total_pixeles = batch_size * height * width * channels

    ratio_aspecto = height / width

    return (model_name, total_pixeles, ratio_aspecto)
    pass

def duplicar_resolucion(shape: tuple) -> tuple:
    """Duplica height y width manteniendo batch_size y channels"""

    batch_size, height, width, channels = shape

    return (batch_size, height * 2, width * 2, channels)
    pass

# 1. Unpacking de dimensiones
resnet50_bs, resnet50_h, resnet50_w, resnet50_c = resnet50_shape
print(f"ResNet50 -> Batch Size: {resnet50_bs}, Height: {resnet50_h}, Width: {resnet50_w}, Channels: {resnet50_c}")
mobilenet_bs, mobilenet_h, mobilenet_w, mobilenet_c = mobilenet_shape
print(f"MobileNet -> Batch Size: {mobilenet_bs}, Height: {mobilenet_h}, Width: {mobilenet_w}, Channels: {mobilenet_c}")
vgg16_bs, vgg16_h, vgg16_w, vgg16_c = vgg16_shape
print(f"VGG16 -> Batch Size: {vgg16_bs}, Height: {vgg16_h}, Width: {vgg16_w}, Channels: {vgg16_c}")

print()

# 2. Cálculo de píxeles procesados por batch
resnet50_pixels = resnet50_bs * resnet50_h * resnet50_w * resnet50_c
print(f"ResNet50 -> Píxeles por batch: {resnet50_pixels}")
mobilenet_pixels = mobilenet_bs * mobilenet_h * mobilenet_w * mobilenet_c
print(f"MobileNet -> Píxeles por batch: {mobilenet_pixels}")
vgg16_pixels = vgg16_bs * vgg16_h * vgg16_w * vgg16_c
print(f"VGG16 -> Píxeles por batch: {vgg16_pixels}")

print()

# 3. Información de cada modelo
resnet50 = calcular_carga_computacional("ResNet50", resnet50_shape)
print(f"ResNet50 Info: {resnet50}")
mobilenet = calcular_carga_computacional("MobileNet", mobilenet_shape)
print(f"MobileNet Info: {mobilenet}")
vgg16 = calcular_carga_computacional("VGG16", vgg16_shape)
print(f"VGG16 Info: {vgg16}")

print()

# 4. Lista ordenada por píxeles procesados
modelos_pixeles = [
    (resnet50_pixels, "ResNet50"),
    (mobilenet_pixels, "MobileNet"),
    (vgg16_pixels, "VGG16")
]

modelos_pixeles.sort()

print("Modelos ordenados por píxeles procesados (menor a mayor):")
for total_pixeles, nombre_modelo in modelos_pixeles:
    print(f"{nombre_modelo}: {total_pixeles} píxeles")

print()

# 5. Duplicar dimensiones de tuplas
resnet50_duplicado = duplicar_resolucion(resnet50_shape)
print(f"ResNet50 dimensiones duplicadas: {resnet50_duplicado}")
mobilenet_duplicado = duplicar_resolucion(mobilenet_shape)
print(f"MobileNet dimensiones duplicadas: {mobilenet_duplicado}")
vgg16_duplicado = duplicar_resolucion(vgg16_shape)
print(f"VGG16 dimensiones duplicadas: {vgg16_duplicado}")
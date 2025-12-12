"""
Ejercicio 1: Sistema de Alertas de Temperatura
Un datacenter de Amazon necesita detectar cuando la temperatura de un servidor supera 75°C durante 10 minutos consecutivos (lecturas cada minuto). Si esto ocurre, activar alerta de enfriamiento.

Datos: Lista de tuplas (timestamp, temperatura)

Pistas
¿Qué patrón reconoces? (Ventana deslizante de confirmación)
¿Qué estructura usarías? (Lista para mantener orden temporal)
¿Qué validaciones necesitas? (Mínimo 10 lecturas, valores numéricos válidos)
¿Cómo manejas lecturas perdidas? (Saltos en timestamps)
"""
def detectar_alerta_temperatura(lecturas: list) -> dict:

    contador = 0
    umbral = 75

    for i in range(1, len(lecturas)):
        timestamp, temp = lecturas[i]

        if temp > umbral:
            contador += 1

            if contador >= 10:
                return {
                        "alerta": True,
                        "inicio_alerta": lecturas[i - 9][0]
                        }
            
        else:
            contador = 0
        
    return {
            "alerta": False,
            "inicio_alerta": None
            }

# Caso de uso
lecturas = [
    (1638360000, 72),
    (1638360010, 77),
    (1638360020, 74),
    (1638360030, 76),
    (1638360040, 77),
    (1638360050, 78),
    (1638360060, 79),
    (1638360070, 80),
    (1638360080, 81),
    (1638360090, 82),
    (1638360100, 83),
    (1638360110, 84),
    (1638360120, 85),
    (1638360130, 86),
]

alerta_temperatura = detectar_alerta_temperatura(lecturas)
print(f"Alerta: {alerta_temperatura['alerta']}")
print(f"Inicio: {alerta_temperatura['inicio_alerta']}")
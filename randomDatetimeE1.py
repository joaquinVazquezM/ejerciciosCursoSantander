import random
from datetime import datetime

# Lista de saludos aleatorios
saludos = ["¡Hola!", "¡Buenos días!", "¡Buenas tardes!", "¡Buenas noches!", "¡Qué tal!"]

# Generar un saludo aleatorio
saludo_aleatorio = random.choice(saludos)

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Imprimir el saludo aleatorio y la fecha y hora actual
print(f"{saludo_aleatorio} La fecha y hora actuales son: {fecha_actual}")

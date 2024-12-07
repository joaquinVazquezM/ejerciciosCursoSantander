# Definir cadenas de texto
nombre = "Juan"
apellido = 'Pérez'
curso = "Programación en Python"

# Mostrar las cadenas
print("Cadenas de texto:")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Curso:", curso)

# Concatenación de cadenas
nombre_completo = nombre + " " + apellido
print("\nConcatenación:")
print("Nombre completo:", nombre_completo)

# Repetición de cadenas
print("\nRepetición:")
print("Nombre repetido 3 veces:", nombre * 3)

# Corte de cadenas (slicing)
print("\nCorte de cadenas:")
print("Primeras 3 letras del nombre:", nombre[:3])
print("Últimas 3 letras del curso:", curso[-3:])

# Métodos de cadenas
print("\nMétodos de strings:")
print("Nombre en mayúsculas:", nombre.upper())
print("Apellido en minúsculas:", apellido.lower())
print("Curso en título:", curso.title())

# Longitud de cadenas
print("\nLongitud de cadenas:")
print("Longitud del nombre:", len(nombre))
print("Longitud del apellido:", len(apellido))
print("Longitud del curso:", len(curso))

# Búsqueda en cadenas
print("\nBúsqueda en cadenas:")
print("¿Contiene 'Python' el curso?", "Python" in curso)
print("Posición de 'Python' en el curso:", curso.find("Python"))

# Reemplazo de cadenas
print("\nReemplazo de cadenas:")
curso_modificado = curso.replace("Python", "Programación")
print("Curso modificado:", curso_modificado)
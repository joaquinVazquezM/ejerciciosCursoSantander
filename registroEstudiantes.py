# Captura de Datos del Estudiante
nombre = input("Ingrese el nombre completo del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
altura = float(input("Ingrese la altura del estudiante (en metros): "))

# Captura de Calificaciones
print("\nIngrese las calificaciones:")
calificacion1 = float(input("Calificación de Matemáticas: "))
calificacion2 = float(input("Calificación de Ciencias: "))
calificacion3 = float(input("Calificación de Literatura: "))

# Cálculos
promedio = (calificacion1 + calificacion2 + calificacion3) / 3
calificacion_maxima = max(calificacion1, calificacion2, calificacion3)
calificacion_minima = min(calificacion1, calificacion2, calificacion3)

# Mensaje Personalizado
if promedio >= 9:
    mensaje_rendimiento = "¡Excelente rendimiento académico!"
elif promedio >= 7:
    mensaje_rendimiento = "Buen trabajo, sigue esforzándote."
else:
    mensaje_rendimiento = "Necesitas mejorar tu desempeño."

# Reporte Completo
print("\n--- REPORTE DEL ESTUDIANTE ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura:.2f} metros")
print("\nCalificaciones:")
print(f"Matemáticas: {calificacion1}")
print(f"Ciencias: {calificacion2}")
print(f"Literatura: {calificacion3}")
print(f"\nPromedio: {promedio:.2f}")
print(f"Calificación Máxima: {calificacion_maxima}")
print(f"Calificación Mínima: {calificacion_minima}")
print(f"\n{mensaje_rendimiento}")
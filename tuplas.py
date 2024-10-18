#Creación de tuplas, se encierra los elementos entre paréntesis
punto = (3, 4)

#Acceso a tuplas, utiliza el indice de los elementos entre corchetes
print(punto[0])
print(punto[1])
print("\n------------------------------------------------------------------")
#Métodos en tuplas
mi_tupla = (1, 2, 3, 2, 4, 2)


# Método count
print("---------------------------------------")
print("Método count")
print("---------------------------------------")
print(mi_tupla.count(2))  # Salida: 3
print("---------------------------------------")

# Método index
print("---------------------------------------")
print("Método index")
print("---------------------------------------")
print(mi_tupla.index(3))  # Salida: 2
print(mi_tupla.index(2))
print(mi_tupla.index(2, 2))
print(mi_tupla.index(2, 2, 4))
print("---------------------------------------")
# Función len
print("---------------------------------------")
print("Método len")
print("---------------------------------------")
print(len(mi_tupla))  # Salida: 6
print("---------------------------------------")


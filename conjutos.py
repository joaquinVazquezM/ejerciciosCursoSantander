#Creación y operaciones básicas
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])
#Los conjuntos admiten operaciones matemáticas de conjuntos, como la unión (|), la intersección (&), la diferencia (-) y la diferencia simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
#Union
union = conjunto1 | conjunto2
print(union)
print("-----------------------------------")
#intersección
interseccion = conjunto1 & conjunto2
print(interseccion) 
print("-----------------------------------")
#diferencia
diferencia = conjunto1 - conjunto2
print(diferencia) 
print("-----------------------------------")
#diferencia simetrica
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica) 
print("-----------------------------------")


frutas = ["manzana", "banana", "naranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

#Métodos de listas
#append(elemento): Agrega un elemento al final de la lista
frutas.append("pera")
print(frutas)
#insert(indice, elemento): inserta un elemento en una posición específica de la lista.
frutas.insert(0,"Tuna")
print(frutas)
#remove(elemento): elimina la primera aparición de un elemento en la lista.
frutas.remove("banana")
print(frutas)
#pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
frutas.pop(2)
print(frutas)
#sort(): ordena los elementos de la lista en orden ascendente.
print(frutas)
#reverse(): invierte el orden de los elementos en la lista
frutas.reverse()
print(frutas)

cantidad_elementos = len(frutas)
print(cantidad_elementos)
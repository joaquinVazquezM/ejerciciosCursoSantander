# Definición y llamado de la función
def saludo():
    print("¡Hola, mundo!")


saludo()

# Paramentros y argumentos: Los parámetros se especifican dentro de los paréntesis en la definición de la función.
def saludo_nombre(nombre):
    print(f"Hola, {nombre}")

# Proporcionamos los argumentos correspondientes a los parámetros
saludo_nombre("Juan")
saludo_nombre("Maria")
saludo_nombre("Mer")

#Ejemplo con varios parametros
def sumar(a, b):
    resultado = a + b
    print(f"La suma es: {resultado}")

sumar(23, 23)
sumar(34, 54)
sumar(345, 5643)

#Valores de retorno
def suma(a, b):
    return a + b


resultado_suma = suma(234, 23)
print(resultado_suma)

def multiplicar(a, b):
    return a * b

resultado_multiplicar = multiplicar(12, 23)
print(f"El resultado de la multiplicación es:\t {resultado_multiplicar}")

#Ejemplo
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatura_f = celsius_a_fahrenheit(28)
print(f"La temperatura en grados fahrenheit es:\t {temperatura_f}")

#Funciones lambda:  es una función anónima (sin nombre) de una línea
cuadrado = lambda x: x ** 2
print(cuadrado(5))

#Ejemplo - suma de dos números
suma_1 = lambda a, b: a + b
print(suma_1(4, 5))

#Otro ejemplo lambda - convertir a mayusculas
mayusculas = lambda texto: texto.upper()
print(mayusculas("Joaquin Vázquez"))

#Lambda - multiplicar por 2
doble = lambda x: x * 2
print(doble(9))

# Alcance de variables - local y global
def funcion():
    variable_local = 19
    print(f"Esta es una varibale local\n {variable_local}") #Accesible unicamente dentro de la función


variable_global = 12

def funcion_2():
    print(f"Esta es una varibale local\n {variable_global}") # Accesible desde cualquier lugar

funcion()
funcion_2()
print(f"Imprime la variable goblal \n {variable_global}")
#print(variable_local) - Esto es un error

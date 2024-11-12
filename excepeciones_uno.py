try:
    # Pedimos al usuario que ingrese un número
    numero = input("Ingrese un número: ")
    
    # Intentamos convertir a entero y hacer cálculos
    numero = int(numero)
    resultado = 100 / numero
    
    print(f"100 dividido por {numero} es: {resultado}")

except ValueError:
    print("Error: Debe ingresar un número válido")
    
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
    
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    
else:
    print("¡El cálculo se realizó exitosamente!")
    
finally:
    print("Fin del programa")
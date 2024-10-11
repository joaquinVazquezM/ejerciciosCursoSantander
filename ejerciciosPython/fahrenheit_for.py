#Tabla de conversión de f° a c° de 0 hasta 20
print("f°       c°")
for temp in range(21):
    print(temp,"      ",int((temp-32)*5/9))
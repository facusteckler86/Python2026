
numero = int (input("Ingresa un numero y 0 para salir: "))
suma_total= 0

while numero != 0:
    suma_total +=numero
    numero = int(input("Ingrese un numero (0 para seguir): "))
else:
    print("La suma total es ", suma_total)



# Uso de range

altura = int(input("Ingrese la altura: "))

for altura in range(1,altura+1):
    print("*" * altura)
#ejercicios de listas (21/04/2026)

lista1=[1,2,3,4]
lista2=["Bye", "ciao", "Agur", "Adieu"]

lista1.append(1234)
lista2.append("Hola")

print(lista1)
print(lista2)

lista2 +=[1234,"Adios"]

lista3=lista1[:-1]

print(lista3)

lista4=lista2[1:-1]
print(lista4)

lista5 = lista2 + lista3
print(lista5)

# /* 
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
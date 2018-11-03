#Definir Variables

lista1 = []
lista2 = []

#Explicacion al usuario de algoritmo

print ("Algoritmo que le pide al usuario numeros y los almacena")
print ("en una lista, luego nuevamente pide numeros para")
print ("almacenarlos. El algoritmo finaliza en 0")

#Pedir numeros al usuario

print ("\nIngrese un numero positivo")
x = int (input())
lista1.append(x)

#Verificar el 0

while x != 0:
    print ("\nIngrese un numero positivo")
    x = int (input())
    lista1.append(x)

#Finalizar lista 1

print ("\nFin de la lista 1")

#Iniciar lista 2. Pedir numeros al usuario

print ("\nIngrese un numero positivo")
y = int (input())
lista2.append(y)

#Verificar el 0

while y != 0:
    print ("\nIngrese un numero positivo")
    y = int (input())
    lista1.append(y)

#Sumar listas

print ("\nLa suma de las listas es:")
print (lista1+lista2)




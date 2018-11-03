#Definir Variables

lista = []

#Explicacion de algoritmo

print ("Algoritmo que pide al usuario el ingreso de una cierta")
print ("cantidad de numeros definidos por él. Estos seran ordenados")
print ("de mayor a menor")

#Preguntaral usuario cuantos numeros va a ingresar

print ("\nCuantos numeros va a ingresar")
n = int (input())

#Verificar que el numero sea positivo:

while n < 0:
    print ("Error, el numero debe ser positivo")
    print ("\nCuantos numeros va a ingresar")
    n = int (input())

#Almacenar Variables

m = n

#Pedir numeros al usuario

print (" ")
while n > 0:
    print ("Ingrese un numero")
    x = int (input())
    lista.append(x)
    n = n - 1

#Realizar el orden de tipo QuickSort


for i in range (1,m):
    for j in range (0, m - i):
        if lista [j] > lista [j + 1]:
            t = lista [j]
            lista [j] = lista [j + 1]
            lista [j + 1] = t

#Mostrar variables ordenadas al usuario

for k in (lista):
    print (k, end =" ")

#Definir Variables

lista1 = []
c = 1

#Definicion de algoritmo al usuario

print ("Algorimo que lee la cantidad de numeros positivos ingresados por el")
print ("usuario, y determina cual es el menor y mayor de ellos")

#Pedir numeros al usuario

print ("\nIngrese la cantidad de numeros que desea comparar:")
d = int (input())

#Validar que el numero sea positivo

while d < 0:
    print ("\Error!, el numero de debe ser positivo:")
    print ("\nIngrese la cantidad de numeros que desea comparar:")
    d = int (input())

#Pedir al usuario los numeros dictados que desea

for l in range (d):
    print ("\nIngrese su numero", c, ":")
    x = int (input())
    lista1.append(x)
    c = c + 1

#Ordenar la lista a traves de QuickSort

for i in range (1, len(lista1)):
    for j in range (0, len(lista1) - i):
        if lista1[j] > lista1[j + 1]:
            t = lista1[j]
            lista1[j] = lista1[j + 1]
            lista1[j + 1] = t

#Decirle al usuario que numero es menor

print ("\nEl numero menor es:", lista1[0])
print ("El numero mayor es:", lista1[len(lista1) - 1])

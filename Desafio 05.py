#Definir Variables

lista1 = []
lista2 = []
lista3 = []
a = 4
c = 0

#Descripcion de algoritmo al usuario

print ("Algoritmo que pide el ingreso de 4 numeros al usuario para formar")
print ("una lista, y luego nuevamente pide el ingreso de 4 numeros mas")
print ("para formar otra lista. Estas listas se sumaran y formaran una")
print ("nueva, la cual estara ordenada")

#Pedir numeros al usuario para la primera lista

print ("\nIngrese los 4 primeros numeros de la primera lista:")
print (" ")
for i in range (a):
    print ("Ingrese su numero:")
    x = int (input())
    lista1.append(x)

#Pedir numeros al usuario para la segunda lista

print ("\nIngrese los 4 primeros numeros de la segunda lista:")
print (" ")
for j in range (a):    
    print ("Ingrese su numero:")
    y = int (input())
    lista2.append(y)

#Sumar listas

while c < a:
    lista3.append(lista1[c])
    lista3.append(lista2[c])
    c = c + 1

#Mostras al usuario la lista sin ordenar

print ("Esta es su lista sin ordenar:")
for k in (lista3):
    print (k, end=" ")

#Ordenar la lista de tipo QuickSort:

for l in range (1,a*2):
    for m in range (0, a*2 - l):
        if lista3 [m] > lista3 [m + 1]:
            t = lista3 [m]
            lista3 [m] = lista3 [m + 1]
            lista3 [m + 1] = t

#Mostrar al usuario la lista ordenada

print (" ")
print ("Esta es su lista ordenada")
for n in (lista3):
    print (n, end=" ")

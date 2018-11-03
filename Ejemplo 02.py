#Definir Variables

lista = []

#Explicacion de algoritmo al usuario

print ("Algoritmo que pide al usuario numeros y los almacena")
print ("Para luego mostrarlo. El proceso se termina con '0'")

#Pedir numero al usuario

print ("\nIngrese un numero")
x = int (input())
lista.append(x)

#Verificar termino con 0

while x != 0:
    print ("Ingrese un numero")
    x = int (input())
    lista.append(x)
#Mostrar numeros ingresados por el usuario Forma #1

print (" ")
print (lista)
print (" ")

#Mostrar numeros ingresados por el usuario Forma #2

for i in (lista):
    print (i, end=" ")

#Explicacion de algoritmo al usuario

print ("Algoritmo que pide un numero positivo al usuario,")
print ("entrega la cantidad de divisores y dice cuales son.")
print (" ")

#Pedir al usuario el numero

print ("Ingrese un numero par y positivo")
nuser = int (input())

while nuser <= 0 or nuser%2==1: 
    print ("Error, el numero debe ser par y positivo")
    print (" ")
    print ("Ingrese un numero par y positivo")
    nuser = int (input())

#Variable

a = 0
b = 0

#Ver cantidad de divisores existentes

while nuser != a:
    a = a + 1
    if nuser%a == 0:
        b = b + 1

print ("El numero contiene", b, "Divisores")

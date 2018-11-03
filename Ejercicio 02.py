#Definir al usuario el contenido del algoritmo

print ("Algoritmo que cuenta cuantos numeros pares e impares ingresa el usuario.")
print (" ")

#Definir las variables

a = 0 #Variable para num. pares
b = 0 #Variable para num. impares

#Pedir al usuario que ingrese los numeros que desee

print ("Ingrese los numeros que desee. Finalice con el numero '0':")
nuser = int (input())

#Cuando el numero del usuario es distino de 0

while nuser != 0:

#Realizar la comparacion de pares e impares

    if nuser%2 == 0:
        a = a + 1
    else:
        b = b + 1

#Volver a pedir un numero

    print ("Ingrese nuevamente los numeros que desee. Finalice con el numero '0':")
    nuser = int (input())

#Definir al usuario la cantidad de numeros pares e impares

print ("La cantidad de numeros pares es:", a)
print ("La cantidad de numeros impares es:", b)
print ("El total de numeros ingresados es:", a + b)

#Explicacion de algoritmo al usuario

print ("Algoritmo que calcula el factorial del numero que desee.\n")

#Pedir numero al usuario

print ("Ingrese un numero positivo:")
x = int (input())

#Comprobar que sea positivo

while x < 1:
    print ("\nError, volver a ingresar el numero")
    x = int (input())

#Designar Variables

y = x
f = x

#Realizar operacion

while x > 1:
    x = x - 1
    a = y*x
    y = a

print ("\nEl factorial de", f, "es:", y)

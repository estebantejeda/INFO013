#Variables

y = ''

#Breve explicacion de algoritmo al usuario

print ("Algoritmo que imprime una triangulo rectangulo, de alto")
print ("segun el numero que ingrese el usuario")

#Pedir numero al usuario

print ("\nIngrese un numero positivo")
x = int (input())

#Validar si el numero ingresado es positivo

while x < 0:
    print ("\nError, el numero debe ser positivo")
    print ("\nIngrese un numero positivo")
    x = int (input())

#Realizar el 'for' para los asteriscos

print ("\nEl triangulo de alto", x, "es:\n")
for i in range (0, x):
    y = y + '*'
    print (y)

    
    

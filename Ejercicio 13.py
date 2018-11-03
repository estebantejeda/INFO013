#Definir Variables

c = 1

#Explicacion de algorimo al usuario

print ("Algoritmo que pide al usuario que ingrese tres numeros")
print ("y determina cual de estos es el mayor")

#Pedir al usuario los numeros

print ("\nIngrese el numero", c, ":")
x = int (input())
c = c + 1

print ("\nIngrese el numero", c, ":")
y = int (input())
c = c + 1

print ("\nIngrese el numero", c, ":")
z = int (input())
print (" ")

#Realizar la comprobacion de que numero es menor y decirle al usuario
#que numero es mayor

if x > y and x > z:
    print (x, " es el mayor")

if y > x and y > z:
    print (y, " es el mayor")

if z > y and z > x:
    print (z, " es el mayor")

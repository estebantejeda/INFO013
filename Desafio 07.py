#Definir Variables #1

lista1 = []
lista2 = []
e = 0
f = 0

#Definion al usuario de algoritmo

print ("Algortimo que le pide dos numeros al usuario y calcula si estos")
print ("son amigos")

#Pedir primer numero al usuario

print ("\nIngrese el primer numero positivo:")
x = int(input())

#Verificar que el numero sea positivo

while x < 0:
    print ("\nError, el numero debe ser Positivo")
    print ("\nIngrese el primer numero:")
    x = int(input())

#Pedir segundo numero al usuario

print ("\nIngrese el segundo numero positivo:")
y = int(input())

#Verificar que el numero sea positivo

while y < 0:
    print ("\nError, el numero debe ser Positivo")
    print ("\nIngrese el segundo numero:")
    y = int(input())

#Definir Variables #2

a = x
b = y

#Almacenar los divisores de la variable 'x'

while a != 0:
    if x%a == 0:
        lista1.append(a)
        e = e + a
        a = a - 1
    else:
        a = a - 1

#Almacenar los divisores de la variable 'y'

while b != 0:
    if y % b == 0:
        lista2.append(b)
        f = f + b
        b = b - 1
    else:
        b = b - 1

#Definir Variables #3

e = e - x
f = f - y

#Mostrar al usuario los divisores del primer numero

print ("\nLos divisores de", x, "son:")
for i in (lista1):
    print (i, end=" - ")
print ("\nSuma:", e)

#Mostrar al usuario los divisores del segundo numero

print ("\nLos divisores de",y, "son:")
for j in (lista2):
    print (j, end=" - ")
print ("\nSuma:", f)

#Realizar comparacion y demostrar al usuario si los numeros son amigos

if x == f and y == e:
    print ("\nLos numeros", x, "y", y, "son amigos")
else:
    print ("\nLos numeros", x, "y", y, "no son amigos")

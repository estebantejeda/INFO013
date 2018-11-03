#Definir Variables

y = 0
i = 0

#Breve explicacion del algoritmo al usuario

print ("Algoritmo que suma todos los numeros positivos anteriores al numero")
print ("ingresado por el usuario")

#Pedir al usuario un numero

print ("\nIngrese un numero positivo")
x = int (input())

#Verificar si es positivo

while x < 0:
    print ("\nError, el numero debe ser positivo")
    print ("\nIngrese un numero positivo")
    x = int (input())

#Realizar la suma

for i in range (1, x):
    y = y + i

print ("\nLa suma es:", i+y+1)

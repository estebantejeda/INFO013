#Explicacion al usuario del algoritmo

print ("Algoritmo que resuelve la sumatoria de forma (2 + i)")
print (" ")

#Definir Variables

a = 1
s = 0

#Pedir al usuario el numero con el que desea realizar la sumatoria

print ("Ingrese el numero con el que desea iniciar la sumatoria (Debe ser positivo):")
n = int (input())

#Verificar que 'n' es positivo

while n<1:
    print ("El numero DEBE SER POSITIVO")
    print (" ")
    print ("Ingrese el numero con el que desea iniciar la sumatoria (Debe ser positivo):")
    n = int (input())

#Realizar la suma

while a <=n:
    s = s+(2+a)
    a = a+1

print ("El resultado es:", s)

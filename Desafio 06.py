#Definir variables

lista1 = []

#Breve explicacion al usuario de algoritmo

print ("Algoritmo que pide un numero al usuario y lo invierte")

#Pedir un numero al usuario

print ("\nIngrese un numero dentro del rango [0,100000]")
n = int (input())

#Comprobar que pertenezca al rango [0, 100000]

while n <= 0 or n >= 100000:
    print ("\nError!, el numero debe estar entre 0 y 100000")
    print ("Ingrese un numero dentro del rango [0,100000]")
    n = int (input())

#Definir variables

a = len (str (n))
b = n

#Almacenar en una lista

while a != 0:
    x = b%10
    lista1.append(x)
    b = b // 10
    a = a - 1

#Mostrar numero invertido
    
print ("\nSu numero invertido es:")
for i in (lista1):
    print (i, end="")

#Definir explicacion de algoritmo al usuario

print ("Algoritmo que le pide al usuario que ingrese un numero positivo")
print ("e imprima los siguientes 5 numeros enteros")

#Pedir numero al usuario

print ("\nIngrese un numero entero positivo")
x = int (input())

#Validar numeracion

while x < 0:
    print ("\nError, debe ser un numero positivo")
    print ("\nIngrese un numero entero positivo")
    x = int (input())

#Realizar el rango y mostrar los numeros que continuan

print ("Los siguientes 5 numeros de", x, "son:")
for i in range (x+1, x+6):  
    print (i, end = " ")

#Definir Variables

lista = []

#Preguntar al usario

print ("Ingrese un numeros")

#Almacenar datos de usuario

x = int (input())
lista.append(x)

#Verificar el 0

while x != 0:
    print ("Ingrese un numeros")
    x = int (input())
    lista.append(x)

#Imprimir Numeros

print (lista)

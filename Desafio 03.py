#Definicion del algoritmo al usuario

print ("Algoritmo que muestra los numeros impares positivos hasta")
print ("el numero ingresado.")

#Activar forma ciclica

ciclica = True
while ciclica:

#Pedir numero al usuario

    print ("\nIngrese un numero positivo no mayor que 50")
    n = int (input())

#Verificar que el numero cumpla los requisitos

    while n < 0 or n > 50:
        print ("\nError, el numero debe ser positivo y no")
        print ("puede ser mayor que 50.\n")
        print ("Vuelva a intentarlo.\n")
        print ("Ingrese un numero positivo no mayor que 50")
        n = int (input())

#Definir Variable

    a = 1

#Calcular de los impares positivos
    print ("\nLos numeros impares de", n, "son: \n")
    while a - 1 < n:
        if (a%2 != 0):
            print (a),
        a = a + 1

#Preguntar Ciclico

    resp = input("\n¿Volver a iniciar el algoritmo? [s/n]:")
    if resp== "n":
        ciclica = False
        print (" ")
        print ("Gracias por usar este algoritmo")    

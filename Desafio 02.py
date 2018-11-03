#Explicacion de algoritmo al usuario

print ("Algoritmo que calcula el promedio de las notas que usted desee.")

#Activar forma ciclica

ciclica = True
while ciclica:

#Definir Variable

    sn = 0
    
#Pedir al usuario la cantidad de notas que dese promediar

    print (" ")
    print ("¿Cuantas notas desea promediar?")
    np = int (input())

#Verificar que el numero ingresado sea positivo

    while np <= 1:
        print ("Error, el numero debe ser positivo y distinto de 1")
        print (" ")
        print ("Reitero. ¿Cuantas notas desea promediar?")
        np = int (input())

#Definir Variable

    x = np

#Preguntar las notas que desea promediar

    while np != 0:
        print ("Ingrese sus notas:")
        n = float (input())
        sn = sn + n
        np = np - 1

#Realiar el calculo de la nota

    pf = sn/x

#Dar resultado al usuario

    print ("Tu promedio de notas es", pf)
    print (" ")

#Preguntar Ciclico

    resp = input("¿Volver a iniciar el algoritmo? [s/n]:")
    if resp== "n":
        ciclica = False
        print (" ")
        print ("Gracias por usar este algoritmo")

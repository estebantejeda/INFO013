#Definir al usuario el contenido del Algoritmo

print ("Algoritmo que suma la cantidad de numeros que el usuario desee.")

#Activar forma ciclica

ciclica = True
while ciclica:

#Definir Variable Suma

    sumauser = 0

#Pedir la cantidad de numeros que quiere sumar

    print (" ")
    print ("Escriba la cantidad de numeros que desea sumar (Debe ser positivo):")
    nuser = int(input())

#Verificar que el número sea positivo

    while nuser <= 0:
        print ("Error, el numero debe ser positivo")
        print (" ")
        print ("Escriba la cantidad de numeros que sea sumar (DEBE SER POSITIVO):")
        nuser = int(input())

#Si el numero es positivo, preguntar los números que desea sumar

    while nuser != 0:
        print ("Ingrese el/los número/s que desea sumar")
        suser = int(input())
        sumauser = sumauser + suser
        nuser = nuser-1

#Demostrar el resultado de la suma

    print ("La suma de los números es:", sumauser)

#Preguntar si volver a realizar la suma

    resp = input("¿Volver a sumar? 'n', para salir: ")
    if resp== 'n':
        ciclica = False
        print("Adios")

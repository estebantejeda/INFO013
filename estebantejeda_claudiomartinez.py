ciclica = True
while ciclica:
    x=[]
    b=0
    print ("Ingrese el tamaño de la lista de numeros")
    num_list = int (input())
    while num_list == 0:
        print ("Error, el tamaño de la lista no puede ser 0\n")
        print ("Ingrese el tamaño de la lista de numeros")
        num_list = int (input())
    while b != num_list:
        print ("Ingrese un numero entre -30 y 30")
        num = int (input())
        while num > 30 or num < -30:
            print ("Error, el numero debe ser entre -30 y 30\n")
            print ("Ingrese un numero entre -30 y 30")
            num = int (input())       
        x.append (num)
        b = b + 1
    print (" ")
    print (x)
    resp = input("¿Volver a realizar la matriz? 'n', para salir: ")
    if resp== 'n':
        ciclica = False
        print("\nAdios")
    


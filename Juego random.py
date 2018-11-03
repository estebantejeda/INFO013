#Importar Random de la biblioteca

from random import randint

#Activar forma ciclica

booleana = True
while booleana:

#Pedir numero

    npc = randint (1,10)
    print ("Escribe un número del 1 al 10")
    nuser = int (input())

#Verificar que el número sea del 1 al 10

    while nuser > 10 or nuser < 1:
        print ("Numero invalido, debe ser entre 1 y 10")
        print ("Escribe un número del 1 al 10")
        nuser = int(input())

#Verificar igualdad y ver ganador

    if nuser == npc:
        print ("Ganaste")
    else:
        print ("Perdiste, el número era", npc)

#Preguntar si volver a jugar

    resp = input("¿Volver a jugar? 'no', para salir: ")
    print (" ")
    if resp== 'no':
        booleana = False
        print("chao")

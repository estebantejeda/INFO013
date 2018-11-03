#Pedir numero al usuario
#validar que el numero este entre 10 y 15
#pedir frase al usuario
#mostrar la frase n veces

#Pedir un numero

print ("Ingrese número del 10 al 15: ")
nuser = int (input())

#Verificar que el número sea del 10 al 15

while nuser > 15 or nuser < 10:
    print ("Numero invalido, debe ser entre 10 y 15")
    print ("Ingrese número del 10 al 15: ")
    nuser = int(input())

#Pedir frase al usuario

print ("Ingrese una frase")
fuser = input()
print (" ")

#Escribir la frase n veces

while nuser != 0:
    print (fuser)
    nuser = nuser - 1


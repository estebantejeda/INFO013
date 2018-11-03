def burbuja (A):
    for i in range (1, len(A)):
        for j in range (0, len(A)-i):
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
            print (A)
    return A

lista = [6, 4, 2, -5, -10, 5, -9, 1, 541, 12]
lista2 = [5, 3, 1, 0, 2, -8, 5, -52, 15, -52]

B = burbuja(lista)
C = burbuja(lista2)
print ("Otra lista: ", C)
print (B)

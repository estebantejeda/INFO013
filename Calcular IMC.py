#Pregunta Nombre

print ("¿Como te llamas?")
name = input ()
print ("Mucho gusto", name)
print (" ")

#Preguntar Edad

print("¿En que año naciste?")
año = int (input())
print("Tienes", 2014-año, "años")
print (" ")

#IMC

print ("Ahora calcularemos tu IMC")
print ("¿Cuanto pesas? (kg)")
peso = int (input())
print ("ahora tu estatura (m)")
estatura = float (input())

#Crear Varible

IMC = peso/(estatura*estatura)

print ("Tu IMC es", IMC )
print (" ")

#Respuesta con Rango

if IMC < 18.5:
    print ("Bajo peso")
    
elif IMC >= 18.5 and IMC <24.99:
    print ("Normal")

elif IMC >=25 and IMC <29.99:
    print ("Sobrepeso")

else:
    print ("Obeso")

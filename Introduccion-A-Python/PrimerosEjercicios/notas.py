# Vamos a hacer un programa que calcule una media de notas y determine si el alumno ha aprobado
# o si ha suspendido

n1 = int(input ("Introduce la primera nota: "))
n2 = int(input ("Introduce la segunda nota: "))
n3 = int(input ("Introduce la tercera nota: "))

promedio = ((n1 + n2 + n3) / 3)

if promedio >= 5:
    print ("¡Has aprobado con un: ", promedio,"!")
else:
    print ("Has suspendido con un: ", promedio)

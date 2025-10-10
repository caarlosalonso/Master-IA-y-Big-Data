# Programa que calcula si un numero es mayor, menor o igual que otro aleatorio, que finaliza cuando
# en n ocasiones dos numeros sean iguales

import random # Importa la libreria random para la generacion de numeros

i = 0 # Variable que lleva el recuento de cuantos números son iguales

while i <2: # Bucle que se ejecuta mientas i sea menor a 2

    # Variables a las que se le asignan un numero aleatorio entre 1 y 10
    n = random.randint(1, 10)
    m = random.randint(1,10)

    print(n, "/" , m) # Saca por pantalla los dos numeros generados

    print("Resultado:")

    #Condicionales que determinan si un numero es mayor, menor o igual
    if n > m:
        print(n,">",m)
    elif m > n:
        print(m,">",n)
    else: # else recoge todos los resultados que se escapen de las dos condiciones anteriores
        print(m,"=",n)
        i+=1 # Si los numeros son iguales suma 1 a i

    print() # Linea que pinta un espacio vertical para aclarar
#Trabajo Practico Estructuras Repetitivas Unidad 4
#Santisteban, Pilar - 1° prog 2°
print("Actividades")
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("1° EJERCICIO")
for i in range(0,101):
    print(i)
    
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
print("2° EJERCICIO")
numero :int = int(input("Ingrese un numero entero: "))
numero = abs(numero)
digitos : int = 0
numero_inicial :int = numero
while numero > digitos:
    digitos = digitos + 1
    numero = numero//10
print(f"El numero {numero_inicial} contiene {digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("3° EJERCICIO")
numero1: int = int(input("Ingrese un numero entero: "))
numero2: int = int(input("Ingrese numero mayor al anterior: "))
suma : int = 0
for i in range(numero1+1,numero2):
    suma =suma +i
print(f"La suma de los numeros comprendidos entre {numero1} y {numero2} es igual a {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
print("4° EJERCICIO")
bandera :bool = True
suma : int = 0
while bandera == True:
    numero : int = int(input("Ingrese un numero: "))
    suma = suma + numero
    if numero==0 : 
        bandera= False
        print("La suma de los numeros ingresados es ", suma )

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("5° EJERCICIO")
import random
print("Bienvenido al juego del azar " \
"Intente adivinar que numero estoy pensando en la menor cantidad de intentos!")
numero_aleatorio : int = random.randint(0,9)
numero_ingresado : int = int(input("Ingrese un numero: "))
intento : int = 1
while numero_ingresado != numero_aleatorio :
    numero_ingresado : int = int(input("Ingrese otro numero: "))
    intento = intento + 1
    if numero_ingresado == numero_aleatorio:
        print(f"Felicidades, adivinaste el numero en {intento} intentos")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("6° EJERCICIO")
for i in range(100,0,-2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("7° EJERCICIO")
numero: int = int(input("Ingrese numero mayor a 0 (cero): "))
suma : int = 0
for i in range(0,numero):
    suma =suma +i
print(f"La suma de los numeros comprendidos entre 0 y {numero} es igual a {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("8° EJERCICIO")
contador_par : int = 0
contador_impar : int = 0
contador_positivo : int = 0
contador_negativo : int = 0
contador_numeros_ingresados : int = 0
ceros : int = 0

for i in range(1, 11):
    numero : int = int(input(f"{i}° Ingrese el número: "))
    if numero == 0:
        ceros += 1
    else:
        if numero % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1

        if numero > 0:
            contador_positivo += 1
        else:
            contador_negativo += 1
print("De los numeros ingresados hay: ")
print("Cantidad de números pares: ", contador_par)
print("Cantidad de números impares: ", contador_impar)
print("Cantidad de números positivos: ", contador_positivo)
print("Cantidad de números negativos: ", contador_negativo)
print("Cantidad de ceros: ", ceros)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
print("9° EJERCICIO")
from statistics import mean
lista = []
for i in range(5): #se cambia el 5 por 100
    numero : int = int(input("Ingrese un numero: "))
    lista.append(numero)
print("La media de los numeros ingresados es igual a ", mean(lista))

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("10° EJERCICIO")
numero : int = int(input("Ingrese un numero: "))
numero_invertido : int = 0
while numero > 0:
    ultimo : int = numero % 10
    numero_invertido = (numero_invertido * 10) + ultimo
    numero = numero // 10
print(numero_invertido)
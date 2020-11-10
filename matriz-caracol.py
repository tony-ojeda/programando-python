''' Genere una matris de n filas y n columnas, siendo n impar(validar), con numeros aleatorios enteros en el intervalo [0, n+n)
    y muestre la matriz en pantalla. Lea la matriz en forma de espiral  comensando por el elemento central, a medida que vaya
    leyendo la matriz, llene un arreglo unidimencional con los números que se van leyendo y muestrer el arreglo en pantalla.
    Usando el arreglo extraiga el numero que se encuentra en la ultima posicion y coloquela en una variable: nro_a, luego extraiga
    el elemento de la posicion nro_a y guardela en una variable: nro_b. por ultimpo llene una matris cuya fila contiene la cantidad
    de numeros menores que nro_b y nro_a, otra fila contiene la cantidad de numeros mayores que nro_b y nro_a y la ultima fila contiene
    la cantidad de numeros menos iguales nro_b y nro_a:
'''

import random


def init():
    n = input('\nIngrese un número impar positivo para generar una matriz de n*n: ')
    if n.isdigit():
        n = int(n)
        if n % 2 is not 0:
            entrada = crear_entrada(n)
            vector = crear_vector(entrada, n)
            salida = crear_salida(vector)
            print(f" {salida[0]} < \n {salida[1]} > \n {salida[2]} = \n")

        else:
            print('Ingrese solo numeros impares positivos')
    else:
        print('Ingrese solo numeros impares positivos')


def crear_entrada(n):
    print("\n ------- Entrada -------\n")
    entrada = []
    for i in range(n):
        fila = []
        for i in range(n):
            fila.append(random.randint(0, (n + n) - 1))
        entrada.append(fila)
        print(fila)
    return entrada


def crear_vector(entrada, n):
    vector = []
    fila = int((n-1)/2)
    columna = int((n-1)/2)
    vector.append(entrada[fila][columna])
    contador_aux = 1
    while len(vector) < (n*n):
        if contador_aux % 2 == 0:
            condicion = -1
        else:
            condicion = 1
        for i in range(contador_aux):
            columna += condicion
            if columna < n and fila < n:
                vector.append(entrada[fila][columna])
        for i in range(contador_aux):
            fila -= condicion
            if columna < n and fila < n:
                vector.append(entrada[fila][columna])
        contador_aux += 1
    print(f"\n ------- Vector -------\n\n {vector}")
    return vector


def crear_salida(vector):
    nro_a = vector[-1]
    nro_b = vector[nro_a]
    print(f"\n ------- Salida -------\n\n nro_b = {nro_b}, nro_a = {nro_a}\n")
    mayores_a= 0
    mayores_b = 0
    menores_a = 0
    menores_b = 0
    for elemento in vector:
        if elemento > nro_a:
            mayores_a += 1
        if elemento > nro_b:
            mayores_b += 1
        if elemento < nro_a:
            menores_a += 1
        if elemento < nro_b:
            menores_b += 1
    return [[menores_b, menores_a], [mayores_b, mayores_a],  [vector.count(nro_b), vector.count(nro_a)]]


init()
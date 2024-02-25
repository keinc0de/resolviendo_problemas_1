# -*- coding: utf-8 -*-
simbolos = "═║╗╝╚╔"

def crear_matriz(n):
    return [[0]*n for x in range(n)]

def cinco(matriz, mitad):
    for x in range(mitad):
        li = matriz[x+1]
        li[x] = 5
        for i in range(len(li)):
            if li[i]==5:break
            else:li[i] = 1

def dos(matriz, mitad):
    indice = -2
    for x in range(mitad):
        li = matriz[x+1]
        li[indice] = 2
        for y in range(indice+1, 0):
            li[y] = 1
        indice-=1

def cuatro(matriz, mitad, par=False):
    indice = mitad
    if par:
        mitad+=1
        _ = 0
    else:
        _ = 1
    for x in range(-(mitad), 0):
        li = matriz[x]
        li[indice-_] = 4
        for i in range(len(li)):
            if li[i]==4:
                break
            else:
                li[i]=1
        indice-=1

def tres(matriz, mitad, par=False):
    indice = mitad
    if par:
        mitad+=1
        mod = 1
    else:
        mod = 0
    for x in range(-mitad, 0):
        li = matriz[x]
        for i in range(-indice, 0):
            li[i] = 1
        li[-indice-mod] = 3
        indice-=1

def espiral(n):
    matriz = crear_matriz(n)
    mitad = (n-1)//2
    cinco(matriz, mitad)
    dos(matriz, mitad)
    b = True if n%2==0 else False
    cuatro(matriz, mitad, b)
    tres(matriz, mitad, b)
    matriz[0][-1] = 2
    for f, fila in enumerate(matriz):
        for c, col in enumerate(fila):
            matriz[f][c] = simbolos[matriz[f][c]]

    _ = []
    for lista in matriz:
        _.append("".join(lista))
    print("\n".join(_))

espiral(1)
espiral(2)
espiral(3)
espiral(5)
espiral(12)
espiral(20)
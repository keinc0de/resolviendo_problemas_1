# -*- coding:utf-8 -*-
# Crea un programa que dibuje una Trifuerza de "Zelda"
#  formada por asteriscos.
#  - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#  - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 
#  Ejemplo: Trifuerza 2
 
#       *
#     ***
#     *   *
#  *** ***
def superior(n):
    lado = 2*n-1
    largo = lado*n+1
    li = []
    cantidad = 1
    char = '*'
    for x in range(n):
        _ = char*cantidad
        li.append(f"{_:^{largo}}")
        cantidad+=2
    print("\n".join(li))

def inferior(n):
    lado = 2*n-1
    largo = lado*n+1
    mitad = lado//2
    li = []
    char = "*"
    indice = n
    cantidad = 1
    for x in range(n):
        _ = char*cantidad
        espacio = ' '*lado
        linea = f"{_}{espacio}{_}"
        li.append(f"{linea: ^{largo}}")
        lado-=2
        cantidad+=2
    print("\n".join(li))

def trifuerza(n):
    superior(n)
    inferior(n)

trifuerza(4)
    
    
    
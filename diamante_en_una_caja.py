def dibuja(margen_i, margen_d, inv=False, char='*'):
    derecha = "{mgi}{char}{mgd}".format(mgi=' '*margen_i, mgd=' '*margen_d, char=char)
    izquierda = "{mgd}{char}{mgi}".format(mgi=' '*margen_i, mgd=' '*margen_d, char=char)
    if inv:
        izquierda, derecha = derecha, izquierda
    print('|', izquierda, ' ', derecha, '|', sep='')
    if margen_d>0:
        dibuja(margen_i+1, margen_d-1, inv, char)

def box(n):
    longitud = 4*n+1
    mitad = longitud//2
    valor = mitad-2

    lado = '{0:-^{1}}'.format('*',longitud)
    print(lado)
    dibuja(0, valor, char='+')
    print("{0:<{1}} {0:>{1}}".format('*', mitad))
    dibuja(0, valor, inv=True, char='+')
    print(lado)

box(1)
box(2)
box(3)

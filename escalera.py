# -*- coding:utf-8 -*-
#   Crea una funci�n que dibuje una escalera seg�n su n�mero de escalones.
#   - Si el n�mero es positivo, ser� ascendente de izquiera a derecha.
#   - Si el n�mero es negativo, ser� descendente de izquiera a derecha.
#   - Si el n�mero es cero, se dibujar�n dos guiones bajos (__).
 
#   Ejemplo: 4
#           _
#         _|
#       _|
#     _|
#   _|

def positivo(n):
	limite = n*2
	texto = f"{' '*limite}_"
	limite-=2
	for x in range(n):
		texto += f"\n{' '*limite}_|"
		limite-=2
	if n==0:
		texto+="_"
	return texto
	
def negativo(n):
    texto = "_"
    inicio = 1
    for x in range(n):
        texto += f"\n{' '*inicio}|_"
        inicio+=2
    return texto
    
def numero_escalones(num):
    return positivo(num) if num>=0 else negativo(-num)
    
escalera = numero_escalones(4)
#~ print(escalera)
#~ print(numero_escalones(0))
print(numero_escalones(-5))

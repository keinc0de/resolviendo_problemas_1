# Resolviendo Problemas
## Diamante en una caja
Escribe la función
caja (n)
obtiene un número entero positivo n, devuelve Ninguno e imprime una imagen ASCII de diamante en una caja.
1. La caja es un cuadrado con una longitud de 4n+1.
2. La parte superior e inferior de la caja deben estar impresas con caracteres "**-**", excepto el  " * " en el medio (consulte el artículo No. 4).
3. Los lados izquierdo y derecho de la caja deben estar impresos con caracteres"|", excepto el " * " en el medio (ver ítem No. 4).
4. Cada vértice de diamante está en el medio de cada lado de la caja y debe estar impreso con el carácter "*".
5. Los lados del diamante deben estar impresos con caracteres "+".
6. La longitud de cada lado del diamante es 2n-1.

> [!IMPORTANT]
> pero tiene limitantes:
> Sólo funciones de recursividad y Strings.
> no para `loops` o `while` o `range`

**Muestra:**
`box(1) => None`
y se imprime lo siguiente:
```
--*--
|+ +|
*   *
|+ +|
--*--
```

Para `box(2)`
```
----*----
|  + +  |
| +   + |
|+     +|
*       *
|+     +|
| +   + |
|  + +  |
----*----
```
### Solucion
![](para_md/prob_dc.gif)

---
## Escalera
Crea una función que dibuje una escalera según su número de escalones.
 - Si el número es positivo, será ascendente de izquierda a derecha.
 - Si el número es negativo, será descendente de izquierda a derecha.
 - Si el número es cero, se dibujarán dos guiones bajos (__).
 
**Ejemplo:** para el numero 4
```python
           _
         _|
       _|
     _|
   _|
```
### Solucion
![](para_md/escalera_cap.gif)

---
## Trifuerza
Crea un programa que dibuje una Trifuerza de "Zelda"
formada por asteriscos.
- Debes indicarle el número de filas de los triángulos con un entero positivo (n).
- Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 
**Ejemplo:** Trifuerza 2
 
```
     *
    ***
   *   *
  *** ***
```
### Solucion
![](para_md/trifuerza_cap.gif)

## Espiral
 Crea una función que dibuje una espiral como la del ejemplo.
 * Únicamente se indica de forma dinámica el tamaño del lado.
 * Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚

 Ejemplo espiral de **lado 5** (5 filas y 5 columnas):
```
 ════╗
 ╔══╗║
 ║╔╗║║
 ║╚═╝║
 ╚═══╝
```

### SOLUCION
![](para_md/espiral_cap.gif)
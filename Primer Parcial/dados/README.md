# Ejercicio: Combinaciones de Dados (Backtracking con generador)

Descripción

Dado un número de dados y un número de caras por dado, queremos generar todas las
combinaciones posibles que utilicen exactamente todos los dados y cuya suma total
sea menor o igual que una cota T.

Requisitos y restricciones (importantes)

-   Implementa una función generadora (usar `yield`) que produzca cada solución.
-   No se permite usar `yield from` (la recursión debe devolver valores mediante
    `yield` explícitos o iterando sobre el generador recursivo).
-   Cada solución debe ser devuelta como una cadena de texto con los valores
    de los dados separados por un único espacio. Ejemplo: "1 1 1".
-   Cada combinación debe usar exactamente `d` dados (ninguno menos).
-   Cada dado toma valores enteros entre `1` y `s` (ambos inclusive).
-   La suma de las caras de la combinación debe ser <= `T`.

Entrada

El programa espera una única línea con tres enteros separados por espacios:

-   d: número de dados (d >= 1)
-   s: número de caras por dado (s >= 1)
-   T: suma máxima permitida (T >= d ya que cada dado como mínimo vale 1, aunque
    el programa debe funcionar también si T < d devolviendo 0 soluciones)

Formato de ejemplo de entrada:

```
3 6 10
```

Salida

-   Cada línea de la salida es una combinación válida en formato de cadena con
    los valores de cada dado separados por espacios (por ejemplo `1 2 3`).
    -   El orden de las combinaciones en la salida debe ser lexicográfico, es decir
        desde "1 1 1" hasta "s s s" (orden ascendente por componentes, como en
        orden lexicográfico habitual).
-   Al final, el programa puede imprimir el número total de soluciones (como lo
    hace `main.py` del enunciado dado).

Ejemplo

Para la entrada `3 6 10` el generador debe producir (entre otras) combinaciones
como:

```
1 1 1
1 1 2
1 1 3
...
```

(donde cada combinación tenga exactamente 3 valores entre 1 y 6 y su suma sea <= 10).

Archivos relevantes

-   `backtracking.py` — Contiene la clase `Backtracking(d, s, T)` y su método `next()`
    que debe ser un generador de las combinaciones (cada elemento devuelto es una
    cadena en el formato especificado).
-   `main.py` — Llama a `Backtracking(d, s, T).next()` y se encarga de imprimir las
    líneas y el recuento final.
-   `simple_stack.py` — Implementación auxiliar de pila (no es necesaria para la
    solución con recursion/generadores, pero se incluye con los ficheros proporcionados).
-   `test1.txt` — Archivo de prueba con la entrada de ejemplo.

Pautas de implementación y pruebas

-   El generador debe usar backtracking recursivo o iterativo, pero debe
    devolver resultados con `yield`.
-   Prueba el ejercicio ejecutando desde la carpeta `dados`:

```powershell
cd "Primer Parcial/dados/given_files"
python main.py
```

-   Si quieres probar entradas diferentes, modifica `test1.txt` o cambia
    `test_file = None` en `main.py` para leer desde la entrada estándar.

Notas finales

-   El enunciado solicita explícitamente que la salida de cada combinación sea
    una cadena en el formato `"1 1 1"`. No cambies ese formato.
-   Si deseas optimizar la generación (por ejemplo podas adicionales cuando la
    suma acumulada ya supera `T`), puedes hacerlo siempre que el formato y el
    comportamiento de salida no cambien.

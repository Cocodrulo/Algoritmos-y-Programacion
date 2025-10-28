## Asignación de Exámenes a Aulas — Max-Fit Decreasing (MFD)

### Objetivo

Implementar una estrategia Greedy para asignar exámenes a aulas con capacidades conocidas usando el algoritmo Max-Fit Decreasing (MFD).

La idea principal es: ordenar los exámenes de mayor a menor y, para cada examen, asignarlo a la primera aula "grande" suficiente (priorizando las aulas con mayor capacidad). Cada aula solo puede usarse una vez.

### Formato de entrada

```
n m
e1 e2 ... en
c1 c2 ... cm
```

donde:

-   `n`: número de exámenes
-   `m`: número de aulas
-   `e1..en`: tamaños (alumnos necesarios) de cada examen
-   `c1..cm`: capacidades de cada aula

### Formato de salida

Si la asignación es posible (todos los exámenes caben), imprimir:

```
rooms_used=<k> waste=<w>
assign=[cap1, cap2, ...]
```

donde:

-   `rooms_used` es el número de exámenes asignados (debe ser `n`).
-   `waste = sum(assign) - sum(exams)` es el desperdicio total de capacidad.
-   `assign[i]` es la capacidad del aula asignada al examen `exams[i]` (en el mismo orden de entrada).

Si la asignación es imposible (algún examen no cabe en ninguna aula según la estrategia), debe devolverse `ERROR` desde `main.py` (la función solicitada retornará `None` para indicar esto).

### Ejemplo

Entrada:

```
4 5
70 45 30 10
80 50 40 30 10
```

Salida esperada:

```
rooms_used=4 waste=45
assign=[80, 50, 40, 30]
```

Explicación rápida: ordenando exámenes de mayor a menor [70,45,30,10] y aulas de mayor a menor [80,50,40,30,10], se asignan las cuatro primeras aulas a los cuatro exámenes.

### Tarea del alumno

Implementa la función `solve_mfd_feasible(exams, rooms)` dentro de `solve.py` con el siguiente comportamiento:

-   Parámetros:

    -   `exams`: lista de enteros con los tamaños de los exámenes (en el orden de entrada).
    -   `rooms`: lista de enteros con las capacidades de las aulas.

-   Devolver:
    -   Si la asignación según MFD es posible: una tupla `(rooms_used, waste, assign_cap)` donde:
        -   `rooms_used` es un entero igual a `n` (número de exámenes asignados).
        -   `waste` es un entero con la suma de las capacidades asignadas menos la suma de exámenes.
        -   `assign_cap` es una lista de capacidades asignadas en el mismo orden que `exams` de entrada.
    -   Si no es posible asignar todos los exámenes siguiendo la estrategia MFD: devolver `None`.

Notas de implementación (estrategia MFD):

1. Ordena los exámenes de mayor a menor, pero recuerda conservar el índice original para reconstruir `assign_cap` en el orden de entrada.
2. Ordena las aulas de mayor a menor.
3. Para cada examen (de mayor a menor), recorre las aulas ordenadas y toma la primera aula con capacidad >= tamaño del examen. Marcar esa aula como usada (no reutilizable).
4. Si algún examen no encuentra aula, devuelve `None`.
5. Si todos los exámenes se asignan, calcula `rooms_used`, `waste` y devuelve `(rooms_used, waste, assign_cap)`.

### Contrato mínimo

-   Entradas: listas de enteros no negativas. Se puede suponer que `n, m >= 0`.
-   Errores: si las entradas no cumplen el tipo esperado, el comportamiento puede ser indefinido (no es necesario capturar todos los errores de tipo para la práctica).

### Casos borde a considerar

-   `n = 0` (sin exámenes): `rooms_used = 0`, `waste = 0`, `assign = []`.
-   `m = 0` y `n > 0`: imposible → devolver `None`.
-   Exámenes con tamaño 0: se pueden asignar a cualquier aula (si esa política es deseada), pero sigue la misma lógica: deben usarse aulas.
-   Aulas con la misma capacidad: mantener orden estable no es necesario, pero asegúrate de no reutilizar aulas.

### Archivos relacionados

-   `main.py`: lee la entrada, llama a `solve_mfd_feasible(exams, rooms)` y formatea la salida; no la modifiques a menos que sea necesario.
-   `solve.py`: implementar aquí la función solicitada.

### Cómo probar (rápido)

Coloca el caso de prueba en un fichero `test.txt` y ejecuta `main.py` tal como ya está preparado en el repositorio; `main.py` debe imprimir la salida en el formato especificado.

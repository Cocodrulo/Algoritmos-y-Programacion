## MergeSort — DJ Playlist (BPM + flow)

🎯 Objetivo

Un DJ quiere ordenar canciones por BPM (beats per minute) pero quiere preservar el orden de entrada para las canciones que empatan en BPM (para mantener el "flow" de la sesión).

Si además se proporciona un campo `energy` (entero) en todas las líneas, el comparador será compuesto:

-   Primero por `bpm` ascendente;
-   Si empatan en `bpm`, por `energy` descendente;
-   Si empatan en `bpm` y `energy`, se preserva el orden de llegada (estabilidad).

Si NO se proporciona `energy` en la entrada, el comparador es simplemente `bpm` ascendente y estable (igual BPM → conservar orden de llegada).

---

🧩 Formato de entrada

```
N
title_1 bpm_1 [energy_1]
...
title_N bpm_N [energy_N]
```

-   `N`: entero > 0 (número de pistas).
-   Cada línea de pista tiene 2 o 3 tokens:
    -   `title`: string sin espacios (título de la pista).
    -   `bpm`: entero >= 0.
    -   `[energy]` (opcional): entero; si aparece, todas las N líneas tendrán este campo.

El `main.py` provisto detecta automáticamente si las N líneas contienen `energy` (todas o ninguna) y llama a la función encargada de ordenar.

---

🧩 Formato de salida

Una única línea con la lista de títulos ordenados, sin comillas y separados por comas:

```
[title_ordenado_1, title_ordenado_2, ..., title_ordenado_N]
```

No se imprime BPM ni energy en la salida (esa información es redundante para el verificador).

---

🧮 Ejemplo (sin `energy`)

Entrada

```
5
Track9 128
Track3 124
Track7 128
Track1 120
Track8 130
```

Salida esperada (estabilidad: Track9 antes que Track7)

```
[Track1, Track3, Track9, Track7, Track8]
```

Orden: BPM ascendente → 120, 124, 128, 128, 130; entre los dos 128 se mantiene el orden de entrada.

---

🧮 Ejemplo (con `energy`)

Entrada

```
5
Track1 128 50
Track2 128 70
Track3 125 90
Track4 128 70
Track5 130 40
```

Salida esperada (BPM asc; empates por energy desc; empate perfecto conserva orden: Track2 antes que Track4)

```
[Track3, Track2, Track4, Track1, Track5]
```

Explicación: ordenar por BPM ascendente → 125, 128(x3), 130. Dentro de 128, ordenar por energy descendente → Track2(70), Track4(70), Track1(50). Como Track2 y Track4 empatan en BPM y energy, se respeta el orden de llegada (Track2 antes que Track4).

---

🧑💻 Tarea del alumno

En `solve.py` implementa la función:

```py
def sort_playlist_by_flow(tracks, use_energy):
    """
    Parámetros:
      - tracks: lista de tuplas (title:str, bpm:int [, energy:int])
      - use_energy: bool (True si todas las líneas incluyen energy)

    Devuelve:
      - list[str]: títulos en el orden final

    Reglas del comparador:
      - Siempre BPM ascendente.
      - Si use_energy: en empate de BPM, energy descendente.
      - Si vuelve a haber empate, mantener orden de llegada (estabilidad).

    Implementación requerida: MergeSort estable (usa merge que selecciona primero del subarray izquierdo en caso de empate).
    """
```

Notas importantes:

-   Debes usar MergeSort y garantizar estabilidad en la fase de merge: cuando los elementos comparados son "iguales" según el comparador, debes elegir el elemento del subarray izquierdo para preservar el orden de llegada.
-   El `main.py` ya prepara `tracks` como lista de tuplas y pasa `use_energy`.

---

🧮 Contrato y casos borde

-   `N = 0`: (no debería ocurrir si N > 0 según la especificación) pero la función debe manejar listas vacías devolviendo `[]`.
-   Todos los `bpm` y `energy` son enteros no negativos; puedes asumir entradas válidas.
-   Si `use_energy=False`, cada tupla en `tracks` tiene 2 elementos `(title, bpm)`; si `True`, tiene 3 `(title, bpm, energy)`.

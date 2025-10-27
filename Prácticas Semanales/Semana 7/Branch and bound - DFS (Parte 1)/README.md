# Branch and Bound — Recorrido en profundidad (DFS)

Descripción
-----------
Proyecto de práctica para implementar un recorrido en profundidad (DFS) orientado a Branch and Bound usando la clase `node`.

Objetivo
--------
Implementar la búsqueda en profundidad sobre el espacio de estados manteniendo una lista (pila) de nodos vivos. El algoritmo ramifica por la derecha y por la izquierda (añadiendo nodos vivos) y usa poda/estimaciones de coste para guiar la búsqueda (según la implementación en `node.py`).

Estructura del repositorio
--------------------------
- `main.py` — punto de entrada. Lee datos de entrada y lanza la resolución.
- `node.py` — definición de la clase `node` (estructura de estado, campos como `index`, `taken`, `value`, `room`, `estimate`, etc.).
- `solve.py` — lógica del algoritmo Branch and Bound / DFS (creación de nodos, expansión, poda y búsqueda).
- `utils.py` — utilidades auxiliares (lectura, impresión o funciones de ayuda).
- `test1.txt` — fichero de ejemplo con datos de entrada para probar el programa.

Cómo ejecutar
--------------
Requiere Python 3.x instalado.

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:

```powershell
python main.py
```

Si `main.py` acepta una ruta de fichero de entrada, se puede pasar `test1.txt` como argumento (si el programa está preparado para ello):

```powershell
python main.py test1.txt
```

Formato de entrada
------------------
El formato exacto depende de cómo lo haya definido `main.py`/`utils.py`. Por lo general `test1.txt` contiene los parámetros del problema (capacidad, pesos/valores, número de objetos, etc.). Si no está claro, abrir `test1.txt` para ver el formato concreto.

Resumen del algoritmo (Branch and Bound, DFS)
--------------------------------------------
- Partir del nodo raíz y añadirlo a la lista de nodos vivos (pila).
- Mientras la pila no esté vacía: sacar (pop) el nodo superior.
- Si el nodo no es hoja: ramificar por la derecha (append) y por la izquierda (append).
- Usar estimaciones en cada `node` para podar ramas que no puedan mejorar la mejor solución conocida.

Notas prácticas
----------------
- Si el comportamiento no es el esperado, revisar `node.py` para entender campos como `estimate` y `value` y `solve.py` para la lógica de expansión.
- Para depurar, añadir prints en los puntos de push/pop de la pila para ver el orden de exploración.

Ejemplo rápido
--------------
1. Abrir `test1.txt` para ver los datos.
2. Ejecutar `python main.py`.
3. Comprobar la salida por consola con la solución encontrada y/o el recorrido de nodos.

Siguientes pasos (opcional)
--------------------------
- Añadir un pequeño script de tests que ejecute `main.py` con varios archivos de entrada y verifique las salidas.
- Documentar el formato de `test1.txt` dentro de este `README.md` si se conoce con detalle.

Contacto
--------
Si necesitas que adapte el README con el formato exacto de entrada o ejemplos de salida, márcalo y lo actualizo.

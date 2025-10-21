# Guía de contribución

Gracias por tu interés en contribuir a este repositorio de ejercicios de Algoritmos y Programación. Este repositorio es de finalidad didáctica: las contribuciones deben facilitar el aprendizaje y la comprensión.

## Alcance y objetivos

-   Mantener los ejercicios organizados por parcial y por enunciado/tema.
-   Proporcionar soluciones claras y bien documentadas.
-   Añadir ejemplos y pequeños tests que ayuden a validar el código.

## Requisitos previos

-   Git instalado.
-   Python 3.7 o superior instalado.
-   Opcional: un editor con soporte para formato/linters (VS Code recomendado).

## Configuración local rápida

```powershell
# 1) Clona tu fork o el repositorio (si tienes permisos de push)
git clone <url-del-repo-o-fork>
cd "Algoritmos-y-Programaci-n"

# 2) (Opcional) Crea y activa un entorno virtual
python -m venv .venv
. .venv/Scripts/Activate.ps1

# 3) Ejecuta un ejercicio de ejemplo
cd "Primer Parcial/dados/solution"
python main.py
```

## Estructura de carpetas (orientativa)

-   `PARCIAL/` carpeta del parcial (p. ej., `Primer Parcial/`).
    -   `EJERCICIO/` carpeta del ejercicio (p. ej., `dados/`).
        -   `given_files/` ficheros proporcionados (plantillas, utilidades, datos).
        -   `solution/` tu solución implementada y ejecutable.
        -   `README.md` instrucciones específicas del ejercicio (si aplica).

Procura no mezclar ejercicios de distintos parciales; cada uno debe ser autocontenible.

## Estilo de código (Python)

-   Sigue PEP 8 (nombres en `snake_case`, líneas ≤ 79/99 caracteres cuando sea razonable, etc.).
-   Escribe funciones pequeñas con responsabilidades claras.
-   Añade docstrings breves donde aporte valor (qué hace, parámetros, retorno, precondiciones).
-   Prefiere variables descriptivas sobre comentarios extensos.
-   Si introduces dependencias externas, justifícalas y limita su uso.

Opcional (si lo usas localmente):

-   Formateo automático con Black.
-   Orden de imports con isort.

## Flujo de trabajo con Git

1. Crea una rama por cambio:

    - feat/nombre-ejercicio-o-idea
    - fix/bug-descripcion-corta
    - docs/actualiza-lecturas

2. Commits con Conventional Commits (en español):

    - `feat:` nueva funcionalidad o nuevo ejercicio
    - `fix:` corrección de fallo
    - `docs:` documentación solamente
    - `style:` formato (espacios, comas) sin cambiar lógica
    - `refactor:` cambio interno sin alterar comportamiento
    - `test:` añade o ajusta pruebas/ejemplos
    - `chore:` tareas varias (scripts, limpieza)

    Ejemplos:

    - `feat(dados): agrega solución backtracking y README`
    - `fix(utils): corrige índice fuera de rango en push`
    - `docs: añade pasos de ejecución en Windows`

3. Mantén los PRs pequeños y enfocados. Incluye un resumen del "por qué" y "qué cambia".

## Pruebas y validación

-   Incluye ejemplos de uso o pequeñas comprobaciones (asserts, doctests o scripts) que permitan validar la solución.
-   Si modificas utilidades compartidas (`utils.py`, `simple_stack.py`), añade un ejemplo mínimo que demuestre que no rompes ejercicios existentes.
-   Explica cómo ejecutar tu ejemplo/prueba en el README del ejercicio.

## Checklist para Pull Requests

-   [ ] La carpeta y nombres siguen la convención del repositorio.
-   [ ] He aportado una solución que funciona.
-   [ ] Se añaden instrucciones de ejecución en el README del ejercicio (si procede).
-   [ ] Los commits siguen el formato Conventional Commits.
-   [ ] No se incluyen archivos generados (.venv, **pycache**, datos grandes, etc.).

## Reporte de issues

Cuando abras un issue, intenta incluir:

-   Contexto breve del problema/mejora.
-   Pasos para reproducir (si es un bug).
-   Resultado esperado vs. resultado obtenido.
-   Fragmentos de código o mensajes de error relevantes.
-   Entorno (SO, versión de Python, etc.).

## Licencia

Si planeas publicar material reutilizable, considera añadir una licencia (por ejemplo, MIT). Si hay material con derechos reservados del curso, evita subirlo sin permiso explícito.

## Código de conducta

Sé respetuoso. El objetivo es aprender y ayudar: revisa cambios con empatía, propone mejoras con ejemplos y evita descalificaciones personales.

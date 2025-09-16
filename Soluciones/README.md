# Soluciones a las Actividades del Repositorio Programacion_UQ_Fisica

Este directorio contiene las soluciones desarrolladas para las diferentes actividades propuestas en el repositorio `Programacion_UQ_Fisica`.

## Estructura del Directorio

Cada taller o proyecto tiene su propio subdirectorio, donde se encuentran los archivos de código (`.py`) y cualquier otro archivo auxiliar necesario (como archivos CSV o JSON generados o descargados durante la ejecución).

- `Proyecto_1/`
- `Taller_Pandas_2/`
- `Taller_Generadores/`
- `Taller_Librerias_1/`

## Proyectos y Talleres Desarrollados

A continuación, se detalla cada actividad resuelta, incluyendo una breve descripción y las instrucciones para ejecutar el código correspondiente.




### Proyecto 1: Descripción y Rúbrica de Evaluación

**Descripción:**

Este proyecto se enfoca en la implementación de conceptos avanzados de Programación Orientada a Objetos (POO) en Python, incluyendo herencia múltiple, abstracción, polimorfismo, encapsulación con `@property`, y el uso de decoradores. Además, requiere la implementación de un método numérico sin librerías externas (excepto `math`), visualización y animación con Matplotlib, modularización del código, y gestión del proyecto en GitHub.

**Archivos Relevantes:**

- `Proyecto_1/proyecto_1.py`: Contiene la implementación de la solución.

**Instrucciones de Ejecución:**

Para ejecutar la solución del Proyecto 1, navegue al directorio `Soluciones/Proyecto_1` y ejecute el script de Python:

```bash
cd Soluciones/Proyecto_1
python3 proyecto_1.py
```

**Resultados Esperados:**

El script generará una visualización o animación (si aplica) y mostrará los resultados del método numérico implementado en la consola.




### Taller Pandas 2

**Descripción:**

Este taller se centra en la manipulación y análisis de datos utilizando la librería Pandas. Las actividades incluyen la importación de un archivo CSV de datos de COVID-19 en Colombia, la unificación de valores repetidos, el manejo de valores nulos, la conversión y extracción de componentes de fechas, la extracción de datos específicos por departamento y ciudad, la generación de una matriz NumPy con datos temporales y de género, y la exportación de tablas filtradas.

**Archivos Relevantes:**

- `Taller_Pandas_2/taller_pandas_2.py`: Contiene la implementación de la solución.
- `Taller_Pandas_2/COVID-19_Colombia.csv`: Archivo de datos utilizado para el análisis.
- `Taller_Pandas_2/COVID-19_BOGOTA.csv`: Archivo de datos exportado para el departamento de Bogotá.

**Instrucciones de Ejecución:**

Para ejecutar la solución del Taller Pandas 2, navegue al directorio `Soluciones/Taller_Pandas_2` y ejecute el script de Python:

```bash
cd Soluciones/Taller_Pandas_2
python3 taller_pandas_2.py
```

**Resultados Esperados:**

El script imprimirá en la consola los resultados de cada punto del taller, incluyendo encabezados del DataFrame, valores únicos unificados, estadísticas de valores nulos, ejemplos de fechas convertidas, y la matriz NumPy generada. Además, se generará un archivo CSV con los datos filtrados para el departamento de Bogotá.




### Taller Generadores y gestión de datos

**Descripción:**

Este taller aborda el uso de generadores en Python y la gestión de datos con diferentes formatos (CSV, JSON, texto plano). Las actividades incluyen la creación de un generador de la serie de Fibonacci, un generador de números pares, el procesamiento de datos de estudiantes desde un archivo CSV (cálculo de promedios, identificación de reprobados y top 10%), la manipulación de datos del Titanic con Pandas (conteo de sobrevivientes por género), la exportación de datos de empleados a formato JSON, el cálculo de sumas acumulativas desde un archivo de texto sin librerías externas, la creación de un generador de palabras largas, y una clase para procesar texto extrayendo párrafos y encontrando los más largos.

**Archivos Relevantes:**

- `Taller_Generadores/taller_generadores.py`: Contiene la implementación de la solución.
- `Taller_Generadores/estudiantes.csv`: Archivo CSV simulado para el ejercicio de estudiantes.
- `Taller_Generadores/titanic.csv`: Archivo CSV del dataset de Titanic (descargado si no existe).
- `Taller_Generadores/empleados.json`: Archivo JSON generado con datos de empleados.
- `Taller_Generadores/numeros.txt`: Archivo de texto simulado con números.
- `Taller_Generadores/sample_text.txt`: Archivo de texto simulado para el procesamiento de párrafos.
- `Taller_Generadores/productos.json`: Archivo JSON simulado con datos de productos.

**Instrucciones de Ejecución:**

Para ejecutar la solución del Taller Generadores y gestión de datos, navegue al directorio `Soluciones/Taller_Generadores` y ejecute el script de Python:

```bash
cd Soluciones/Taller_Generadores
python3 taller_generadores.py
```

**Resultados Esperados:**

El script imprimirá en la consola los resultados de cada punto del taller, incluyendo la serie de Fibonacci, números pares, promedios de estudiantes, reprobados y top 10%, estadísticas del Titanic, confirmación de exportación JSON, sumas acumulativas, palabras largas, y el procesamiento de párrafos.




### Taller Manejo de librerías 1

**Descripción:**

Este taller explora el uso de librerías fundamentales como Pandas y NumPy para análisis de datos y álgebra lineal, así como la implementación de clases, objetos, excepciones y el manejo de argumentos variables (`*args` y `**kwargs`). Las actividades incluyen el análisis de datos desde un CSV, la generación de términos de una serie de Taylor, la creación de una clase `Particula` con propiedades y cálculo de energía cinética, y la resolución de sistemas de ecuaciones lineales.

**Archivos Relevantes:**

- `Taller_Librerias_1/taller_librerias_1.py`: Contiene la implementación de la solución.
- `Taller_Librerias_1/datos_ejercicio1.csv`: Archivo CSV generado para el ejercicio 1.

**Instrucciones de Ejecución:**

Para ejecutar la solución del Taller Manejo de librerías 1, navegue al directorio `Soluciones/Taller_Librerias_1` y ejecute el script de Python:

```bash
cd Soluciones/Taller_Librerias_1
python3 taller_librerias_1.py
```

**Resultados Esperados:**

El script imprimirá en la consola los resultados de cada ejercicio, incluyendo el análisis del DataFrame, los términos de la serie de Taylor, las propiedades y energía cinética de las partículas, y la solución de los sistemas de ecuaciones lineales.




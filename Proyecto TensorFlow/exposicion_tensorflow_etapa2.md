## Segunda Etapa del Proyecto: Estructuras de Datos y Entrenamiento del Modelo

Una vez que hemos sentado las bases en la primera etapa al definir la arquitectura de nuestra red neuronal, la segunda etapa se enfoca en darle vida a ese modelo. Esto implica dos componentes cruciales: la **preparación de los datos** que el modelo usará para aprender y el **proceso de entrenamiento** en sí mismo, donde la red ajusta sus parámetros para minimizar el error.

### 1. Habilidades en Python: Listas, Tuplas y Manejo de Colecciones

En el contexto del aprendizaje automático, los datos son el combustible que alimenta el motor del modelo. La capacidad de manejar y estructurar estos datos de manera eficiente es una habilidad fundamental en Python.

*   **Generación de Datos:** Antes de que el modelo pueda aprender la función `y = x²`, necesitamos proporcionarle ejemplos. En esta etapa, se utiliza la librería **NumPy** para generar dos colecciones de datos:
    *   Un vector `x` con valores numéricos (las entradas).
    *   Un vector `y` con los valores correspondientes al cuadrado de `x` (las salidas o etiquetas).

*   **Estructuras de Datos:** Estos vectores son, en esencia, colecciones (arrays de NumPy) que se manejan de manera similar a las listas de Python. Se utilizan para almacenar miles de pares `(x, y)` que servirán como ejemplos de entrenamiento.

*   **División de Datos (Train/Validation Split):** Una práctica estándar en Machine Learning es no usar todos los datos para entrenar el modelo. Se dividen en dos conjuntos:
    *   **Conjunto de Entrenamiento (Training Set):** La mayor parte de los datos (ej. 80%) que el modelo utiliza directamente para aprender y ajustar sus pesos internos.
    *   **Conjunto de Validación (Validation Set):** Una porción más pequeña (ej. 20%) que el modelo no "ve" durante el ajuste de pesos, pero que se usa al final de cada época para evaluar qué tan bien está generalizando su aprendizaje a datos nuevos. Esto es crucial para detectar problemas como el **sobreajuste (overfitting)**, donde el modelo memoriza los datos de entrenamiento pero no aprende la relación subyacente.

En nuestro proyecto, el método `generar_datos` de la clase `ModeloCuadratico` se encarga de esta tarea, creando los arrays `x` e `y` que luego se pasarán al método de entrenamiento.

### 2. Habilidades en TensorFlow: Entrenar el Modelo y Graficar Resultados

Esta es la fase donde ocurre la "magia" del aprendizaje. Una vez que tenemos el modelo compilado (de la Etapa 1) y los datos preparados, el siguiente paso es entrenarlo.

*   **Entrenamiento del Modelo (`model.fit`):** El corazón de esta etapa es la llamada al método `fit()` del modelo de Keras. Este método orquesta todo el proceso de entrenamiento, que consiste en:
    1.  Tomar un lote (`batch`) de datos del conjunto de entrenamiento.
    2.  Pasar las entradas `x` a través de la red para obtener una predicción.
    3.  Comparar la predicción con el valor real `y` usando la **función de pérdida (loss)** que definimos en la compilación (en nuestro caso, el Error Cuadrático Medio o MSE).
    4.  Utilizar el **optimizador** (ej. `Adam`) para calcular cómo ajustar los pesos de las neuronas para reducir esa pérdida.
    5.  Actualizar los pesos de la red.
    6.  Repetir este proceso para todos los lotes hasta completar una **época (epoch)**, que es un recorrido completo por todo el conjunto de entrenamiento.
    7.  Repetir todo el ciclo durante el número de épocas especificado.

*   **Monitoreo y Graficación de Resultados:** El método `fit()` devuelve un objeto `history` que contiene un registro de la pérdida y otras métricas en cada época, tanto para los datos de entrenamiento como para los de validación. Esta información es invaluable y se utiliza para:
    *   **Graficar la Curva de Pérdida (Loss Curve):** Se visualiza cómo la pérdida de entrenamiento y la de validación disminuyen a lo largo de las épocas. Idealmente, ambas deberían converger hacia un valor bajo. Si la pérdida de validación comienza a aumentar mientras la de entrenamiento sigue bajando, es una señal clara de sobreajuste.

### Conexión con la Primera Etapa

La segunda etapa es la continuación lógica y directa de la primera. La conexión es la siguiente:

1.  **El Modelo es el Puente:** El modelo de red neuronal que **creamos y compilamos** en la Etapa 1 es el objeto central que se **entrena** en la Etapa 2. Sin un modelo compilado, el método `fit()` no se puede ejecutar.

2.  **De la Arquitectura a la Práctica:** La Etapa 1 fue teórica, donde diseñamos la "mente" de nuestro modelo (las capas, el optimizador, la función de pérdida). La Etapa 2 es la fase práctica, donde alimentamos esa "mente" con datos y le permitimos aprender a través de la experiencia (iteraciones de entrenamiento).

3.  **POO en Acción:** La clase `ModeloCuadratico` que definimos en la Etapa 1 ahora se utiliza de manera concreta. El método `entrenar` de nuestra clase encapsula la llamada a `model.fit()`, manteniendo el código organizado y coherente con el diseño orientado a objetos.

En resumen, si la Etapa 1 fue construir el motor de un coche (la red neuronal), la Etapa 2 es llenarlo de gasolina (los datos) y encenderlo para que aprenda a conducir (el entrenamiento).

```python
# Ejemplo de cómo se conectan las etapas en el código:

# --- ETAPA 1 ---
mi_modelo = ModeloCuadratico()
mi_modelo.construir_modelo()  # Se crea y compila el modelo.

# --- ETAPA 2 ---
x_data, y_data = mi_modelo.generar_datos() # Se preparan los datos.
mi_modelo.entrenar(x_data, y_data) # Se usa el modelo de la Etapa 1 para entrenar con los datos.
```

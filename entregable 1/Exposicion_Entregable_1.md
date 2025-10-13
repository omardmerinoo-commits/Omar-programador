# Exposición del Entregable 1: Aproximación de la Función y = x² con una Red Neuronal Simple

## 1. Introducción

El presente documento detalla el desarrollo de un proyecto de aprendizaje automático enfocado en la aproximación de la función cuadrática `y = x²` utilizando una red neuronal simple implementada con TensorFlow y Keras. Este entregable aborda los fundamentos de la construcción, entrenamiento y evaluación de modelos de redes neuronales, así como la organización del código en una estructura modular y la visualización de resultados.

El objetivo principal es demostrar la capacidad de una red neuronal para aprender patrones no lineales a partir de datos, reforzando conceptos clave de Python como la programación orientada a objetos y el manejo de librerías científicas.

## 2. Contexto y Justificación

La aproximación de funciones es una tarea fundamental en el aprendizaje automático y la inteligencia artificial. Permite a los modelos aprender relaciones complejas entre entradas y salidas, lo que es crucial para aplicaciones como la predicción, la clasificación y el control. La función `y = x²` es un ejemplo clásico de una relación no lineal que, aunque simple, sirve como un excelente punto de partida para entender cómo las redes neuronales pueden modelar este tipo de comportamientos.

La elección de TensorFlow y Keras se debe a su popularidad, flexibilidad y facilidad de uso, lo que permite construir y experimentar con arquitecturas de redes neuronales de manera eficiente. La estructuración del código en una clase `ModeloCuadratico` promueve la **reusabilidad**, la **modularidad** y la **legibilidad**, principios esenciales en el desarrollo de software de calidad.

## 3. Diseño del Código

El proyecto se compone de dos archivos principales: `modelo_cuadratico.py`, que define la clase central del modelo, y `main.py`, que orquesta la ejecución del flujo de trabajo.

### 3.1. `modelo_cuadratico.py`: La Clase `ModeloCuadratico`

Esta clase encapsula toda la lógica relacionada con la red neuronal, desde la generación de datos hasta la predicción. Sus métodos son:

#### `__init__(self)`

*   **Propósito**: Constructor de la clase. Inicializa las variables de instancia `self.model`, `self.history`, `self.x_train`, `self.y_train`, `self.x_val`, y `self.y_val` a `None`. Esto asegura que el estado del modelo sea conocido y que los atributos estén disponibles para ser asignados durante las fases posteriores.

#### `generar_datos(self, n_samples: int = 1000, rango: tuple = (-1, 1))`

*   **Propósito**: Genera un conjunto de datos sintéticos para el entrenamiento y la evaluación del modelo.
*   **Funcionamiento**: 
    *   Utiliza `np.random.uniform` para crear `n_samples` puntos `x` distribuidos uniformemente dentro del `rango` especificado (por defecto, de -1 a 1).
    *   Calcula los valores `y` correspondientes a `x²` y añade un pequeño ruido aleatorio (`np.random.normal`) para simular datos del mundo real y evitar el sobreajuste trivial. El ruido tiene una media de 0 y una desviación estándar de 0.05.
    *   `np.random.seed(42)` se utiliza para garantizar la reproducibilidad de los datos generados, lo que es crucial para la depuración y la comparación de resultados.
*   **Utilidad**: Proporciona un conjunto de datos limpio y controlable para probar la capacidad de la red neuronal para aprender una relación cuadrática.

#### `construir_modelo(self)`

*   **Propósito**: Define la arquitectura de la red neuronal y la compila.
*   **Funcionamiento**: 
    *   Crea un modelo secuencial de Keras (`tf.keras.Sequential`).
    *   Añade tres capas `Dense` (totalmente conectadas):
        *   La primera capa oculta tiene 64 neuronas, utiliza la función de activación `relu` (Rectified Linear Unit) y espera una entrada de una sola característica (`input_shape=(1,)`).
        *   La segunda capa oculta también tiene 64 neuronas y `relu` como activación.
        *   La capa de salida tiene 1 neurona (para predecir un único valor `y`) y no tiene función de activación, lo que es común para problemas de regresión.
    *   Compila el modelo con el optimizador `adam` (Adaptive Moment Estimation), conocido por su eficiencia en una amplia gama de problemas de aprendizaje profundo, y la función de pérdida `mse` (Mean Squared Error), adecuada para tareas de regresión.
*   **Utilidad**: Establece la estructura de la red neuronal que aprenderá la relación entre `x` y `y`.

#### `entrenar(self, x_train, y_train, x_val, y_val, epochs: int = 100, batch_size: int = 32)`

*   **Propósito**: Entrena el modelo utilizando los datos de entrenamiento y validación.
*   **Funcionamiento**: 
    *   Almacena los datos de entrenamiento y validación en las variables de instancia.
    *   Invoca el método `fit` del modelo de Keras, pasándole los datos de entrenamiento, el número de `epochs` (iteraciones completas sobre el conjunto de datos), el `batch_size` (número de muestras por actualización de gradiente) y los datos de validación (`validation_data`).
    *   El `verbose=0` suprime la salida detallada de cada época, mostrando solo mensajes de inicio y fin de entrenamiento.
    *   El historial de entrenamiento (pérdida en entrenamiento y validación por época) se guarda en `self.history` para su posterior análisis y visualización.
*   **Utilidad**: Ajusta los pesos y sesgos de la red neuronal para minimizar la función de pérdida, permitiendo que el modelo aprenda la relación subyacente en los datos.

#### `predecir(self, x)`

*   **Propósito**: Realiza predicciones sobre nuevos datos utilizando el modelo entrenado.
*   **Funcionamiento**: 
    *   Verifica que el modelo haya sido construido y entrenado, lanzando un `ValueError` si no es así, para evitar errores en tiempo de ejecución.
    *   Utiliza el método `predict` del modelo de Keras para generar las predicciones. La entrada `x` se remodela a `x.reshape(-1, 1)` para asegurar que tenga la forma correcta (número de muestras, 1 característica) que espera el modelo.
*   **Utilidad**: Permite evaluar el rendimiento del modelo en datos no vistos y generar las predicciones que se compararán con los valores reales.

### 3.2. `main.py`: Script Principal de Ejecución

El archivo `main.py` actúa como el punto de entrada del programa, coordinando las llamadas a los métodos de la clase `ModeloCuadratico` y manejando la visualización y el guardado de resultados.

#### Flujo de Ejecución

1.  **Instanciación del Modelo**: Se crea una instancia de `ModeloCuadratico`.
2.  **Generación de Datos**: Se llama a `modelo_cuadratico.generar_datos()` para obtener los pares `(x, y)`.
3.  **División de Datos**: Los datos generados se dividen en conjuntos de entrenamiento y validación (80% y 20% respectivamente) utilizando `train_test_split` de `sklearn.model_selection`. Esto es crucial para evaluar la capacidad de generalización del modelo en datos no vistos durante el entrenamiento.
4.  **Construcción del Modelo**: Se invoca `modelo_cuadratico.construir_modelo()` para definir la arquitectura de la red neuronal.
5.  **Entrenamiento del Modelo**: Se llama a `modelo_cuadratico.entrenar()` con los datos divididos, especificando 100 épocas y un tamaño de lote de 32.
6.  **Predicción**: Se utilizan los datos de validación (`x_val`) para obtener predicciones (`y_pred`) del modelo entrenado mediante `modelo_cuadratico.predecir()`.
7.  **Visualización de Predicciones**: 
    *   Se genera una gráfica (`prediccion_vs_real.png`) que compara los valores reales (`y_val`) con las predicciones del modelo (`y_pred`) en el conjunto de validación. Esto permite una inspección visual del ajuste del modelo.
    *   Se utiliza `matplotlib.pyplot` para crear un gráfico de dispersión, con etiquetas claras, título y leyenda.
8.  **Visualización de la Curva de Pérdida**: 
    *   Se crea una segunda gráfica (`loss_vs_epochs.png`) que muestra la evolución de la pérdida de entrenamiento (`loss`) y la pérdida de validación (`val_loss`) a lo largo de las épocas. Esta gráfica es fundamental para diagnosticar problemas como el sobreajuste o el subajuste.
9.  **Guardado del Modelo**: El modelo entrenado se guarda en formato HDF5 (`modelo_cuadratico.h5`) utilizando `modelo_cuadratico.model.save()`. Esto permite reutilizar el modelo sin necesidad de reentrenarlo.

## 4. Implementación y Utilidad

### 4.1. Cómo Sirve el Código

El código desarrollado proporciona una solución completa y modular para la aproximación de funciones mediante redes neuronales. La clase `ModeloCuadratico` abstrae la complejidad de TensorFlow/Keras, permitiendo a los usuarios centrarse en la experimentación y el análisis. El script `main.py` demuestra un flujo de trabajo típico en el aprendizaje automático, desde la preparación de datos hasta la evaluación del modelo.

### 4.2. Para Qué Sirve

Este proyecto sirve como una base educativa y práctica para:

*   **Comprender Redes Neuronales**: Ilustra cómo una red neuronal aprende a mapear entradas a salidas en un problema de regresión no lineal.
*   **Programación Orientada a Objetos (POO) en Python**: Demuestra la aplicación de clases y métodos para organizar un proyecto de aprendizaje automático.
*   **Uso de TensorFlow/Keras**: Proporciona un ejemplo práctico de cómo construir, compilar, entrenar y evaluar modelos con estas librerías.
*   **Visualización de Datos**: Enseña a utilizar `matplotlib` para interpretar el rendimiento del modelo y las tendencias de entrenamiento.
*   **Gestión de Datos**: Muestra cómo dividir datos para entrenamiento y validación, una práctica estándar para evitar el sobreajuste.

### 4.3. En Qué se Puede Implementar

Los conceptos y la estructura de este proyecto pueden extenderse y aplicarse en diversas áreas:

*   **Aproximación de Funciones Más Complejas**: Adaptando la arquitectura de la red (más capas, más neuronas, diferentes activaciones) y el optimizador, el modelo puede aproximar funciones matemáticas mucho más complejas o relaciones en datos del mundo real.
*   **Predicción de Series Temporales**: Con ajustes en la entrada y la arquitectura (por ejemplo, usando capas recurrentes como LSTM), se puede predecir el comportamiento futuro de variables como precios de acciones, clima o demanda de productos.
*   **Modelado de Fenómenos Físicos**: En ingeniería y ciencias, las redes neuronales pueden aprender modelos a partir de datos experimentales, lo que es útil cuando las ecuaciones analíticas son difíciles de obtener.
*   **Control de Sistemas**: Los modelos entrenados pueden usarse para predecir el estado de un sistema y diseñar controladores que mantengan el sistema en un estado deseado.
*   **Optimización de Procesos**: En la industria, las redes neuronales pueden modelar la relación entre parámetros de entrada y métricas de rendimiento para optimizar procesos de fabricación o logísticos.

## 5. Conclusiones

Este entregable ha demostrado la implementación de una red neuronal para aproximar la función `y = x²`, destacando la importancia de una estructura de código modular y el uso de herramientas estándar de la industria como TensorFlow, Keras, scikit-learn y Matplotlib. El proyecto no solo cumple con los requisitos técnicos de la tarea, sino que también sienta las bases para explorar aplicaciones más avanzadas del aprendizaje automático en diversos dominios.

## 6. Referencias

*   TensorFlow Documentation: [https://www.tensorflow.org/](https://www.tensorflow.org/)
*   Keras Documentation: [https://keras.io/](https://keras.io/)
*   NumPy Documentation: [https://numpy.org/doc/](https://numpy.org/doc/)
*   Matplotlib Documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
*   Scikit-learn Documentation: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)


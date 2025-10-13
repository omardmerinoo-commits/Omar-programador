# Proyecto TensorFlow: Aproximación de la función y = x^2 con una red neuronal simple

Este proyecto implementa una red neuronal simple utilizando TensorFlow y Keras para aproximar la función cuadrática `y = x^2`. El código está estructurado en una clase `ModeloCuadratico` para facilitar la organización y reutilización.

## Estructura del Proyecto

- `modelo_cuadratico.py`: Contiene la definición de la clase `ModeloCuadratico` con los métodos para generar datos, construir, entrenar y predecir con el modelo.
- `main.py`: Script principal que orquesta la generación de datos, la construcción del modelo, el entrenamiento, la predicción y la visualización de los resultados.
- `prediccion_vs_real.png`: Gráfica que compara las predicciones del modelo con los valores reales.
- `loss_vs_epochs.png`: Gráfica que muestra la curva de pérdida (MSE) durante el entrenamiento del modelo.
- `modelo_cuadratico.h5`: Archivo que guarda el modelo entrenado en formato HDF5.

## Requisitos

Asegúrate de tener Python 3.x instalado. Las siguientes librerías de Python son necesarias:

- `tensorflow`
- `numpy`
- `scikit-learn`
- `matplotlib`

Puedes instalarlas usando pip:

```bash
pip install tensorflow numpy scikit-learn matplotlib
```

## Ejecución del Código

Para ejecutar el proyecto, simplemente corre el script `main.py` desde tu terminal:

```bash
python3 main.py
```

Al ejecutar el script, se realizarán los siguientes pasos:

1. Se generarán 1000 muestras de datos para la función `y = x^2` con ruido.
2. Los datos se dividirán en conjuntos de entrenamiento (80%) y validación (20%).
3. Se construirá una red neuronal secuencial con dos capas densas ocultas y una capa de salida.
4. El modelo se entrenará durante 100 épocas utilizando el optimizador Adam y la función de pérdida de error cuadrático medio (MSE).
5. Se realizarán predicciones sobre el conjunto de validación.
6. Se generarán y guardarán dos gráficas:
   - `prediccion_vs_real.png`: Muestra los valores reales vs. las predicciones del modelo.
   - `loss_vs_epochs.png`: Muestra cómo la pérdida de entrenamiento y validación evoluciona a lo largo de las épocas.
7. El modelo entrenado se guardará en el archivo `modelo_cuadratico.h5`.

## Descripción del Código

### `modelo_cuadratico.py`

La clase `ModeloCuadratico` encapsula toda la lógica del modelo:

- `__init__(self)`: Inicializa el modelo y las variables de historial.
- `generar_datos(self, n_samples: int = 1000, rango: tuple = (-1, 1))`: Genera `n_samples` puntos `x` uniformemente distribuidos en el `rango` especificado y calcula `y = x^2` con ruido gaussiano.
- `construir_modelo(self)`: Define y compila la arquitectura de la red neuronal. Utiliza capas `Dense` con activación `relu` y `adam` como optimizador con `mse` como función de pérdida.
- `entrenar(self, x_train, y_train, x_val, y_val, epochs: int = 100, batch_size: int = 32)`: Entrena el modelo con los datos proporcionados, registrando el historial de entrenamiento.
- `predecir(self, x)`: Realiza predicciones sobre un conjunto de datos `x` utilizando el modelo entrenado.

### `main.py`

El script `main.py` es el punto de entrada del programa. Coordina las siguientes acciones:

1. Crea una instancia de `ModeloCuadratico`.
2. Llama a `generar_datos` para obtener los datos de entrada y salida.
3. Divide los datos en conjuntos de entrenamiento y validación usando `train_test_split` de `sklearn`.
4. Llama a `construir_modelo` para definir la red neuronal.
5. Llama a `entrenar` para iniciar el proceso de aprendizaje del modelo.
6. Utiliza `predecir` para obtener las predicciones del modelo sobre los datos de validación.
7. Genera y guarda las gráficas `prediccion_vs_real.png` y `loss_vs_epochs.png` utilizando `matplotlib`.
8. Guarda el modelo entrenado en `modelo_cuadratico.h5`.


# -*- coding: utf-8 -*-
"""
Proyecto 1: Aproximación de la función y = x² con TensorFlow y Keras.

Este script define e implementa la clase `ModeloCuadratico` para encapsular
todo el flujo de trabajo de un proyecto de aprendizaje automático, incluyendo:
- Generación de datos sintéticos.
- Construcción de un modelo de red neuronal secuencial.
- Entrenamiento del modelo.
- Evaluación y predicción.
- Visualización de resultados.
- Guardado y carga del modelo entrenado.
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import pickle
import time
from functools import wraps

# --- Decoradores para Funcionalidad Adicional ---

def timing(func):
    """Decorador para medir y mostrar el tiempo de ejecución de una función."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[INFO] Tiempo de ejecución de [1m{func.__name__}[0m: [36m{end_time - start_time:.4f}[0m segundos.")
        return result
    return wrapper

# --- Clase Principal del Proyecto: ModeloCuadratico ---

class ModeloCuadratico:
    """Una clase para construir, entrenar y evaluar un modelo de red neuronal
    que aprende la relación y = x².
    """
    def __init__(self, learning_rate=0.001):
        """Inicializa la clase, estableciendo el modelo y el historial como None."""
        self.model = None
        self.history = None
        self.learning_rate = learning_rate
        print("\n[1mInstancia de ModeloCuadratico creada.[0m")

    @timing
    def generar_datos(self, n_samples: int = 1000, rango: tuple = (-10, 10)):
        """Genera datos de entrada (x) y de salida (y = x²) con ruido aleatorio.

        Args:
            n_samples (int): Número de muestras a generar.
            rango (tuple): Rango (min, max) para los valores de x.

        Returns:
            tuple: Una tupla conteniendo los arrays de NumPy (x, y).
        """
        print(f"\n[1m1. Generando {n_samples} muestras de datos en el rango {rango}...[0m")
        x = np.random.uniform(rango[0], rango[1], n_samples)
        y = x**2
        # Añadir un pequeño ruido aleatorio para simular datos del mundo real
        ruido = np.random.normal(0, 0.1, n_samples)
        y += ruido
        print("[32m[ÉXITO][0m Datos generados correctamente.")
        return x, y

    @timing
    def construir_modelo(self):
        """Crea y compila un modelo secuencial de Keras con capas densas."""
        print("\n[1m2. Construyendo el modelo de red neuronal...[0m")
        self.model = keras.Sequential([
            # Capa de entrada: espera un solo valor (x)
            keras.layers.Input(shape=(1,), name="input_layer"),
            
            # Capas ocultas: 64 neuronas cada una con activación ReLU
            # ReLU es una excelente opción para capas ocultas en problemas de regresión
            keras.layers.Dense(64, activation="relu", name="hidden_layer_1"),
            keras.layers.Dense(64, activation="relu", name="hidden_layer_2"),
            
            # Capa de salida: 1 neurona para predecir el valor de y
            # La activación lineal (por defecto) es adecuada para regresión
            keras.layers.Dense(1, name="output_layer")
        ])
        
        # Compilar el modelo
        # Optimizador Adam: eficiente y ampliamente utilizado
        # Pérdida MSE (Mean Squared Error): estándar para problemas de regresión
        optimizer = keras.optimizers.Adam(learning_rate=self.learning_rate)
        self.model.compile(optimizer=optimizer, loss="mean_squared_error", metrics=["mae"])
        
        print("[32m[ÉXITO][0m Modelo construido y compilado.")
        self.model.summary()

    @timing
    def entrenar(self, x_train, y_train, epochs: int = 100, batch_size: int = 32, validation_split=0.2):
        """Entrena el modelo con los datos generados.

        Args:
            x_train (np.array): Datos de entrada para el entrenamiento.
            y_train (np.array): Datos de salida para el entrenamiento.
            epochs (int): Número de épocas para el entrenamiento.
            batch_size (int): Tamaño del lote para el entrenamiento.
            validation_split (float): Porcentaje de datos a usar para validación.
        """
        if self.model is None:
            print("\u001B[31m[ERROR][0m El modelo debe ser construido antes de entrenar. Llama a `construir_modelo()` primero.")
            return

        print(f"\n[1m3. Entrenando el modelo por {epochs} épocas con un tamaño de lote de {batch_size}...[0m")
        
        self.history = self.model.fit(
            x_train,
            y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            verbose=1 # Muestra una barra de progreso
        )
        print("\n[32m[ÉXITO][0m Entrenamiento completado.")

    def predecir(self, x):
        """Devuelve la predicción del modelo para un conjunto de datos x."""
        if self.model is None:
            print("\u001B[31m[ERROR][0m El modelo no ha sido entrenado. Llama a `entrenar()` primero.")
            return None
        
        print(f"\n[1m4. Realizando predicciones...[0m")
        return self.model.predict(x)

    def visualizar_resultados(self, x_test, y_test, y_pred):
        """Genera y guarda una gráfica que compara los valores reales y los predichos."""
        print("\n[1m5. Visualizando resultados: Comparación de predicciones vs. valores reales...[0m")
        plt.figure(figsize=(12, 6))
        
        # Gráfica de predicción vs. real
        plt.subplot(1, 2, 1)
        plt.scatter(x_test, y_test, alpha=0.6, label="Valores Reales", color="blue")
        plt.scatter(x_test, y_pred, alpha=0.6, label="Predicciones del Modelo", color="red")
        plt.title("Predicción vs. Valor Real")
        plt.xlabel("Entrada (x)")
        plt.ylabel("Salida (y)")
        plt.legend()
        plt.grid(True)

        # Gráfica de la pérdida (loss) durante el entrenamiento
        if self.history:
            plt.subplot(1, 2, 2)
            plt.plot(self.history.history["loss"], label="Pérdida de Entrenamiento")
            plt.plot(self.history.history["val_loss"], label="Pérdida de Validación")
            plt.title("Curva de Pérdida (Loss) vs. Épocas")
            plt.xlabel("Época")
            plt.ylabel("Pérdida (MSE)")
            plt.legend()
            plt.grid(True)
        
        plt.tight_layout()
        
        # Guardar la gráfica
        output_filename = "prediccion_vs_real.png"
        plt.savefig(output_filename)
        print(f"\u001B[32m[ÉXITO][0m Gráfica guardada como [1m{output_filename}[0m.")
        plt.show()

    @timing
    def guardar_modelo(self, filepath: str = "modelo_cuadratico.pkl"):
        """Guarda el modelo entrenado y su historial usando pickle."""
        if self.model is None:
            print("\u001B[31m[ERROR][0m No hay un modelo entrenado para guardar.")
            return

        print(f"\n[1m6. Guardando el modelo y el historial en [1m{filepath}[0m...[0m")
        with open(filepath, "wb") as f:
            pickle.dump((self.model, self.history.history), f)
        print(f"\u001B[32m[ÉXITO][0m Modelo guardado correctamente.")

    @classmethod
    @timing
    def cargar_modelo(cls, filepath: str = "modelo_cuadratico.pkl"):
        """Carga un modelo y su historial desde un archivo pickle."""
        print(f"\n[1mCargando modelo y historial desde [1m{filepath}[0m...[0m")
        try:
            with open(filepath, "rb") as f:
                model, history = pickle.load(f)
            
            instancia = cls()
            instancia.model = model
            # Crear un objeto simulado para el historial si es necesario
            class HistoryMock:
                def __init__(self, history_dict):
                    self.history = history_dict
            instancia.history = HistoryMock(history)
            
            print("\u001B[32m[ÉXITO][0m Modelo cargado correctamente.")
            return instancia
        except FileNotFoundError:
            print(f"\u001B[31m[ERROR][0m No se encontró el archivo [1m{filepath}[0m.")
            return None
        except Exception as e:
            print(f"\u001B[31m[ERROR][0m Ocurrió un error al cargar el modelo: {e}")
            return None

# --- Flujo de Ejecución Principal ---

if __name__ == "__main__":
    # --- Fase 1: Entrenamiento y Evaluación Inicial ---
    print("\n[1;34m--- INICIANDO FLUJO DE TRABAJO DE MACHINE LEARNING ---[0m")
    
    # 1. Crear una instancia de la clase
    mi_modelo = ModeloCuadratico(learning_rate=0.001)
    
    # 2. Generar datos
    x_data, y_data = mi_modelo.generar_datos(n_samples=2000, rango=(-20, 20))
    
    # 3. Construir el modelo
    mi_modelo.construir_modelo()
    
    # 4. Entrenar el modelo
    # TensorFlow se encarga de dividir los datos para validación internamente
    mi_modelo.entrenar(x_data, y_data, epochs=150, batch_size=64, validation_split=0.2)
    
    # 5. Realizar predicciones con los mismos datos para comparar
    predicciones = mi_modelo.predecir(x_data)
    
    # 6. Visualizar los resultados
    if predicciones is not None:
        mi_modelo.visualizar_resultados(x_data, y_data, predicciones)
    
    # 7. Guardar el modelo entrenado
    mi_modelo.guardar_modelo()

    # --- Fase 2: Carga y Reutilización del Modelo ---
    print("\n[1;34m--- PROBANDO LA CARGA Y REUTILIZACIÓN DEL MODELO ---[0m")
    
    # 1. Cargar el modelo desde el archivo
    modelo_cargado = ModeloCuadratico.cargar_modelo()
    
    if modelo_cargado:
        # 2. Generar nuevos datos para probar el modelo cargado
        x_nuevos = np.array([-2.5, -1.5, 0.5, 1.5, 2.5, 3.5])
        y_reales_nuevos = x_nuevos**2
        
        # 3. Realizar predicciones con el modelo cargado
        predicciones_nuevas = modelo_cargado.predecir(x_nuevos)
        
        # 4. Mostrar los resultados
        if predicciones_nuevas is not None:
            print("\n[1mResultados con el modelo cargado:[0m")
            for i, x_val in enumerate(x_nuevos):
                print(f"  Entrada: {x_val:.2f}, Valor Real: {y_reales_nuevos[i]:.2f}, Predicción: [35m{predicciones_nuevas[i][0]:.2f}[0m")

    print("\n[1;32m--- PROCESO COMPLETADO ---[0m\n")


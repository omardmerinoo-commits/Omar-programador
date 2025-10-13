import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class ModeloCuadratico:
    def __init__(self):
        self.model = None
        self.history = None
        self.x_train = None
        self.y_train = None
        self.x_val = None
        self.y_val = None

    def generar_datos(self, n_samples: int = 1000, rango: tuple = (-1, 1)):
        np.random.seed(42) # Para reproducibilidad
        x = np.random.uniform(rango[0], rango[1], n_samples)
        y = x**2 + np.random.normal(0, 0.05, n_samples) # y = x^2 con ruido aleatorio
        return x, y

    def construir_modelo(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')
        print("Modelo TensorFlow construido y compilado.")
        self.model.summary()

    def entrenar(self, x_train, y_train, x_val, y_val, epochs: int = 100, batch_size: int = 32):
        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        print(f"Entrenando el modelo por {epochs} épocas con un tamaño de lote de {batch_size}...")
        self.history = self.model.fit(
            self.x_train, self.y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=(self.x_val, self.y_val),
            verbose=0 # No mostrar el progreso de cada época
        )
        print("Entrenamiento completado.")

    def predecir(self, x):
        if self.model is None:
            raise ValueError("El modelo no ha sido construido. Llame a 'construir_modelo()' primero.")
        if self.history is None:
            raise ValueError("El modelo no ha sido entrenado. Llame a 'entrenar()' primero.")
        return self.model.predict(x.reshape(-1, 1))



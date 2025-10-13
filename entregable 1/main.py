import numpy as np
from sklearn.model_selection import train_test_split
from modelo_cuadratico import ModeloCuadratico
import matplotlib.pyplot as plt

def main():
    # 1. Instanciar la clase ModeloCuadratico
    modelo_cuadratico = ModeloCuadratico()

    # 2. Generar datos
    print("Generando datos...")
    x, y = modelo_cuadratico.generar_datos(n_samples=1000, rango=(-1, 1))
    print(f"Datos generados: {len(x)} muestras.")

    # 3. Generar y dividir los datos en conjuntos de entrenamiento y validación (80% entrenamiento, 20% validación)
    print("Dividiendo datos en conjuntos de entrenamiento y validación...")
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)
    print(f"Tamaño del conjunto de entrenamiento: {len(x_train)} muestras.")
    print(f"Tamaño del conjunto de validación: {len(x_val)} muestras.")

    # 4. Construir el modelo
    modelo_cuadratico.construir_modelo()

    # 5. Entrenar el modelo
    modelo_cuadratico.entrenar(x_train, y_train, x_val, y_val, epochs=100, batch_size=32)

    # 6. Realizar predicciones
    print("Realizando predicciones en el conjunto de validación...")
    y_pred = modelo_cuadratico.predecir(x_val)

    # 7. Graficar predicciones vs valores reales
    plt.figure(figsize=(10, 6))
    plt.scatter(x_val, y_val, label='Valores Reales', alpha=0.6)
    plt.scatter(x_val, y_pred, label='Predicciones del Modelo', alpha=0.6)
    plt.title('Predicciones del Modelo vs. Valores Reales')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.savefig('prediccion_vs_real.png')
    print("Gráfica 'prediccion_vs_real.png' guardada.")

    # 8. Graficar la curva de pérdida (loss vs. epochs)
    plt.figure(figsize=(10, 6))
    plt.plot(modelo_cuadratico.history.history['loss'], label='Pérdida de Entrenamiento')
    plt.plot(modelo_cuadratico.history.history['val_loss'], label='Pérdida de Validación')
    plt.title('Curva de Pérdida durante el Entrenamiento')
    plt.xlabel('Época')
    plt.ylabel('Pérdida (MSE)')
    plt.legend()
    plt.grid(True)
    plt.savefig('loss_vs_epochs.png')
    print("Gráfica 'loss_vs_epochs.png' guardada.")

    # Guardar el modelo entrenado
    modelo_cuadratico.model.save('modelo_cuadratico.h5')
    print("Modelo entrenado guardado como 'modelo_cuadratico.h5'.")

if __name__ == "__main__":
    main()


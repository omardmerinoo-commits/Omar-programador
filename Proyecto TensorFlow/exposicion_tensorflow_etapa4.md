## Cuarta Etapa del Proyecto: Visualización y Análisis de Resultados

Una vez que nuestro modelo ha sido entrenado, no basta con saber que el proceso terminó. Necesitamos **evaluar qué tan bien aprendió** y **visualizar su rendimiento** de una manera que sea fácil de interpretar. La cuarta etapa se centra en el uso de herramientas de visualización para analizar los resultados del entrenamiento y las predicciones del modelo.

### 1. Habilidades en Python: Uso de Matplotlib

**Matplotlib** es la librería de visualización de datos más fundamental y extendida en el ecosistema de Python. Permite crear una amplia variedad de gráficos estáticos, animados e interactivos. En el contexto de este proyecto, Matplotlib es la herramienta clave para traducir los números y las métricas del modelo en gráficos comprensibles.

Las habilidades específicas de Matplotlib que se aplican aquí son:

*   **Gráficos de Dispersión (`plt.scatter`):** Son perfectos para comparar dos conjuntos de datos punto por punto. En nuestro caso, los usamos para:
    *   Visualizar los datos originales (los valores `x` y sus correspondientes `y` reales).
    *   Superponer las predicciones del modelo (`y_pred`) sobre los datos reales. Esto nos da una idea visual inmediata de qué tan cerca están las predicciones de la verdad.

*   **Gráficos de Líneas (`plt.plot`):** Son ideales para mostrar la evolución de una variable a lo largo del tiempo o, en nuestro caso, a lo largo de las épocas de entrenamiento. Los usamos para crear la **curva de pérdida (loss curve)**, que muestra cómo la métrica de error (MSE) disminuyó a medida que el modelo aprendía.

*   **Personalización de Gráficos:** Más allá de simplemente trazar los datos, es crucial hacer que los gráficos sean legibles. Esto implica añadir:
    *   Títulos (`plt.title`).
    *   Etiquetas para los ejes X e Y (`plt.xlabel`, `plt.ylabel`).
    *   Leyendas (`plt.legend`) para identificar qué representa cada línea o conjunto de puntos.
    *   Rejillas (`plt.grid`) para facilitar la lectura de los valores.

*   **Guardado de Gráficos (`plt.savefig`):** Una vez creado un gráfico, podemos guardarlo como un archivo de imagen (por ejemplo, `.png`) para incluirlo en informes, presentaciones o, como en este caso, en el archivo `README.md` del repositorio.

### 2. Habilidades en TensorFlow: Graficar Pérdidas y Predicciones

Si bien Matplotlib es la herramienta que crea los gráficos, los **datos** para esos gráficos provienen directamente de TensorFlow y del proceso de entrenamiento.

*   **Historial de Entrenamiento (`history`):** Como se mencionó en la Etapa 2, el método `model.fit()` de Keras devuelve un objeto `history`. Este objeto es un diccionario que contiene la historia de todas las métricas que se monitorearon durante el entrenamiento. Las claves más importantes son:
    *   `loss`: La pérdida del conjunto de entrenamiento en cada época.
    *   `val_loss`: La pérdida del conjunto de validación en cada época.
    *   `mae`, `val_mae`, etc.: Cualquier otra métrica que hayamos incluido al compilar el modelo.

    La habilidad aquí es saber cómo acceder a estos datos (ej. `history.history["loss"]`) y pasarlos a Matplotlib para graficar la curva de aprendizaje.

*   **Predicciones del Modelo (`model.predict`):** Antes de poder visualizar qué tan bien predice el modelo, primero debemos obtener esas predicciones. El método `model.predict(x_test)` toma un conjunto de datos de entrada y devuelve las predicciones correspondientes del modelo. Estas predicciones son las que luego se grafican junto a los valores reales para una comparación visual.

### Conexión con las Etapas Anteriores

La cuarta etapa es el punto culminante donde se **analizan y presentan los resultados** de todo el trabajo anterior:

1.  **Dependencia del Entrenamiento (Etapa 2):** La visualización de la curva de pérdida es completamente dependiente del historial de entrenamiento (`history`) generado en la Etapa 2. Sin el entrenamiento, no hay nada que graficar.

2.  **Uso del Modelo Entrenado (Etapas 1-3):** Para graficar las predicciones, necesitamos un modelo funcional. Este modelo fue **diseñado** en la Etapa 1, **entrenado** en la Etapa 2 y, opcionalmente, **cargado** desde un archivo en la Etapa 3. La Etapa 4 utiliza este modelo final para generar las predicciones que se visualizarán.

3.  **Organización en la Clase (POO):** Siguiendo el paradigma de Programación Orientada a Objetos, toda la lógica de visualización se encapsula en un método `visualizar_resultados` dentro de la clase `ModeloCuadratico`. Este método toma como entrada los datos de prueba y las predicciones, y se encarga de todo el proceso de creación y guardado de los gráficos. Esto mantiene el código limpio y separa las responsabilidades: la clase no solo gestiona el modelo, sino también su evaluación visual.

En esencia, la Etapa 4 responde a la pregunta: **"¿Funcionó? Y si es así, ¿qué tan bien?"**. Proporciona la evidencia visual que valida (o invalida) el éxito de nuestro modelo de aprendizaje automático. Un modelo con una curva de pérdida que no desciende o cuyas predicciones son muy diferentes de los valores reales indica claramente que algo necesita ser ajustado en las etapas anteriores (por ejemplo, la arquitectura del modelo, los hiperparámetros de entrenamiento, o la calidad de los datos).

```python
# Ejemplo de cómo se conectan las etapas en el código:

# ... (Después de entrenar el modelo en la Etapa 2 y obtener las predicciones)

# --- ETAPA 4 ---
predicciones = mi_modelo.predecir(x_data)

# Se pasan los datos originales y las predicciones al método de visualización.
if predicciones is not None:
    mi_modelo.visualizar_resultados(x_data, y_data, predicciones)
```

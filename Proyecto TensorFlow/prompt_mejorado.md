# Prompt Mejorado para el Proyecto de TensorFlow

## Objetivo General

Desarrollar un proyecto completo y de alta calidad utilizando TensorFlow y Python para resolver el problema de aproximar la función `y = x²`. El proyecto debe ser un recurso educativo integral que no solo cumpla con los requisitos técnicos, sino que también sirva como material de aprendizaje para comprender los fundamentos del Machine Learning con TensorFlow.

## Entregables Clave

1.  **Código Fuente del Proyecto (`modelo_cuadratico.py`):**
    *   **Clase `ModeloCuadratico`:** Implementar una clase en Python que encapsule todo el flujo de trabajo del Machine Learning. La clase debe ser robusta, bien documentada y seguir las mejores prácticas de la Programación Orientada a Objetos (POO).
    *   **Métodos Esenciales:** La clase debe incluir, como mínimo, los siguientes métodos:
        *   `generar_datos()`: Para crear datos de entrenamiento y validación.
        *   `construir_modelo()`: Para definir y compilar la arquitectura de la red neuronal con Keras.
        *   `entrenar()`: Para ejecutar el ciclo de entrenamiento del modelo.
        *   `predecir()`: Para realizar predicciones con el modelo entrenado.
        *   `visualizar_resultados()`: Para generar y guardar gráficos del rendimiento del modelo.
        *   `guardar_modelo()`: Para serializar y guardar el modelo entrenado (usando `pickle` o el formato nativo de Keras).
        *   `cargar_modelo()`: Un método de clase para cargar un modelo guardado y reconstruir el estado de la clase.
    *   **Calidad del Código:** El código debe ser limpio, legible, bien comentado (con `docstrings` detallados) y utilizar decoradores (`@timing`, `@wraps`) para añadir funcionalidades como la medición del tiempo de ejecución.

2.  **Exposiciones Detalladas por Fase (Archivos `.md`):**
    *   Crear un archivo Markdown separado para cada una de las 5 etapas del proyecto descritas en la imagen.
    *   Cada exposición debe explicar en detalle:
        *   Las **habilidades de Python** involucradas en esa etapa.
        *   Las **habilidades de TensorFlow** aplicadas.
        *   La **conexión y dependencia** con las etapas anteriores y posteriores.
        *   **Fragmentos de código** relevantes para ilustrar los conceptos.
        *   Una explicación clara de la **teoría** subyacente (ej. ¿qué es una capa `Dense`?, ¿cómo funciona un optimizador?).

3.  **Guiones para Videos Educativos (10 Guiones):**
    *   Generar 10 guiones detallados para una serie de videos de YouTube (aprox. 5 minutos cada uno) que sirvan como una introducción completa a TensorFlow para principiantes.
    *   Los temas deben cubrir desde los conceptos más básicos hasta temas más avanzados, incluyendo:
        1.  ¿Qué es TensorFlow?
        2.  Instalación y primer modelo.
        3.  Capas de Keras.
        4.  Optimizadores y Funciones de Pérdida.
        5.  Ciclo de vida de un proyecto de ML.
        6.  Sobreajuste (Overfitting).
        7.  Clasificación de Imágenes.
        8.  Redes Neuronales Convolucionales (CNNs).
        9.  Aprendizaje por Transferencia (Transfer Learning).
        10. Despliegue de Modelos (TFLite, TF.js, etc.).
    *   Cada guion debe incluir indicaciones para el host, animaciones sugeridas y el código a mostrar, con un enfoque en ser claro, conciso y atractivo.

4.  **Artefactos Generados por el Modelo:**
    *   **`prediccion_vs_real.png`:** Una gráfica de alta calidad que compare visualmente los valores reales con las predicciones del modelo y muestre la curva de aprendizaje (pérdida vs. épocas).
    *   **`modelo_cuadratico.pkl`:** El archivo del modelo entrenado y guardado.

5.  **Documentación del Repositorio (`README.md`):**
    *   Un archivo `README.md` completo que sirva como la guía principal del proyecto, incluyendo:
        *   Descripción del proyecto.
        *   Instrucciones de instalación de dependencias.
        *   Guía paso a paso para ejecutar el script.
        *   Explicación de los archivos del repositorio.
        *   Inclusión de la gráfica de resultados generada.

## Instrucción de Tono y Calidad

El desarrollo debe realizarse desde la perspectiva de un experto en Machine Learning y un educador. El objetivo no es solo "hacer que funcione", sino "hacerlo bien, explicarlo bien y hacerlo reutilizable". El código debe ser de calidad de producción y los materiales educativos (exposiciones y guiones) deben ser claros, precisos y didácticos.

## Primera Etapa del Proyecto: Fundamentos y Creación del Modelo

La primera etapa del proyecto se enfoca en los **Fundamentos** de Python y la creación de un **Modelo Secuencial** en TensorFlow. Esto implica:

### 1. Habilidades en Python: Clases, Métodos y Objetos

En esta fase, se aplica la Programación Orientada a Objetos (POO) en Python, creando una clase `ModeloCuadratico` que encapsula toda la lógica del proyecto. Se implementan métodos para manejar las diferentes funcionalidades, como la generación de datos, la construcción del modelo, el entrenamiento y la predicción.

### 2. Habilidades en TensorFlow: Crear y Compilar un Modelo Secuencial

Se utiliza TensorFlow (específicamente la API Keras) para:

*   **Crear un Modelo Secuencial:** Se define la arquitectura de la red neuronal como una pila lineal de capas.
*   **Añadir Capas Densas:** Se añaden capas `Dense` para aprender las características de los datos.
*   **Compilar el Modelo:** Se configura el proceso de aprendizaje, especificando un optimizador (ej. `Adam`), una función de pérdida (ej. `mean_squared_error`) y métricas para monitorear el rendimiento.

El objetivo de esta etapa es tener un modelo de red neuronal funcional, aunque aún no entrenado, listo para aprender la relación `y = x²`.

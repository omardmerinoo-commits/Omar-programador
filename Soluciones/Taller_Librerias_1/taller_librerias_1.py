import pandas as pd
import numpy as np
import math

# Ejercicio 1: Análisis de Datos con Pandas y Numpy
print("\n--- Ejercicio 1: Análisis de Datos con Pandas y Numpy ---")

def analizar_datos(filepath, **kwargs):
    try:
        df = pd.read_csv(filepath)
        print("DataFrame cargado exitosamente.")

        # Mostrar las primeras filas
        if kwargs.get("head", False):
            print("\nPrimeras 5 filas:\n", df.head())

        # Describir datos numéricos
        if kwargs.get("describe", False):
            print("\nEstadísticas descriptivas:\n", df.describe())

        # Contar valores únicos en una columna específica
        column_to_count = kwargs.get("count_unique_col")
        if column_to_count and column_to_count in df.columns:
            print(f"\nValores únicos en '{column_to_count}':\n", df[column_to_count].value_counts())

        # Filtrar por un valor en una columna
        filter_col = kwargs.get("filter_column")
        filter_val = kwargs.get("filter_value")
        if filter_col and filter_val and filter_col in df.columns:
            filtered_df = df[df[filter_col] == filter_val]
            print(f"\nFiltrado por '{filter_col}' == '{filter_val}':\n", filtered_df.head())

        # Calcular la media de una columna numérica
        mean_col = kwargs.get("mean_column")
        if mean_col and mean_col in df.columns and pd.api.types.is_numeric_dtype(df[mean_col]):
            print(f"\nMedia de '{mean_col}': {df[mean_col].mean():.2f}")

    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Crear un archivo CSV de ejemplo para el Ejercicio 1
data = {
    'Nombre': ['Ana', 'Luis', 'Maria', 'Pedro', 'Laura'],
    'Edad': [24, 30, 22, 35, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Sevilla'],
    'Puntuacion': [85, 92, 78, 88, 95]
}
df_ej1 = pd.DataFrame(data)
df_ej1.to_csv('datos_ejercicio1.csv', index=False)

analizar_datos('datos_ejercicio1.csv', head=True, describe=True, count_unique_col='Ciudad', filter_column='Ciudad', filter_value='Madrid', mean_column='Puntuacion')


# Ejercicio 2: Comprensión de Generadores y Funciones con Serie de Taylor
print("\n--- Ejercicio 2: Comprensión de Generadores y Funciones con Serie de Taylor ---")

def generador_taylor(x, num_terms=10, **kwargs):
    """Generador para la serie de Taylor de e^x."""
    current_term = 1.0
    sum_series = 0.0
    for n in range(num_terms):
        sum_series += current_term
        yield sum_series
        current_term = current_term * x / (n + 1)

# Ejemplo de uso
x_val = 1.0
terms = 5
print(f"\nSerie de Taylor para e^{x_val} con {terms} términos:")
for i, val in enumerate(generador_taylor(x_val, num_terms=terms)):
    print(f"  Término {i+1}: {val:.6f}")

# Comparar con math.exp(x)
print(f"  Valor real de e^{x_val}: {math.exp(x_val):.6f}")


# Ejercicio 3: Clases, Objetos, Excepciones y *args y **kwargs
print("\n--- Ejercicio 3: Clases, Objetos, Excepciones y *args y **kwargs ---")

class Particula:
    def __init__(self, masa, velocidad, **kwargs):
        if not isinstance(masa, (int, float)) or masa <= 0:
            raise ValueError("La masa debe ser un número positivo.")
        if not isinstance(velocidad, (int, float)) or velocidad < 0:
            raise ValueError("La velocidad debe ser un número no negativo.")
        self._masa = masa
        self._velocidad = velocidad
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def masa(self):
        return self._masa

    @masa.setter
    def masa(self, new_masa):
        if not isinstance(new_masa, (int, float)) or new_masa <= 0:
            raise ValueError("La masa debe ser un número positivo.")
        self._masa = new_masa

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, new_velocidad):
        if not isinstance(new_velocidad, (int, float)) or new_velocidad < 0:
            raise ValueError("La velocidad debe ser un número no negativo.")
        self._velocidad = new_velocidad

    def energia_cinetica(self):
        return 0.5 * self.masa * (self.velocidad ** 2)

# Ejemplo de uso
try:
    p1 = Particula(masa=10, velocidad=5, color='rojo', forma='esfera')
    print(f"\nPartícula 1: Masa={p1.masa}kg, Velocidad={p1.velocidad}m/s, Color={p1.color}, Forma={p1.forma}")
    print(f"Energía cinética de P1: {p1.energia_cinetica()} Joules")

    p1.masa = 12
    print(f"Nueva masa de P1: {p1.masa}kg")

    p2 = Particula(masa=2, velocidad=10)
    print(f"Partícula 2: Masa={p2.masa}kg, Velocidad={p2.velocidad}m/s")
    print(f"Energía cinética de P2: {p2.energia_cinetica()} Joules")

    # Intento de crear partícula con masa inválida
    # p_invalida = Particula(masa=-1, velocidad=5)
except ValueError as e:
    print(f"Error al crear partícula: {e}")


# Ejercicio 4: Álgebra Lineal con Pandas y Numpy
print("\n--- Ejercicio 4: Álgebra Lineal con Pandas y Numpy ---")

def resolver_sistema_lineal(A, B, **kwargs):
    """Resuelve un sistema de ecuaciones lineales Ax = B y verifica la solución."""
    try:
        # Convertir a arrays de NumPy si no lo son
        A_np = np.array(A)
        B_np = np.array(B)

        # Verificar que A sea una matriz cuadrada y que las dimensiones coincidan
        if A_np.shape[0] != A_np.shape[1]:
            raise ValueError("La matriz A debe ser cuadrada.")
        if A_np.shape[0] != B_np.shape[0]:
            raise ValueError("Las dimensiones de A y B no coinciden.")

        # Resolver el sistema
        x = np.linalg.solve(A_np, B_np)
        print("\nSolución del sistema (x):\n", x)

        # Verificar la solución
        if kwargs.get("verificar", False):
            B_reconstruido = np.dot(A_np, x)
            print("\nVector B reconstruido (A * x):\n", B_reconstruido)
            if np.allclose(B_np, B_reconstruido):
                print("La solución es correcta (A * x == B).")
            else:
                print("La solución no es correcta (A * x != B).")
        return x

    except np.linalg.LinAlgError as e:
        print(f"Error de álgebra lineal: {e} (posiblemente matriz singular o no invertible).")
        return None
    except ValueError as e:
        print(f"Error de valor: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

# Ejemplo de uso
A_matrix = [[2, 1], [1, -1]]
B_vector = [3, 0]

print("\nSistema de ecuaciones:")
print("A =", A_matrix)
print("B =", B_vector)

solucion = resolver_sistema_lineal(A_matrix, B_vector, verificar=True)

# Otro ejemplo con Pandas DataFrame (aunque numpy es más directo para álgebra lineal)
df_A = pd.DataFrame([[3, 2], [1, 4]])
df_B = pd.Series([7, 9])

print("\nSistema de ecuaciones con DataFrames de Pandas:")
print("A =\n", df_A)
print("B =\n", df_B)

solucion_df = resolver_sistema_lineal(df_A.values, df_B.values, verificar=True)



import math
import pandas as pd

# Generador de serie de Fibonacci
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Comprensión de generadores para números pares
def even_numbers_generator(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

print("\n--- Taller Generadores y gestión de datos ---")
print("\n--- Punto 1: Generador de serie de Fibonacci y comprensión de generadores para números pares ---")

print("Serie de Fibonacci (primeros 10 números):")
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

print("\nNúmeros pares hasta 20:")
even_gen = even_numbers_generator(20)
for num in even_gen:
    print(num)





# Punto 2: Leer archivo CSV de estudiantes, calcular promedios, identificar reprobados y top 10%
print("\n--- Punto 2: Procesamiento de datos de estudiantes desde CSV ---")

# Simular un archivo CSV de estudiantes
# En un escenario real, esto se leería de un archivo.
student_data = [
    "nombre,nota1,nota2,nota3",
    "Juan,4.5,3.8,4.2",
    "Maria,3.0,2.5,3.2",
    "Pedro,5.0,4.9,4.8",
    "Ana,2.0,1.5,2.2",
    "Luis,4.0,4.1,3.9",
    "Laura,3.5,3.0,3.3",
    "Carlos,4.8,4.7,4.9",
    "Sofia,2.8,2.0,2.5",
    "Diego,3.9,3.7,3.8",
    "Elena,4.2,4.0,4.1"
]

# Guardar la simulación en un archivo temporal para lectura
with open("estudiantes.csv", "w") as f:
    for line in student_data:
        f.write(line + "\n")

def process_students_csv(filepath):
    students = []
    try:
        with open(filepath, "r") as f:
            header = f.readline().strip().split(",")
            for line in f:
                data = line.strip().split(",")
                student = {
                    "nombre": data[0],
                    "notas": [float(n) for n in data[1:]]
                }
                student["promedio"] = sum(student["notas"]) / len(student["notas"])
                students.append(student)
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no se encontró.")
        return []
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []

    # Identificar reprobados (promedio < 3.0)
    reprobados = [s for s in students if s["promedio"] < 3.0]

    # Identificar top 10%
    students.sort(key=lambda x: x["promedio"], reverse=True)
    top_10_percent_count = max(1, int(len(students) * 0.10))
    top_10_percent = students[:top_10_percent_count]

    print("\nPromedios de estudiantes:")
    for s in students:
        print(f'  {s["nombre"]}: {s["promedio"]:.2f}')

    print("\nEstudiantes reprobados:")
    if reprobados:
        for s in reprobados:
            print(f'  {s["nombre"]}: {s["promedio"]:.2f}')
    else:
        print("  No hay estudiantes reprobados.")

    print("\nTop 10% de estudiantes:")
    if top_10_percent:
        for s in top_10_percent:
            print(f'  {s["nombre"]}: {s["promedio"]:.2f}')
    else:
        print("  No hay suficientes estudiantes para calcular el top 10%.")

process_students_csv("estudiantes.csv")





# Punto 3: Manipular datos de Titanic con Pandas (sobrevivientes vs no sobrevivientes)
print("\n--- Punto 3: Manipulación de datos de Titanic con Pandas ---")

# Descargar el dataset de Titanic si no existe
try:
    titanic_df = pd.read_csv("titanic.csv")
    print("Dataset de Titanic cargado exitosamente.")
except FileNotFoundError:
    print("Descargando el dataset de Titanic...")
    # Usar una URL de un dataset público de Titanic
    titanic_url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    try:
        titanic_df = pd.read_csv(titanic_url)
        titanic_df.to_csv("titanic.csv", index=False)
        print("Dataset de Titanic descargado y guardado como titanic.csv")
    except Exception as e:
        print(f"Error al descargar el dataset de Titanic: {e}")
        titanic_df = pd.DataFrame() # Crear un DataFrame vacío para evitar errores posteriores

if not titanic_df.empty:
    # Sobrevivientes vs No Sobrevivientes
    survived_counts = titanic_df["Survived"].value_counts()
    print("\nConteo de Sobrevivientes (1) y No Sobrevivientes (0):\n", survived_counts)

    # Porcentaje de sobrevivientes
    total_passengers = len(titanic_df)
    if total_passengers > 0:
        percentage_survived = (survived_counts.get(1, 0) / total_passengers) * 100
        print(f"\nPorcentaje de sobrevivientes: {percentage_survived:.2f}%")
    else:
        print("No hay datos de pasajeros para calcular el porcentaje de sobrevivientes.")

    # Sobrevivientes por género
    survived_by_sex = titanic_df.groupby("Sex")["Survived"].value_counts(normalize=True).unstack()
    print("\nPorcentaje de Sobrevivientes por Género:\n", survived_by_sex)
else:
    print("No se pudo procesar el dataset de Titanic debido a un error de carga.")





# Punto 4: Exportar lista de diccionarios de empleados a JSON.
print("\n--- Punto 4: Exportar lista de diccionarios de empleados a JSON ---")

import json

employees = [
    {"id": 1, "nombre": "Alice", "departamento": "HR", "salario": 60000},
    {"id": 2, "nombre": "Bob", "departamento": "IT", "salario": 75000},
    {"id": 3, "nombre": "Charlie", "departamento": "HR", "salario": 62000},
    {"id": 4, "nombre": "David", "departamento": "Finance", "salario": 80000}
]

output_json_file = "empleados.json"

with open(output_json_file, "w") as f:
    json.dump(employees, f, indent=4)

print(f"Lista de empleados exportada a {output_json_file}")





# Punto 5: Leer archivo de texto con números, generar suma acumulativa sin librerías.
print("\n--- Punto 5: Suma acumulativa de números desde archivo de texto ---")

# Simular un archivo de texto con números
numbers_data = "10\n20\n5\n15\n30"
with open("numeros.txt", "w") as f:
    f.write(numbers_data)

def cumulative_sum_from_file(filepath):
    cumulative_sum = 0
    try:
        with open(filepath, "r") as f:
            for line in f:
                try:
                    number = int(line.strip())
                    cumulative_sum += number
                    print(f"Suma acumulativa: {cumulative_sum}")
                except ValueError:
                    print(f"Advertencia: Ignorando línea no numérica: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

cumulative_sum_from_file("numeros.txt")





# Punto 6: Función que toma lista de palabras y devuelve generador de palabras con más de 5 letras.
print("\n--- Punto 6: Generador de palabras largas ---")

def long_words_generator(word_list):
    for word in word_list:
        if len(word) > 5:
            yield word

words = ["manzana", "sol", "elefante", "casa", "computadora", "flor"]

print("Palabras con más de 5 letras:")
for lw in long_words_generator(words):
    print(lw)





# Punto 7: Clase para procesar texto: leer archivo, método para lista de tuplas (párrafo, longitud), método para N párrafos más largos sin librerías.
print("\n--- Punto 7: Clase para procesamiento de texto ---")

class TextProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.paragraphs = []
        self._read_file()

    def _read_file(self):
        try:
            with open(self.filepath, "r") as f:
                content = f.read()
                # Dividir el contenido en párrafos. Asumo que los párrafos están separados por doble salto de línea.
                self.paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        except FileNotFoundError:
            print(f"Error: El archivo {self.filepath} no se encontró.")
            self.paragraphs = []
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            self.paragraphs = []

    def get_paragraphs_with_length(self):
        return [(p, len(p)) for p in self.paragraphs]

    def get_n_longest_paragraphs(self, n):
        # Ordenar los párrafos por longitud de forma descendente
        sorted_paragraphs = sorted(self.paragraphs, key=len, reverse=True)
        return sorted_paragraphs[:n]

# Simular un archivo de texto para el procesamiento
text_data = """
Este es el primer párrafo. Es un párrafo corto.

Este es el segundo párrafo. Es un poco más largo que el primero, con más palabras y detalles.

El tercer párrafo es el más extenso de todos, diseñado para probar la funcionalidad de encontrar los párrafos más largos. Contiene mucha información y varias oraciones complejas para asegurar una buena longitud.

Cuarto párrafo, también corto.

Quinto y último párrafo. Este es de longitud media.
"""

with open("sample_text.txt", "w") as f:
    f.write(text_data)

processor = TextProcessor("sample_text.txt")

print("\nPárrafos con su longitud:")
for p, length in processor.get_paragraphs_with_length():
    print(f"  Párrafo: \"{p[:50]}...\" (Longitud: {length})")

print("\nLos 2 párrafos más largos:")
for p in processor.get_n_longest_paragraphs(2):
    print(f"  - \"{p[:50]}...\" (Longitud: {len(p)})")





# Punto 8: Leer archivo JSON de productos, generar productos con precio superior a umbral.
print("\n--- Punto 8: Generador de productos por umbral de precio ---")

# Simular un archivo JSON de productos
products_data = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 75},
    {"id": 4, "nombre": "Monitor", "precio": 300},
    {"id": 5, "nombre": "Webcam", "precio": 50},
    {"id": 6, "nombre": "Auriculares", "precio": 150}
]

with open("productos.json", "w") as f:
    json.dump(products_data, f, indent=4)

def products_above_price_generator(filepath, threshold):
    try:
        with open(filepath, "r") as f:
            products = json.load(f)
            for product in products:
                if product.get("precio", 0) > threshold:
                    yield product
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: El archivo {filepath} no es un JSON válido.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

price_threshold = 100
print(f"\nProductos con precio superior a {price_threshold}:")
for product in products_above_price_generator("productos.json", price_threshold):
    print(f'  - {product["nombre"]}: ${product["precio"]}')



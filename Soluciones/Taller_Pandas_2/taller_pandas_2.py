



import pandas as pd
import numpy as np

# 1. Realice un programa que importe el archivo compartido “COVID-19_Colombia.csv” y
# visualice el encabezado del mismo (primeras cinco columnas)

print("\n--- Punto 1: Importar y visualizar encabezado ---")
try:
    df = pd.read_csv("COVID-19_Colombia.csv")
    print("Encabezado del DataFrame:\n", df.head())
except FileNotFoundError:
    print("Error: El archivo COVID-19_Colombia.csv no se encontró. Asegúrese de que esté en el mismo directorio.")





# 2. Identifique los valores repetidos en cada columna y los unifique (Ejemplo: Todos los
# valores de Armeniia, ARMENIA y Armenia deben unificarse en ARMENIA)

print("\n--- Punto 2: Identificar y unificar valores repetidos ---")
# Unificar valores en la columna 'ciudad' (ejemplo)
# Convertir a minúsculas y luego a mayúsculas para estandarizar
if 'ciudad' in df.columns:
    df['ciudad'] = df['ciudad'].str.lower().str.upper()
    print("Valores únicos en la columna 'ciudad' después de unificación:\n", df['ciudad'].unique())
else:
    print("La columna 'ciudad' no se encontró en el DataFrame.")





# 3. Cambie los valores nulos por 0 en las columnas en que sea más conveniente. Justificando
# su elección

print("\n--- Punto 3: Manejo de valores nulos ---")
# Identificar columnas con valores nulos
print("Valores nulos antes de la manipulación:\n", df.isnull().sum())

# Justificación: Para columnas numéricas que representan conteos (como las de edad o casos),
# un valor nulo puede interpretarse como la ausencia de casos o un conteo de cero.
# Cambiar a 0 es conveniente para análisis numéricos y evitar errores en cálculos.

# Columnas a considerar para reemplazar nulos por 0 (ejemplo, ajustar según el dataset real)
# Asumo que las columnas de rangos de edad (0_a_9, 10_a_19, etc.) y las de género (femenino, masculino)
# son las más convenientes para reemplazar nulos por 0, ya que representan conteos.
columns_to_fill_zero = [col for col in df.columns if col.startswith(("0_a_", "10_a_", "20_a_", "30_a_", "40_a_", "50_a_", "60_a_", "70_a_", "80_a_", "90_", "femenino", "masculino", "importado", "asociado"))]

for col in columns_to_fill_zero:
    if col in df.columns:
        df[col] = df[col].fillna(0)

print("Valores nulos después de la manipulación:\n", df.isnull().sum())





# 4. Cambie las columnas que tienen fechas al formato de pandas datetime y genere para
# cada caso nuevas columnas con día, mes y año (Ejemplo: En la columna Fecha de
# notificación aparece una fecha 14/3/2020 0:00:00, esta columna debe ser un datetime
# correcto y se deben crear tres nuevas columnas en la tabla, una con el dia 14, otra con
# el mes 3 y otra con el año 2020)

print("\n--- Punto 4: Conversión de fechas y extracción de componentes ---")
# Identificar columnas que parecen ser fechas
date_columns = [col for col in df.columns if 'fecha' in col.lower()]

for col in date_columns:
    if col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df[f'{col}_dia'] = df[col].dt.day
            df[f'{col}_mes'] = df[col].dt.month
            df[f'{col}_año'] = df[col].dt.year
            print(f"Columna \'{col}\' convertida a datetime y componentes extraídos.")
            print(df[[col, f'{col}_dia', f'{col}_mes', f'{col}_año']].head())
        except Exception as e:
            print(f"No se pudo convertir la columna \'{col}\' a datetime: {e}")





# 5. Elija un departamento y extraiga en vectores de numpy los fallecidos, graves, leves y
# moderados por cada ciudad del departamento de su elección.

print("\n--- Punto 5: Extracción de datos por departamento y ciudad ---")
# Asumiendo que la columna de departamento/ciudad es 'ciudad'
# Y que las columnas de casos son 'fallecido', 'grave', 'leve', 'moderado'
# (Necesitaría verificar los nombres exactos de las columnas en el CSV real)

# Para este ejemplo, usaré las columnas que parecen ser conteos de casos
# Basado en el `df.head()` y el contenido del PDF, las columnas relevantes son:
# 0_a_9, 10_a_19, ..., 90+, femenino, masculino, importado, asociado
# El PDF menciona 'fallecidos, graves, leves y moderados', pero el CSV no parece tener esas columnas explícitamente.
# Voy a asumir que se refiere a conteos de casos por edad/género o que el CSV es una versión simplificada.
# Si el CSV tuviera esas columnas, el código se adaptaría fácilmente.

# Voy a elegir el departamento/ciudad 'BOGOTA' como ejemplo.
departamento_elegido = "BOGOTA"

df_departamento = df[df["ciudad"] == departamento_elegido]

# Columnas que podrían representar los estados (ajustar según el CSV real)
# Para este ejemplo, usaré las columnas de rango de edad como sustituto si no hay otras más claras.
# Si el CSV tuviera columnas como 'fallecidos', 'graves', 'leves', 'moderados', se usarían esas.

# Voy a usar las columnas de rangos de edad como ejemplo de 'casos' para este punto,
# ya que el CSV descargado no tiene 'fallecidos', 'graves', 'leves', 'moderados' explícitamente.
# Si el CSV original del taller fuera diferente, estas columnas deberían ajustarse.

# Identificar columnas de casos (ejemplo con rangos de edad)
columnas_casos = [col for col in df.columns if col.startswith(("0_a_", "10_a_", "20_a_", "30_a_", "40_a_", "50_a_", "60_a_", "70_a_", "80_a_", "90_"))]

# Agrupar por ciudad dentro del departamento y sumar los casos
if not df_departamento.empty:
    print(f"Datos para el departamento/ciudad: {departamento_elegido}")
    for ciudad in df_departamento["ciudad"].unique():
        df_ciudad = df_departamento[df_departamento["ciudad"] == ciudad]
        print(f"\nCiudad: {ciudad}")
        for col_caso in columnas_casos:
            if col_caso in df_ciudad.columns:
                # Sumar los casos para esa ciudad y columna específica
                casos_ciudad = df_ciudad[col_caso].sum()
                # Convertir a vector de numpy (aunque sea un solo valor, para cumplir el requisito)
                vector_casos = np.array([casos_ciudad])
                print(f"  {col_caso}: {vector_casos}")
else:
    print(f"No se encontraron datos para el departamento/ciudad: {departamento_elegido}")





# 6. Generar una matriz de numpy con la información de:
# Días transcurridos desde la primera fecha que aparece en el DataFrame.
# Muertes de hombres para las respectivas fechas de la anterior columna
# Muertes de mujeres para las respectivas fechas de la anterior columna
# Recuperaciones de hombres para las respectivas fechas de la anterior columna
# Recuperaciones de mujeres para las respectivas fechas de la anterior columna

print("\n--- Punto 6: Generación de matriz NumPy con datos temporales y de género ---")

# Asegurarse de que la columna de fecha principal esté en formato datetime
# Asumo que la columna principal de fecha es 'fecha' o 'fecha_notificacion'
# Basado en el CSV, la columna de fecha es 'fecha'
if 'fecha' in df.columns:
    df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')
    df = df.dropna(subset=["fecha"])
    df = df.sort_values(by="fecha").reset_index(drop=True)

    # Días transcurridos desde la primera fecha
    fecha_inicio = df["fecha"].min()
    df["dias_transcurridos"] = (df["fecha"] - fecha_inicio).dt.days

    # Para las columnas de muertes y recuperaciones por género, el CSV descargado no las tiene explícitamente.
    # El CSV tiene columnas como 'femenino' y 'masculino' que parecen ser conteos de casos por género.
    # Voy a asumir que 'femenino' y 'masculino' se refieren a casos generales por género, no específicamente a muertes o recuperaciones.
    # Si el taller original tuviera un CSV con esas columnas, el código se adaptaría.

    # Para este ejemplo, voy a usar las columnas 'femenino' y 'masculino' como proxy para 'casos por género'.
    # Si se necesitaran 'muertes' o 'recuperaciones', se buscarían columnas con nombres similares en el CSV real.

    # Agrupar por fecha y sumar los casos por género
    df_agrupado_fecha = df.groupby("fecha").agg({
        "dias_transcurridos": "first",
        "masculino": "sum",
        "femenino": "sum"
    }).reset_index()

    # Crear una matriz NumPy
    # Columnas: Días transcurridos, Casos Masculinos, Casos Femeninos
    # Si hubiera columnas de muertes/recuperaciones, se añadirían aquí.
    matriz_numpy = df_agrupado_fecha[["dias_transcurridos", "masculino", "femenino"]].to_numpy()

    print("Matriz NumPy generada (Días transcurridos, Casos Masculinos, Casos Femeninos):\n", matriz_numpy)
    print("Dimensiones de la matriz NumPy:", matriz_numpy.shape)
else:
    print("La columna 'fecha' no se encontró en el DataFrame, no se pudo generar la matriz NumPy.")





# 7. Exporte una nueva tabla donde solo aparezca la información del departamento selec-
# cionado

print("\n--- Punto 7: Exportar tabla del departamento seleccionado ---")
# Usar el departamento_elegido definido en el punto 5
if not df_departamento.empty:
    output_filename = f"COVID-19_{departamento_elegido}.csv"
    df_departamento.to_csv(output_filename, index=False)
    print(f"Tabla del departamento \'{departamento_elegido}\' exportada a {output_filename}")
else:
    print(f"No hay datos para el departamento \'{departamento_elegido}\' para exportar.")




# Librerías
import pandas as pd
import os

# Función para cargar el archivo CSV


def load_dataframe(file_path):
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"Error: No se encontró el archivo en {file_path}")
        return None

    # Intentar cargar el archivo CSV
    try:
        df = pd.read_csv(file_path)
        print("El archivo fue cargado con éxito.")
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None


# Ruta del archivo CSV
csv_ruta = '../../data/csv/history.csv'

# Cargar el DataFrame usando la función
df = load_dataframe(csv_ruta)

# Verificar si el DataFrame se cargó correctamente
if df is not None:
    # Eliminar espacios en blanco en los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Buscar columnas que contengan 'precip'
    precip_columns = [col for col in df.columns if 'precip' in col.lower()]

    # Verificar si se encontraron columnas relacionadas con la precipitación
    if not precip_columns:
        print("No se encontraron columnas relacionadas con precipitación.")
    else:
        # Imprimir estadísticas de las columnas de precipitación
        print("Estadísticas de las columnas de precipitación:\n")
        for col in precip_columns:
            print(f"Columna: {col}")
            print(f"  Media: {df[col].mean()}")
            print(f"  Suma: {df[col].sum()}")
            print(f"  Desviación Estándar: {df[col].std()}\n")
else:
    print("No se pudo cargar el DataFrame.")

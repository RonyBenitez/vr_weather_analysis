import pandas as pd
import numpy as np
import sympy as sp
import os
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing


# Función para cargar el archivo CSV
def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Error: No se encontró el archivo en {file_path}")
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        if 'precip_total' not in df.columns:
            raise ValueError(
                "El archivo CSV no contiene la columna 'precip_total'.")
        print("El archivo fue cargado con éxito.")
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None


# Función para validar entrada numérica
def validate_input(mensaje, min_val, max_val):
    while True:
        try:
            valor = float(input(mensaje))
            if min_val < valor < max_val:
                return valor
            else:
                print(
                    f"Error: El valor debe estar entre {min_val} y {max_val}")
        except ValueError:
            print("Error: Ingrese un número válido.")


# Función para calcular el caudal
def calculate_flow(df, coef_escorrentia, area_captacion, tiempo_concentracion):
    df['intensidad_lluvia'] = df['precip_total'] / \
        (tiempo_concentracion * 3600)
    df['caudal'] = coef_escorrentia * \
        df['intensidad_lluvia'] * (area_captacion * 10000)
    return df


# Función para calcular el diámetro de la alcantarilla
def calculate_diameter(df, coef_manning, pendiente):
    D = sp.Symbol('D', positive=True)
    R = D / 4
    A = sp.pi * (R**2)
    df['diametro_recomendado'] = df['caudal'].apply(
        lambda Q: sp.solve(sp.Eq(Q, (1 / coef_manning) *
                           A * (R**(2/3)) * (pendiente**0.5)), D)
    )
    df['diametro_recomendado'] = df['diametro_recomendado'].apply(
        lambda x: x[0] if x else None)
    return df


# Función para predecir precipitaciones futuras
def predict_precipitation(df, months_to_predict):
    try:
        model = ExponentialSmoothing(
            df['precip_total'], trend='add', seasonal='add', seasonal_periods=12, damped_trend=True)
        fit = model.fit()
        predictions = fit.forecast(months_to_predict)
        if predictions.max() > 1000:
            print("Advertencia: Las predicciones de precipitación parecen ser incorrectas. Verifique los datos de entrada.")
        else:
            return predictions
    except Exception as e:
        print(f"Error al predecir precipitaciones: {e}")
        return None


# Función para generar gráficos
def generate_plots(df):
    plt.figure(figsize=(12, 6))

    # Gráfico de caudal
    plt.subplot(2, 1, 1)
    plt.plot(df['year_month'], df['caudal'], label='Caudal (m³/s)', color='b')
    plt.xlabel('Mes')
    plt.ylabel('Caudal (m³/s)')
    plt.title('Relación entre Precipitación y Caudal')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()

    # Gráfico de diámetro recomendado
    plt.subplot(2, 1, 2)
    plt.plot(df['year_month'], df['diametro_recomendado'],
             label='Diámetro Recomendado (m)', color='r')
    plt.xlabel('Mes')
    plt.ylabel('Diámetro (m)')
    plt.title('Diámetro Recomendado de la Alcantarilla a lo Largo del Tiempo')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()

    plt.tight_layout()
    plt.show(block=True)


# Función para guardar resultados en CSV
def save_results(df, output_path):
    df[['year_month', 'precip_total', 'caudal', 'diametro_recomendado']].to_csv(
        output_path, index=False)
    print(f"Archivo CSV generado con éxito en {output_path}")


# Función principal
def main():
    # Obtener datos del usuario
    pendiente = validate_input(
        "Ingrese la pendiente del terreno (0 < p < 1): ", 0, 1)
    tiempo_concentracion = validate_input(
        "Ingrese el tiempo de concentración en horas (>0): ", 0.01, 100)
    area_captacion = validate_input(
        "Ingrese el área de captación en hectáreas (0 < A < 1000): ", 0, 1000)

    # Selección del coeficiente de escorrentía
    tipo_terreno = {'Pavimento': 0.6, 'Tierra': 0.3}
    while True:
        material = input(
            "Ingrese el tipo de terreno (Pavimento/Tierra): ").capitalize()
        if material in tipo_terreno:
            coef_escorrentia = tipo_terreno[material]
            break
        else:
            print("Error: Seleccione una opción válida.")

    # Selección del material de la alcantarilla
    materiales_manning = {
        "concreto liso": 0.012, "concreto rugoso": 0.015, "pvc": 0.009,
        "acero corrugado": 0.024, "polietileno hdpe": 0.012, "ladrillo": 0.017,
        "hormigón armado": 0.013, "canal de tierra": 0.025, "canal de roca": 0.035,
        "mampostería de piedra": 0.030
    }

    while True:
        print("Materiales disponibles:")
        for material in materiales_manning.keys():
            print(f"- {material.capitalize()}")

        mat_alcantarilla = input(
            "Ingrese el material de la alcantarilla: ").strip().lower()

        if mat_alcantarilla in materiales_manning:
            coef_manning = materiales_manning[mat_alcantarilla]
            break
        else:
            print("Error: Seleccione una opción válida.")

    # Cargar datos de precipitaciones
    csv_ruta = os.path.join(os.getcwd(), "data", "csv", "history.csv")
    df = load_data(csv_ruta)

    if df is not None:
        # Calcular el caudal
        df = calculate_flow(df, coef_escorrentia,
                            area_captacion, tiempo_concentracion)

        # Calcular el diámetro de la alcantarilla
        df = calculate_diameter(df, coef_manning, pendiente)

        # Guardar resultados en CSV
        ruta_salida = os.path.join(
            os.getcwd(), "data", "csv", "estimaciones_diametro.csv")
        save_results(df, ruta_salida)

        # Generar gráficos
        generate_plots(df)

        # Extra: Predicción de precipitaciones futuras
        try:
            months_to_predict = 24
            predictions = predict_precipitation(df, months_to_predict)
            print(
                f"Predicciones de precipitación para los próximos {months_to_predict} meses:")
            print(predictions)
        except Exception as e:
            print(f"Error al predecir precipitaciones: {e}")


if __name__ == "__main__":
    main()

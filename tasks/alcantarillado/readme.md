# Estimación de Alcantarillas con el Coeficiente de Manning

## **Objetivo**

Este script en Python estima el diámetro necesario de una alcantarilla para manejar el flujo de agua de lluvia, basado en registros históricos de precipitación mensual y el coeficiente de Manning.

---

## **Requisitos**

### **1. Librerías necesarias**

Es recomendable usar la siguientes librerias para resolver el problema:

```bash
pip install numpy pandas matplotlib
```

---

### **2. Datos a utilizar**

Para obtener los registros históricos de precipitación mensual, utilizar el archivo CSV en `data/csv/history.csv`. 

El usuario debe proporcionar:

- La pendiente del terreno en m/m (validar que este valor sea positivo (0<p<1).
- Tiempo de concentración de  la lluvia en horas (validar que este valor sea mayor que cero).
- Area de captación de la lluvia en hectáreas (validar que este valor sea mayor que cero y menor que 1000).
- Coeficiente de escorrentía de la lluvia (validar que este valor sea mayor que cero y menor que 1).
El usuario debera elegir de la siguiente lista de opciones (Pavimento, Tierra)

| Material              | Coeficiente de escorrentía (C) |
| --------------------- | -------------------------- |
| Pavimento             | 0.6                      |
| Tierra                | 0.3                      |


- Selección del material de la alcantarilla (mostrar una lista de opciones y validar que el usuario seleccione uno de ellos de la siguiente lista).


| Material              | Coeficiente de Manning (n) |
| --------------------- | -------------------------- |
| Concreto liso         | 0.012                      |
| Concreto rugoso       | 0.015                      |
| PVC                   | 0.009                      |
| Acero corrugado       | 0.024                      |
| Polietileno HDPE      | 0.012                      |
| Ladrillo              | 0.017                      |
| Hormigón armado       | 0.013                      |
| Canal de tierra       | 0.025                      |
| Canal de roca         | 0.035                      |
| Mampostería de piedra | 0.030                      |

---

### **4. Cálculos Requeridos**

#### **Cálculo del caudal (Q) usando el Método Racional:**

$$
Q = C \times I \times A
$$

Donde:

- \(Q\) = caudal (m³/s)
- \(C\) = coeficiente de escorrentía (0.6 para pavimento, 0.3 para tierra)
- \(I\) = intensidad de lluvia ( m/s)
- \(A\) = área de captación (m²) (factor de conversión: 1 ha = 10,000 m² )

La intensidad de lluvia \(I\) se calcula como:

$$
I = \frac{P}{T_c}
$$

Donde:

- \(P\) = precipitación diaria promedio (metros)
- \(T_c\) = tiempo de concentración (segundos)

#### **Cálculo del diámetro de la alcantarilla usando la ecuación de Manning:**

$$
Q = \frac{1}{n} A (R)^{2/3} p^{1/2}
$$

Donde:

- \(Q\) = caudal (m³/s)
- \(n\) = coeficiente de Manning
- \(p\) = Pendiente del terreno (m/m) (adimencional)
- \(R\) = Radio hidraulico de la alcantarilla (m)
- \(A\) = área equivalente (m²) = $(pi \times R^2)$

Donde el diámetro \(D\) para una alcantarilla circular se se obtiene de la ecuación:

$$
R = \frac{D}{4}
$$

Siendo \(D\) el diámetro de la alcantarilla y \(R\) el radio hidraulico .

Finalmente, el diámetro mínimo recomendado para cada día se calcula de manera numérica utilizando sympy (https://docs.sympy.org/latest/index.html). o cualquier otra librería de cálculo numérico.


### **5. Salida de Datos**

- Usar matplotlib para generar una gráfica con la relación entre precipitación y diámetro de la alcantarilla.
- Obtener el mes en el periodo 2019-2023 en el cual se necesitaba la alcantarilla mas pequeña.
- Generar un archivo CSV con las estimaciones mensuales de diámetro de la alcantarilla.


### **6. Extras Opcionales**

✅ Manejo de errores para archivos de entrada mal formateados.\
✅ Utilizar liberias de regresion temporal para calcular las precipitaciones mensuales hasta marzo de 2025 y estimar el diámetro una alcantarilla para pavimento suponiendo una pendiente de 0.01 m/m, un coeficiente de Manning de 0.012, una área de captación de 1 ha y un tiempo de concentración de 1 hora.\

---

### **7. Entega del Programa**

1. Crea una branch feature/alcantarillada
1. El script debera ser guardado en tasks/alcantarillada/run.py
2. Incluir los requirements en tasks/alcantarillada/requirements.txt




# VR Weather Analysis

## Descripción

Analisis de los datos meteorológicos de Villa Rica para posibles aplicaciones en ingeniería civil

## Motivación

### Variables solares
- **heliofania_media**: Dimensionamiento de sistemas de energía solar, diseño de iluminación natural en edificios, análisis de fatiga de materiales expuestos al sol.
- **heliofania_total**: Cálculos de rendimiento energético en paneles solares, estudio de sombreamiento en desarrollos urbanos, diseño de protecciones solares en fachadas.

### Variables de presión atmosférica
- **pres_atm_nivel_mar**: Cálculo de cargas de viento en estructuras altas, diseño de sistemas de ventilación natural.
- **pres_atm_nivel_estacion**: Análisis de comportamiento de materiales sellantes, calibración de equipos de medición in situ.

### Variables de precipitación
- **precip_max**: Diseño de sistemas de drenaje urbano, dimensionamiento de alcantarillado pluvial, cálculo de vertederos.
- **precip_total**: Cálculo de balance hídrico para embalses, diseño de canales y sistemas de captación.

### Variables de viento
- **viento_vel_med**: Diseño estructural para resistencia a cargas eólicas continuas, estudios de ventilación urbana.
- **viento_vel_max**: Dimensionamiento de estructuras ante eventos extremos, ubicación de aerogeneradores, análisis de dispersión de contaminantes.

### Variables de humedad
- **humedad_relativa_media**: Selección de materiales resistentes a la corrosión, diseño de sistemas de climatización, prevención de patologías en edificaciones.

### Variables de temperatura
- **temp_max**: Cálculo de dilataciones térmicas en puentes y vías férreas, diseño de cubiertas.
- **temp_min**: Diseño de sistemas de calefacción, protección de tuberías contra congelamiento.
- **media_temp_max**: Diseño de sistemas de climatización, análisis de confort térmico.
- **media_temp_min**: Cálculo de demanda energética en edificios, dimensionamiento de aislamiento térmico.
- **temp_media**: Selección de materiales según resistencia térmica, estimación de consumos energéticos.
- **dias_menos_0**: Diseño de infraestructura resistente a heladas, planificación de hormigonado en condiciones extremas.
- **dias_entre_0_y_5**: Análisis de ciclos de congelamiento-descongelamiento en pavimentos, protección de sistemas hidráulicos.
- **dias_entre_35_y_40**: Diseño de sistemas de enfriamiento, análisis de comportamiento de asfaltos.
- **dias_superior_40**: Selección de materiales resistentes a altas temperaturas, previsión de dilataciones extremas.
- **temp_rocio**: Prevención de condensaciones en edificios, diseño de sistemas de aislamiento térmico, control de humedades en estructuras subterráneas.


## Unidades de medida

COLUMN NAME | UNITS
------------ | -------------
Heliofania | Hour (h)
Presión atmosférica | Hectopascal (hPa)
Precipitación | Milímetros (mm)
Intensidad del Viento | Kilómetros por hora (km/h)
Humedad Relativa | Porcentaje (%)
Temperatura | Grados Centígrados (°C)   

## Instalación

Para instalar los paquetes necesarios para el proyecto, ejecutar el siguiente comando en la consola:

```bash
pip install -r requirements.txt
```

# Estructura de datos

## data/raw
Datos meterológicos de Villa Rica extraidos de la página oficial de la Dirección General de Meteorología de Paraguay.

Los datos son proveidos en pdf

## data/csv
Datos meteorológicos procesados y organizados en formato csv, distribuidos por meses en el periodo 2019-2023


#### Columnas 
- year_month: mes del año
- heliofania_media: Duracion media del brillo solar
- heliofania_total: Duracion total del brillo solar (suma de todas las duraciones diarias)
- pres_atm_nivel_mar: Presion atmosferica media en el mes medida al nivel del mar
- pres_atm_nivel_estacion: Presion atmosferica media en el mes medida en la estacion meteorologica
- precip_max: Precipitacion maxima alcanzada en el mes
- dia_precip_max: Dia en que se alcanzo la precipitacion maxima
- precip_total: Precipitacion total en el mes
- dias_con_precip: Total de dias con precipitacion
- viento_vel_med: Velocidad media del viento en el mes
- viento_vel_max: Velocidad maxima del viento en el mes
- humedad_relativa_media: Humedad relativa media en el mes
- temp_max: Temperatura maxima alcanzada en el mes
- dia_temp_max: Dia en que se alcanzo la temperatura maxima
- temp_min: Temperatura minima alcanzada en el mes
- dia_temp_min: Dia en que se alcanzo la temperatura minima
- media_temp_max: Media de todas las temperaturas maximas por dia
- media_temp_min: Media de todas las temperaturas minimas por dia
- temp_media: Temperatura media en el mes
- dias_menos_0: Dias en que se produjo menos de 0 grados
- dias_entre_0_y_5: Dias en que se produjo entre 0 y 5 grados
- dias_entre_35_y_40: Dias en que se produjo entre 35 y 40 grados
- dias_superior_40: Dias en que se produjo mayor de 40 grados
- temp_rocio: Temperatura rocio en el mes




## Fuentes

- https://www.meteorologia.gov.py/publicaciones




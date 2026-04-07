# 🚲 Bike Sharing Dataset

## Descripción

Dataset de demanda de alquiler de bicicletas en Washington D.C.
Contiene registros por hora con variables climáticas y temporales
para predecir la cantidad de bicicletas alquiladas.

## Fuente

- Kaggle: https://www.kaggle.com/c/bike-sharing-demand

## Dimensiones

- Train - Filas: 10,886 | Columnas: 12
- Test - Filas: 6,493 | Columnas: 9

## Variables principales

| Variable  | Descripción                                            |
| --------- | ------------------------------------------------------ |
| datetime  | Fecha y hora del registro                              |
| season    | Temporada (1=Primavera, 2=Verano, 3=Otoño, 4=Invierno) |
| weather   | Condición climática                                    |
| temp      | Temperatura en Celsius                                 |
| humidity  | Humedad relativa                                       |
| windspeed | Velocidad del viento                                   |
| count     | Total de bicicletas alquiladas (variable objetivo)     |

## Variables derivadas

- `hour` — Hora del día extraída de datetime
- `day` — Día de la semana
- `month` — Mes del año
- `year` — Año

## Valores nulos

- Dataset sin valores nulos
- Se aplicó KNN Imputer como verificación

## Hallazgos principales

- Mayor demanda en horas pico (8am y 5-6pm)
- Verano y Otoño presentan mayor demanda
- Temperatura correlaciona positivamente con alquileres

## Uso típico

- Regresión supervisada
- Análisis de series temporales
- Predicción de demanda

## Archivos del repositorio

- `bike_sharing.ipynb` — Notebook con exploración y preparación
- `data/train.csv` — Dataset de entrenamiento
- `data/test.csv` — Dataset de prueba

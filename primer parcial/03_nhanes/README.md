# 🏥 NHANES Dataset (2017-2018)

## Descripción

NHANES (National Health and Nutrition Examination Survey) es una encuesta
del CDC que combina entrevistas y exámenes físicos para evaluar la salud
y nutrición de adultos y niños en Estados Unidos.

## Fuente

- Portal oficial CDC: https://www.cdc.gov/nchs/nhanes/index.html
- Edición utilizada: 2017-2018

## Módulos utilizados

| Archivo    | Módulo         | Descripción                |
| ---------- | -------------- | -------------------------- |
| DEMO_J.XPT | Demographics   | Edad, sexo, raza, ingresos |
| BMX_J.XPT  | Body Measures  | Peso, talla, IMC           |
| BPX_J.XPT  | Blood Pressure | Presión arterial           |
| DIQ_J.XPT  | Diabetes       | Diagnóstico de diabetes    |

## Dimensiones (dataset unificado)

- Filas: 11,933
- Columnas: ~65

## Valores nulos

- Se eliminaron columnas constantes
- Se imputaron variables numéricas con **KNN Imputer (k=5)**
- Se imputaron variables categóricas con la **moda**
- Resultado final: 0 valores nulos

## Hallazgos principales

- Se analizó distribución de IMC de la población
- Se analizó distribución de edades
- Se exploró relación entre presión arterial sistólica e IMC

## Uso típico

- Predicción de enfermedades crónicas
- Análisis de salud poblacional
- Clasificación de riesgo cardiovascular

## Archivos del repositorio

- `nhanes.ipynb` — Notebook con exploración y preparación
- `data/` — Archivos originales del dataset

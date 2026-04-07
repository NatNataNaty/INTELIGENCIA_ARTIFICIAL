# 🦘 Statlog Australian Credit Dataset

## Descripción

Dataset de solicitudes de crédito con atributos mixtos (numéricos
y categóricos), originado en Australia. El objetivo es predecir
la aprobación o rechazo de una solicitud.

## Fuente

- UCI Machine Learning Repository:
  https://archive.ics.uci.edu/ml/datasets/statlog+(australian+credit+approval)

## Dimensiones

- Filas: 690
- Columnas: 15

## Variable objetivo

- `A15`: decisión (0 = rechazado, 1 = aprobado)

## Tipos de variables

- Todas numéricas (algunas actúan como categóricas binarias)

## Valores nulos

- Este dataset NO tiene valores nulos
- No se requirió imputación

## Uso típico

- Clasificación binaria
- Evaluación de riesgo crediticio
- Comparación con Credit Approval Dataset

## Archivos

- `australian_credit.ipynb` — Notebook con exploración
- `data/australian.dat` — Dataset principal

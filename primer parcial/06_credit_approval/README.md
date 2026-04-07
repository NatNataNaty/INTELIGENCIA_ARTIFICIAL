# 💳 Credit Approval Dataset

## Descripción

Dataset de solicitudes de tarjetas de crédito con atributos
anonimizados por privacidad. El objetivo es predecir si una
solicitud fue aprobada o rechazada.

## Fuente

- UCI Machine Learning Repository:
  https://archive.ics.uci.edu/ml/datasets/credit+approval

## Dimensiones

- Filas: 690
- Columnas: 16

## Variable objetivo

- `A16`: decisión de crédito (+ aprobado / - rechazado)

## Tipos de variables

- Numéricas: 6 (A2, A3, A8, A11, A14, A15)
- Categóricas: 10 (A1, A4, A5, A6, A7, A9, A10, A12, A13, A16)

## Valores nulos

- Presentes en: A1, A2, A4, A5, A6, A7, A14
- Imputación numéricas: KNN Imputer (k=5)
- Imputación categóricas: moda
- Resultado: 0 nulos

## Uso típico

- Clasificación binaria
- Evaluación de riesgo crediticio
- Análisis de decisiones financieras

## Archivos

- `credit_approval.ipynb` — Notebook con exploración
- `data/crx.data` — Dataset principal
- `data/crx.names` — Descripción de variables

# 🎗️ Breast Cancer Wisconsin (Diagnostic) Dataset

## Descripción

Dataset con características extraídas de imágenes digitalizadas
de biopsias de masa mamaria. El objetivo es clasificar tumores
como malignos (M) o benignos (B).

## Fuente

- UCI Machine Learning Repository:
  https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(diagnostic)

## Dimensiones

- Filas: 569
- Columnas: 31 (30 features + 1 target)

## Variable objetivo

- `diagnosis`: M = Maligno, B = Benigno

## Tipos de variables

- Numéricas: 30 (10 características × 3 estadísticos: mean, se, worst)
- Categórica: diagnosis (target)

## Valores nulos

- Este dataset NO tiene valores nulos

## Hallazgos principales

- Radio, perímetro y área tienen alta correlación entre sí
- Variables de concavidad son las más discriminativas
- Dataset levemente desbalanceado: ~63% benigno, ~37% maligno

## Uso típico

- Clasificación binaria
- Diagnóstico médico asistido por ML
- Selección de características

## Archivos

- `breast_cancer.ipynb` — Notebook con exploración
- `data/wdbc.data` — Dataset principal
- `data/wdbc.names` — Descripción de variables

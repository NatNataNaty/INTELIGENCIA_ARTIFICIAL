# 🧠 Meningitis Dataset

## Descripción

Dataset clínico con características de pacientes para
clasificar el tipo de meningitis o predecir su diagnóstico.

## Fuente

- Kaggle: https://www.kaggle.com/datasets/joebeachcapital/meningitis

## Dimensiones

- Filas: según dataset descargado
- Columnas: según dataset descargado

## Variable objetivo

- Columna de diagnóstico (última columna del dataset)

## Tipos de variables

- Mezcla de variables numéricas y categóricas clínicas

## Valores nulos

- Se verificaron al cargar el dataset
- Imputación numérica: KNN Imputer (k=5)
- Imputación categórica: moda

## Uso típico

- Clasificación multiclase
- Diagnóstico médico asistido por ML
- Análisis de datos clínicos

## Archivos

- `meningitis.ipynb` — Notebook con exploración
- `data/` — Dataset descargado de Kaggle

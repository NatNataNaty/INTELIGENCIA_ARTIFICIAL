# 🏠 Ames Housing Dataset

## Descripción

Dataset sobre precios de venta de casas en Ames, Iowa (EE.UU.).
Contiene características detalladas de propiedades residenciales
para predecir su precio de venta.

## Fuente

- Kaggle: https://www.kaggle.com/datasets/marcopale/housing

## Dimensiones

- Filas: 2930
- Columnas: 82

## Variable objetivo

- `SalePrice`: precio de venta de la vivienda en USD

## Tipos de variables

- Numéricas: 39
- Categóricas: 44

## Valores nulos

- Se encontraron columnas con valores nulos
- Se imputaron variables numéricas con **KNN Imputer (k=5)**
- Se imputaron variables categóricas con la **moda**
- Resultado final: 0 valores nulos

## Uso típico

- Regresión supervisada
- Feature engineering
- Análisis de precios inmobiliarios

## Archivos

- `ames_housing.ipynb` — Notebook con exploración y preparación
- `data/AmesHousing.xls` — Dataset original

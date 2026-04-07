# 💰 Adult Census Income Dataset

## Descripción

Dataset del censo de EE.UU. que contiene información demográfica
y laboral de personas para predecir si su ingreso anual supera
o no los $50,000 USD.

## Fuente

- UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/adult

## Dimensiones

- Train - Filas: 32,561 | Columnas: 15
- Test - Filas: 16,281 | Columnas: 15

## Variables principales

| Variable       | Tipo       | Descripción                      |
| -------------- | ---------- | -------------------------------- |
| age            | Numérica   | Edad                             |
| workclass      | Categórica | Tipo de empleo                   |
| education      | Categórica | Nivel educativo                  |
| occupation     | Categórica | Ocupación                        |
| race           | Categórica | Raza                             |
| sex            | Categórica | Sexo                             |
| hours_per_week | Numérica   | Horas trabajadas por semana      |
| income         | Categórica | Variable objetivo (<=50K / >50K) |

## Valores nulos

- Los nulos estaban codificados como '?'
- Se reemplazaron con NaN
- Se imputaron numéricas con **KNN Imputer (k=5)**
- Se imputaron categóricas con la **moda**
- Resultado final: 0 valores nulos

## Hallazgos principales

- Dataset desbalanceado: mayoría gana <=50K
- Mayor educación correlaciona con mayores ingresos
- Personas de mayor edad tienden a ganar más

## Uso típico

- Clasificación binaria
- Análisis de equidad y sesgo
- Predicción de ingresos

## Archivos del repositorio

- `adult_census.ipynb` — No

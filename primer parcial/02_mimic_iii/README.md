# ⚕️ MIMIC-III Dataset

## Descripción

MIMIC-III (Medical Information Mart for Intensive Care) es una base de datos
médica de acceso libre que contiene información de más de 40,000 pacientes
ingresados en unidades de cuidados intensivos (UCI) del Beth Israel Deaconess
Medical Center entre 2001 y 2012.

## Fuente

- PhysioNet: https://physionet.org/content/mimiciii-demo/1.4/
- Descripción: https://www.innovatiana.com/en/datasets/mimic-iii

## Archivos utilizados

| Archivo              | Descripción                     |
| -------------------- | ------------------------------- |
| ADMISSIONS.csv.gz    | Ingresos hospitalarios          |
| PATIENTS.csv.gz      | Datos demográficos de pacientes |
| DIAGNOSES_ICD.csv.gz | Diagnósticos en códigos ICD-9   |
| LABEVENTS.csv.gz     | Resultados de laboratorio       |
| PRESCRIPTIONS.csv.gz | Medicamentos prescritos         |

## Valores nulos

- Se imputaron variables numéricas con **KNN Imputer (k=5)**
- Se imputaron variables categóricas con la **moda**
- Resultado final: 0 valores nulos

## Hallazgos principales

- Tipos de ingreso: EMERGENCY, ELECTIVE, URGENT, NEWBORN
- Se analizó mortalidad hospitalaria
- Se identificaron los 10 diagnósticos ICD-9 más frecuentes

## Uso típico

- Predicción de mortalidad
- Análisis de estancia hospitalaria
- Clasificación de diagnósticos
- Procesamiento de datos médicos con missings

## Archivos del repositorio

- `mimic_iii.ipynb` — Notebook con exploración y preparación
- `data/` — Archivos originales del dataset

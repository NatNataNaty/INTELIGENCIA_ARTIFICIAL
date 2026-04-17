## Bloque — Texto para README.md

````markdown
# Clasificación Multiclase de Riesgo Cardíaco con PyTorch — NHANES 2021-2023

## Descripción

Este proyecto implementa un modelo de clasificación multiclase usando una red neuronal
MLP (Multilayer Perceptron) con PyTorch para predecir el nivel de riesgo cardíaco
de pacientes a partir de datos reales de la encuesta NHANES (National Health and
Nutrition Examination Survey) del CDC, ciclo 2021-2023.

A diferencia de enfoques que construyen la variable objetivo mediante reglas heurísticas,
este proyecto utiliza diagnósticos médicos reales registrados por el CDC como etiqueta
de clasificación.

---

## Variable Objetivo

La variable objetivo `evento_cardiaco` se construye a partir de diagnósticos
médicos reales del cuestionario MCQ de NHANES:

| Clase | Descripción                                    | Columnas CDC     |
| ----- | ---------------------------------------------- | ---------------- |
| 0     | Sin evento cardíaco registrado                 | —                |
| 1     | Riesgo moderado: angina / enfermedad coronaria | MCQ160C, MCQ160D |
| 2     | Riesgo alto: infarto o insuficiencia cardíaca  | MCQ160E, MCQ160B |

> La distribución de clases refleja la realidad clínica: ~85% sin evento,
> ~8% angina, ~7% infarto/insuficiencia. Este desbalance es inherente
> al dataset y no un error del preprocesamiento.

---

## Fuentes de Datos

Los datos provienen de 13 archivos XPT descargados directamente del CDC:

| Archivo     | Contenido                               |
| ----------- | --------------------------------------- |
| DEMO_L.xpt  | Edad, sexo, educación                   |
| BMX_L.xpt   | IMC, circunferencia de cintura          |
| GHB_L.xpt   | Hemoglobina glucosilada (HbA1c)         |
| HDL_L.xpt   | Colesterol HDL                          |
| TCHOL_L.xpt | Colesterol total                        |
| BPXO_L.xpt  | Presión arterial sistólica              |
| ALQ_L.xpt   | Consumo de alcohol                      |
| SLQ_L.xpt   | Horas de sueño                          |
| BPQ_L.xpt   | Diagnóstico de hipertensión             |
| SMQ_L.xpt   | Hábito de fumar                         |
| PAQ_L.xpt   | Actividad física                        |
| DIQ_L.xpt   | Diagnóstico de diabetes                 |
| MCQ_L.xpt   | Condiciones médicas (variable objetivo) |

---

## Features del Modelo

```python
features = [
    'edad', 'sexo', 'educacion',
    'bmi', 'cintura',
    'hba1c', 'hdl', 'col_total', 'presion_sistolica',
    'alcohol', 'sueno',
    'hipertension', 'fumador', 'diabetes', 'act_fisica'
]
```
````

---

## Preprocesamiento

- Unión de todos los datasets por clave `SEQN`
- Limpieza de códigos especiales NHANES (7, 9, 77, 99, 777, 999...)
- Consolidación de variables de alcohol en una sola métrica continua
- Conversión de variables binarias (hipertensión, fumador, diabetes): 1=Sí, 0=No
- Imputación de valores faltantes con `KNNImputer(n_neighbors=5)`
- Normalización min-max al rango [0, 1]
- Split 70% train / 15% validación / 15% test

---

## Arquitectura del Modelo

```
Input(15) → Linear(128) → BatchNorm → ReLU → Dropout(p)
          → Linear(64)  → BatchNorm → ReLU → Dropout(p)
          → Linear(3)   → Softmax
```

- Optimizador: Adam
- Loss: CrossEntropyLoss
- Activación: ReLU + Softmax en salida

---

## Experimentos de Regularización

Se comparan 4 configuraciones siguiendo la metodología del notebook
de referencia:

| Experimento | Configuración  | Técnica             |
| ----------- | -------------- | ------------------- |
| 1           | Baseline       | Sin regularización  |
| 2           | L2             | weight_decay=0.01   |
| 3           | Early Stopping | patience=20         |
| 4           | Dropout + ES   | p=0.3 + patience=30 |

Para cada experimento se reporta accuracy en train, validación y test,
así como la brecha de generalización (Train - Test).

---

## Métricas Reportadas

- Accuracy global
- F1-Score macro y weighted
- ROC-AUC multiclase (one-vs-rest)
- Reporte completo por clase (precision, recall, F1)
- Matriz de confusión
- Curvas ROC por clase
- Distribución real vs predicha en test

---

## Limitaciones

- **Desbalance de clases**: la Clase 0 representa ~85% del dataset,
  lo cual puede sesgar el modelo hacia predecir siempre "sin evento".
  Se recomienda evaluar principalmente con F1 macro y ROC-AUC en lugar
  de accuracy.
- **Corte transversal**: NHANES es una encuesta puntual, no un
  seguimiento longitudinal, por lo que el modelo predice condiciones
  actuales y no riesgo futuro.
- **Población representada**: los resultados son válidos para la
  población adulta de Estados Unidos representada en NHANES.

---

## Requisitos

```
torch
numpy
pandas
scikit-learn
matplotlib
```

---

## Estructura del Proyecto

```
NHANES/
├── DEMO_L.xpt
├── BMX_L.xpt
├── GHB_L.xpt
├── HDL_L.xpt
├── TCHOL_L.xpt
├── BPXO_L.xpt
├── ALQ_L.xpt
├── SLQ_L.xpt
├── BPQ_L.xpt
├── SMQ_L.xpt
├── PAQ_L.xpt
├── DIQ_L.xpt
├── MCQ_L.xpt
└── notebook.ipynb
```

---

## Referencias

- [NHANES 2021-2023 — CDC](https://www.cdc.gov/nchs/nhanes)
- [MCQ Questionnaire Codebook](https://wwwn.cdc.gov/Nchs/Nhanes/2021-2023/MCQ_L.htm)
- [PyTorch Documentation](https://pytorch.org/docs)
- [scikit-learn: KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html)

```

```

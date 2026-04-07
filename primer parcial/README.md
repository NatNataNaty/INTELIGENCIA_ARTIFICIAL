# 📊 Primer Parcial 2026 — Exploración de Datasets

Repositorio con la exploración, limpieza y análisis descriptivo de 9 datasets
seleccionados para el primer parcial. Cada dataset fue trabajado en un Jupyter
Notebook individual con las siguientes etapas: carga de datos, tipos de variables,
valores nulos, imputación, estadísticas descriptivas y visualizaciones.

---

## 🗂️ Estructura del Repositorio

primer-parcial-2026/
├── README.md
├── 01_ames_housing/
├── 02_mimic_iii/
├── 03_nhanes/
├── 04_bike_sharing/
├── 05_adult_census/
├── 06_credit_approval/
├── 07_australian_credit/
├── 08_breast_cancer/
└── 09_meningitis/

---

## 📋 Resumen de los 9 Datasets

| #   | Dataset                 | Filas             | Columnas    | Tipo de tarea | Fuente    |
| --- | ----------------------- | ----------------- | ----------- | ------------- | --------- |
| 1   | Ames Housing            | 1,460             | 81          | Regresión     | Kaggle    |
| 2   | MIMIC-III               | 40,000+ pacientes | 26 tablas   | Múltiple      | PhysioNet |
| 3   | NHANES                  | ~5,000/año        | 1,000+ vars | Múltiple      | CDC       |
| 4   | Bike Sharing            | 17,379 (hora)     | 17          | Regresión     | UCI       |
| 5   | Adult Census Income     | 48,842            | 15          | Clasificación | UCI       |
| 6   | Credit Approval         | 690               | 16          | Clasificación | UCI       |
| 7   | Australian Credit       | 690               | 15          | Clasificación | UCI       |
| 8   | Breast Cancer Wisconsin | 569               | 32          | Clasificación | UCI       |
| 9   | Meningitis              | Variable          | Variable    | Clasificación | Kaggle    |

---

## 📁 Descripción Detallada de Cada Dataset

---

### 🏠 1. Ames Housing Dataset

**Descripción:**
Dataset sobre la venta de propiedades residenciales en la ciudad de Ames,
Iowa, Estados Unidos, entre los años 2006 y 2010. Fue compilado por Dean De Cock
en 2011 como una alternativa moderna y más completa al clásico Boston Housing
Dataset. Es uno de los datasets más utilizados en competencias de machine learning
para el problema de predicción de precios de vivienda.

**Origen:** Creado por Dean De Cock (2011). Disponible en Kaggle como parte
de la competencia "House Prices: Advanced Regression Techniques".

- Fuente: https://www.kaggle.com/datasets/marcopale/housing

**Dimensiones:**

- Filas: 1,460 (train) + 1,459 (test) = 2,919 total
- Columnas: 81 (79 features + ID + SalePrice)

**Variable objetivo:** `SalePrice` — precio de venta en dólares

**Tipos de variables:**

- 23 variables nominales (categóricas sin orden): tipo de zona, estilo de techo, etc.
- 23 variables ordinales (categóricas con orden): calidad general, condición, etc.
- 14 variables discretas: número de habitaciones, baños, garajes, etc.
- 20 variables continuas: áreas en pies cuadrados, precio, etc.

**Variables clave:**

- `GrLivArea`: área habitable sobre el suelo (pies²)
- `OverallQual`: calidad general de materiales y acabados (1–10)
- `YearBuilt`: año de construcción
- `TotalBsmtSF`: área total del sótano (pies²)
- `GarageCars`: capacidad del garaje en número de autos
- `SalePrice`: precio de venta (target)

**Valores nulos:** Presente en múltiples columnas. La columna `PoolQC`
tiene hasta 99.5% de nulos (la mayoría de casas no tiene piscina).
Columnas como `Alley`, `Fence`, `MiscFeature` también tienen alto porcentaje de nulos.

**Características especiales:**

- Alta cantidad de features (79) que requieren feature engineering
- Distribución de SalePrice con cola derecha larga → se recomienda transformación logarítmica
- Excelente para practicar selección de variables y modelos de regresión avanzados

**Usos típicos:** Regresión, feature engineering, análisis de precios inmobiliarios,
competencias de Kaggle.

---

### 🏥 2. MIMIC-III Clinical Database

**Descripción:**
MIMIC-III (Medical Information Mart for Intensive Care) es una base de datos
clínica de libre acceso que contiene información desidentificada de más de 40,000
pacientes que estuvieron internados en las unidades de cuidados intensivos (UCI)
del Beth Israel Deaconess Medical Center en Boston, Massachusetts, entre los
años 2001 y 2012. Es uno de los datasets de salud más importantes y utilizados
en investigación clínica e inteligencia artificial médica.

**Origen:** Creado por Alistair Johnson, Tom Pollard y otros investigadores del MIT
y Beth Israel Deaconess Medical Center. Publicado en PhysioNet.

- Fuente: https://physionet.org/content/mimiciii/1.4/
- Citación: Johnson et al. (2016). MIMIC-III, a freely accessible critical care database.
  Scientific Data.

**Acceso especial requerido:**
Para acceder al dataset completo se deben completar dos pasos obligatorios:

1. Completar el curso de protección de participantes humanos en investigación
   (curso CITI con módulo HIPAA)
2. Firmar un acuerdo de uso de datos (Data Use Agreement) en PhysioNet
   La aprobación tarda al menos una semana.

**Dimensiones:**

- Pacientes: más de 40,000
- Admisiones UCI: más de 60,000
- Tablas: 26 tablas relacionales en formato CSV
- Período: 2001–2012

**Estructura (tablas principales):**
| Tabla | Contenido |
|-------|-----------|
| PATIENTS | Datos demográficos de pacientes |
| ADMISSIONS | Registros de admisiones hospitalarias |
| ICUSTAYS | Estadías en UCI |
| CHARTEVENTS | Signos vitales y eventos registrados |
| LABEVENTS | Resultados de laboratorio |
| PRESCRIPTIONS | Medicamentos recetados |
| DIAGNOSES_ICD | Diagnósticos en código ICD-9 |
| NOTEEVENTS | Notas clínicas de médicos y enfermeras |

**Variables clave:**

- `subject_id`: identificador único del paciente
- `hadm_id`: identificador de admisión hospitalaria
- `icustay_id`: identificador de estadía en UCI
- `intime` / `outtime`: tiempos de entrada y salida de UCI
- `los`: duración de estadía (length of stay)
- Signos vitales: frecuencia cardíaca, presión arterial, temperatura, SpO2
- Resultados de laboratorio: glucosa, creatinina, hemoglobina, etc.

**Características especiales:**

- Datos completamente desidentificados (cumple HIPAA)
- Alta resolución temporal: datos cada ~1 hora a la cabecera del paciente
- Incluye notas clínicas en texto libre (útil para NLP)
- Las fechas de nacimiento de pacientes mayores de 89 años fueron modificadas
  por regulaciones de privacidad (pueden aparecer con edades >300 años)
- Base de datos relacional: requiere conocimiento de SQL o pandas merge

**Usos típicos:** Predicción de mortalidad, predicción de readmisión, análisis
de sepsis, NLP en textos clínicos, epidemiología, investigación clínica.

---

### 📊 3. NHANES (National Health and Nutrition Examination Survey)

**Descripción:**
La Encuesta Nacional de Examen de Salud y Nutrición (NHANES) es un programa
de estudios diseñado para evaluar el estado de salud y nutrición de adultos y
niños en Estados Unidos. Es administrado por el Centro Nacional de Estadísticas
de Salud (NCHS) dependiente del CDC (Centers for Disease Control and Prevention).
Su característica única es que combina entrevistas en el hogar con exámenes
físicos realizados en centros móviles especializados (Mobile Examination Centers).

**Origen:** Iniciado en 1960 como encuesta periódica. A partir de 1999 se
convirtió en encuesta continua con datos publicados en ciclos de 2 años.

- Fuente: https://www.cdc.gov/nchs/nhanes/index.html

**Dimensiones:**

- Aproximadamente 5,000 personas examinadas por año
- Datos organizados en múltiples módulos y archivos
- Cubre todos los grupos etarios de la población civil no institucionalizada

**Estructura (módulos principales):**
| Módulo | Contenido |
|--------|-----------|
| Demographics | Edad, sexo, raza, educación, ingresos, pesos de encuesta |
| Examination | Presión arterial, medidas corporales, audiometría, salud oral |
| Laboratory | Colesterol, glucosa, metales pesados, hepatitis, HIV, triglicéridos |
| Questionnaire | Alcohol, diabetes, actividad física, salud mental, nutrición |
| Dietary | Ingesta alimentaria de 24 horas, suplementos |

**Variables clave:**

- `SEQN`: identificador único del participante (clave primaria para unir archivos)
- `RIDAGEYR`: edad en años
- `RIAGENDR`: sexo (1=masculino, 2=femenino)
- `RIDRETH3`: raza/etnia
- `BMXBMI`: índice de masa corporal (IMC/BMI)
- `BPXSY1`: presión arterial sistólica
- `LBXTC`: colesterol total
- `LBDGLUSI`: glucosa en ayunas

**Características especiales:**

- Datos disponibles en formato SAS Transport (.xpt), requieren conversión a CSV
- Diseño muestral complejo con sobremuestreo de grupos minoritarios
  (hispanos, afroamericanos, asiáticos, adultos mayores)
- Para análisis estadísticamente válidos se deben usar los pesos de encuesta
  incluidos en el módulo de demografía
- Los archivos de cada ciclo deben unirse mediante el campo `SEQN`
- Cada ciclo de 2 años tiene su propia documentación y codebook

**Usos típicos:** Epidemiología poblacional, análisis de prevalencia de
enfermedades crónicas, estudios nutricionales, análisis de desigualdades
en salud, predicción de diabetes y obesidad.

---

### 🚲 4. Bike Sharing Dataset

**Descripción:**
Dataset que registra el conteo de alquileres de bicicletas por hora y por día
en el sistema Capital Bikeshare de Washington D.C., EE.UU., durante los años
2011 y 2012. Fue creado por Hadi Fanaee-T de la Universidad de Porto. Es un
excelente ejemplo de datos de series temporales con fuerte influencia de
factores climáticos y temporales.

**Origen:** Hadi Fanaee-T y João Gama (2013). UCI Machine Learning Repository.

- Fuente: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
- Datos originales: http://capitalbikeshare.com/system-data

**Dimensiones:**

- `hour.csv`: 17,379 filas × 17 columnas (datos por hora)
- `day.csv`: 731 filas × 16 columnas (datos diarios)

**Variable objetivo:** `cnt` — total de bicicletas alquiladas (casual + registered)

**Variables principales:**
| Variable | Tipo | Descripción |
|----------|------|-------------|
| instant | Numérica | Índice del registro |
| dteday | Fecha | Fecha |
| season | Categórica | Temporada (1=primavera, 2=verano, 3=otoño, 4=invierno) |
| yr | Categórica | Año (0=2011, 1=2012) |
| mnth | Numérica | Mes (1–12) |
| hr | Numérica | Hora (0–23), solo en hour.csv |
| holiday | Binaria | Si es feriado (0/1) |
| weekday | Numérica | Día de la semana (0–6) |
| workingday | Binaria | Si es día laboral (0/1) |
| weathersit | Categórica | Condición climática (1=despejado, 2=nublado, 3=lluvia leve, 4=lluvia fuerte) |
| temp | Numérica | Temperatura normalizada (0–1) |
| atemp | Numérica | Sensación térmica normalizada (0–1) |
| hum | Numérica | Humedad normalizada (0–1) |
| windspeed | Numérica | Velocidad del viento normalizada (0–1) |
| casual | Numérica | Usuarios ocasionales |
| registered | Numérica | Usuarios registrados |
| cnt | Numérica | Total de alquileres (TARGET) |

**Valores nulos:** No tiene valores nulos.

**Características especiales:**

- `casual` + `registered` = `cnt` (por lo que casual y registered deben
  eliminarse al modelar cnt para evitar data leakage)
- Los alquileres pican fuertemente en horas pico (7–9 AM y 5–7 PM)
- La temperatura es la variable con mayor correlación positiva con cnt (~0.63)
- Datos de serie temporal: se recomienda no usar split aleatorio al modelar

**Usos típicos:** Regresión, análisis de series temporales, análisis de
patrones de movilidad urbana, predicción de demanda.

---

### 💰 5. Adult Census Income Dataset

**Descripción:**
También conocido como "Adult" o "Census Income", este dataset fue extraído
por Barry Becker y Ronny Kohavi de la base de datos del Censo de EE.UU. de 1994. El objetivo es predecir si una persona tiene un ingreso anual superior
o inferior a $50,000 USD basándose en características demográficas y laborales.
Es uno de los datasets de clasificación más clásicos y utilizados en machine learning.

**Origen:** Barry Becker y Ronny Kohavi (1996). UCI Machine Learning Repository.
Los datos provienen del Census Bureau de EE.UU. de 1994.

- Fuente: https://archive.ics.uci.edu/dataset/2/adult
- Condición de extracción: AAGE>16, AGI>100, AFNLWGT>1, HRSWK>0

**Dimensiones:**

- Train (`adult.data`): 32,561 filas × 15 columnas
- Test (`adult.test`): 16,281 filas × 15 columnas
- Total: 48,842 registros

**Variable objetivo:** `income` — <=50K o >50K

**Variables principales:**
| Variable | Tipo | Descripción |
|----------|------|-------------|
| age | Numérica | Edad |
| workclass | Categórica | Tipo de empleo (Private, Gov, Self-emp...) |
| fnlwgt | Numérica | Peso final del censo (representatividad) |
| education | Categórica | Nivel educativo |
| education_num | Numérica | Nivel educativo en número |
| marital_status | Categórica | Estado civil |
| occupation | Categórica | Ocupación laboral |
| relationship | Categórica | Relación familiar |
| race | Categórica | Raza |
| sex | Categórica | Sexo |
| capital_gain | Numérica | Ganancia de capital |
| capital_loss | Numérica | Pérdida de capital |
| hours_per_week | Numérica | Horas trabajadas por semana |
| native_country | Categórica | País de origen |
| income | Categórica | Nivel de ingreso (TARGET) |

**Valores nulos:**

- Los valores nulos están codificados como '?' en el archivo original
- Columnas afectadas: `workclass`, `occupation`, `native_country`
- Se reemplazan con NaN y se imputan (KNN para numéricas, moda para categóricas)

**Características especiales:**

- Dataset desbalanceado: ~75% gana <=50K, ~25% gana >50K
- Mayor nivel educativo correlaciona fuertemente con ingresos más altos
- La variable `fnlwgt` representa cuántas personas del censo representa
  ese registro (peso muestral) — generalmente se descarta en modelos
- Contiene 42 países distintos en `native_country`
- Importante para estudios de equidad y sesgo en ML

**Usos típicos:** Clasificación binaria, análisis de equidad y sesgo,
predicción de ingresos, análisis socioeconómico.

---

### 💳 6. Credit Approval Dataset

**Descripción:**
Dataset de solicitudes de tarjetas de crédito, recopilado por J.R. Quinlan
en 1987. Todos los nombres de atributos y valores han sido cambiados por
símbolos sin significado para proteger la confidencialidad de los datos.
La fuente original se cree que proviene de solicitudes de crédito japonesas.
Es uno de los datasets benchmark clásicos para algoritmos de clasificación.

**Origen:** J.R. Quinlan (1987). UCI Machine Learning Repository.
Referencia original: "Simplifying decision trees", Int J Man-Machine Studies 27, 1987.

- Fuente: https://archive.ics.uci.edu/dataset/27/credit+approval

**Dimensiones:**

- Filas: 690
- Columnas: 16 (15 atributos + 1 clase)

**Variable objetivo:** `A16` — resultado de la solicitud (+ aprobado, - rechazado)

**Atributos (todos anonimizados):**
| Variable | Tipo | Valores posibles |
|----------|------|-----------------|
| A1 | Categórica | b, a |
| A2 | Continua | numérico |
| A3 | Continua | numérico |
| A4 | Categórica | u, y, l, t |
| A5 | Categórica | g, p, gg |
| A6 | Categórica | c, d, cc, i, j, k, m, r, q, w, x, e, aa, ff |
| A7 | Categórica | v, h, bb, j, n, z, dd, ff, o |
| A8 | Continua | numérico |
| A9 | Binaria | t, f |
| A10 | Binaria | t, f |
| A11 | Continua | numérico |
| A12 | Binaria | t, f |
| A13 | Categórica | g, p, s |
| A14 | Continua | numérico |
| A15 | Continua | numérico |
| A16 | Clase | +, - (TARGET) |

**Valores nulos:**

- Presentes en columnas A1, A2, A4, A5, A6, A7, A14 (marcados como '?')
- Imputación: KNN para numéricas, moda para categóricas

**Características especiales:**

- Todos los atributos están completamente anonimizados por privacidad
- Mezcla rica de tipos de datos: continuas, nominales con pocos y muchos valores
- 37 registros (~5%) tienen al menos un valor nulo
- Dataset pequeño (690 filas) pero desafiante por la mezcla de tipos

**Usos típicos:** Clasificación binaria, evaluación de riesgo crediticio,
benchmark de algoritmos de árboles de decisión.

---

### 🦘 7. Statlog Australian Credit Dataset

**Descripción:**
Dataset de solicitudes de crédito originadas en Australia, también recopilado
por Ross Quinlan en 1987. Al igual que el Credit Approval Dataset, todos los
atributos han sido anonimizados para proteger la confidencialidad. Forma parte
de la colección Statlog del proyecto europeo de comparación de clasificadores.
Existe en el repositorio UCI como una variante del Credit Approval Dataset con
algunas diferencias en la codificación de variables.

**Origen:** Ross Quinlan (1987). UCI Machine Learning Repository / Proyecto Statlog.

- Fuente: https://archive.ics.uci.edu/dataset/143/statlog+australian+credit+approval

**Dimensiones:**

- Filas: 690
- Columnas: 15 (14 atributos + 1 clase)

**Variable objetivo:** `A15` — decisión (0 = rechazado, 1 = aprobado)

**Estructura de variables:**

- 6 variables numéricas (continuas): A2, A3, A7, A10, A13, A14
- 8 variables categóricas (originalmente con etiquetas, reconvertidas a números): A1, A4, A5, A6, A8, A9, A11, A12
- Las etiquetas categóricas originales fueron convertidas a números enteros
  para facilitar el procesamiento estadístico

**Valores nulos:** Este dataset NO tiene valores nulos en su versión estándar.

**Diferencias con Credit Approval (Dataset 6):**

- Mismo origen pero diferente preprocesamiento
- Australian Credit tiene variables categóricas convertidas a enteros
- Credit Approval mantiene las variables categóricas como texto
- Australian Credit no tiene valores nulos; Credit Approval sí los tiene
- La variable objetivo es 0/1 en Australian vs +/- en Credit Approval

**Características especiales:**

- Útil para comparar directamente con Credit Approval
- Al tener todo numérico, es más directo para aplicar modelos sin encoding previo
- Dataset pequeño y limpio, ideal para benchmarking rápido

**Usos típicos:** Clasificación binaria, evaluación de riesgo crediticio,
comparación de clasificadores (benchmark), proyecto Statlog.

---

### 🎗️ 8. Breast Cancer Wisconsin (Diagnostic)

**Descripción:**
Dataset creado a partir de imágenes digitalizadas de biopsias por aspiración
con aguja fina (Fine Needle Aspirate — FNA) de masas mamarias. Las características
fueron computadas para describir los núcleos celulares presentes en las imágenes.
Fue creado por el Dr. William H. Wolberg de la Universidad de Wisconsin en
colaboración con W. Nick Street y Olvi L. Mangasarian. Es uno de los datasets
médicos más citados y utilizados en machine learning para diagnóstico clínico.

**Origen:** W. Wolberg, O. Mangasarian, N. Street y W. Street (1993–1995).
Universidad de Wisconsin - Madison.
UCI Machine Learning Repository.

- Fuente: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- Donado al UCI: 1 de noviembre de 1995

**Dimensiones:**

- Filas: 569
- Columnas: 32 (ID + diagnosis + 30 features numéricas)
- Sin valores nulos

**Variable objetivo:** `diagnosis` — M (Maligno) o B (Benigno)

**Distribución del target:**

- Benigno (B): 357 casos (~62.7%)
- Maligno (M): 212 casos (~37.3%)

**Estructura de las 30 features:**
Para cada una de las 10 características del núcleo celular, se calcularon
3 estadísticos: media (mean), error estándar (se) y peor valor (worst).
Las 10 características base son:

| Característica    | Descripción                                        |
| ----------------- | -------------------------------------------------- |
| radius            | Radio medio de las células                         |
| texture           | Desviación estándar de valores de escala de grises |
| perimeter         | Perímetro del núcleo                               |
| area              | Área del núcleo                                    |
| smoothness        | Variación local en longitudes de radio             |
| compactness       | Perímetro² / área – 1.0                            |
| concavity         | Severidad de porciones cóncavas del contorno       |
| concave_points    | Número de porciones cóncavas del contorno          |
| symmetry          | Simetría del núcleo                                |
| fractal_dimension | Aproximación de la "costa" – 1                     |

Esto resulta en 30 columnas: `mean_radius`, `se_radius`, `worst_radius`, etc.

**Características especiales:**

- Radio, perímetro y área tienen correlación muy alta entre sí (multicolinealidad)
- Las variables de concavidad (`concavity`, `concave_points`) son las más
  discriminativas para separar maligno de benigno
- No requiere imputación (0 valores nulos)
- Excelente para visualizar separabilidad con PCA o pairplots

**Usos típicos:** Clasificación binaria, diagnóstico médico asistido por ML,
selección de características, PCA, SVM, Random Forest.

---

### 🧠 9. Meningitis Dataset

**Descripción:**
Dataset clínico con características de pacientes para clasificar el tipo de
meningitis o apoyar su diagnóstico diferencial. La meningitis es una inflamación
de las meninges (membranas que rodean el cerebro y la médula espinal), que puede
ser causada por bacterias, virus u hongos. El diagnóstico diferencial rápido
es crítico para el tratamiento.

**Origen:** Disponible en Kaggle.

- Fuente: https://www.kaggle.com/datasets/joebeachcapital/meningitis

**Características del dataset:**

- Contiene variables clínicas de pacientes con diagnóstico de meningitis
- Variables incluyen signos y síntomas clínicos, resultados de laboratorio
  del líquido cefalorraquídeo (LCR) y características demográficas
- La variable objetivo indica el tipo o diagnóstico de meningitis

**Variables típicas en datasets de meningitis:**
| Variable | Descripción |
|----------|-------------|
| age | Edad del paciente |
| temperature | Temperatura corporal |
| headache | Presencia de cefalea |
| neck_stiffness | Rigidez de nuca (signo de Kernig/Brudzinski) |
| csf_glucose | Glucosa en líquido cefalorraquídeo |
| csf_protein | Proteínas en LCR |
| csf_cells | Recuento celular en LCR |
| diagnosis | Tipo de meningitis (TARGET) |

**Características especiales:**

- Dataset clínico con variables de laboratorio especializadas (LCR)
- El diagnóstico diferencial entre meningitis bacteriana y viral es
  crítico: la bacteriana requiere antibióticos urgentes
- Puede contener valores nulos por la naturaleza de los datos clínicos
  (no siempre se realizan todos los estudios)

**Usos típicos:** Clasificación multiclase o binaria, diagnóstico clínico
asistido, análisis de datos médicos, predicción de tipo de infección.

---

## 🔧 Herramientas y Librerías Utilizadas

```python
pandas        # Manipulación y análisis de datos
numpy         # Operaciones numéricas
matplotlib    # Visualizaciones básicas
seaborn       # Visualizaciones estadísticas avanzadas
scikit-learn  # KNNImputer para imputación de valores nulos
jupyter       # Entorno de notebooks
```

## ⚙️ Metodología aplicada a cada dataset

1. **Carga de datos** — lectura del archivo con pandas, revisión del encoding
2. **Vista general** — shape, head(), dtypes, identificación de variables
3. **Valores nulos** — isnull().sum(), porcentaje por columna
4. **Imputación** — KNN Imputer para numéricas, moda para categóricas
5. **Estadísticas descriptivas** — describe() para numéricas
6. **Visualizaciones** — distribución del target, histogramas, boxplots, heatmap de correlaciones

## 👩‍💻 Autora

Natalia Camila Diaz Campos — Primer Parcial 2026

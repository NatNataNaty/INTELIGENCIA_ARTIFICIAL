# Detalle de Trabajo Realizado - Laboratorio 7: Aprendizaje No Supervisado, Semi-supervisado y Activo

Este documento contiene una explicación detallada de todas las implementaciones, adaptaciones teóricas y experimentación práctica llevada a cabo en el cuadernillo **`02 aprendizaje no supervisado y semisupervisado.ipynb`** dentro de la carpeta `lab7`.

---

## Introducción
El aprendizaje no supervisado es fundamental para extraer patrones significativos de datos que carecen de etiquetas (el escenario más común en el mundo real). En este laboratorio hemos explorado cómo:
1. Generar datos sintéticos realistas con un número aleatorio de clusters bien separados.
2. Identificar el número óptimo de clusters usando inercia (Codo) y coeficientes de silueta (Siluetas).
3. Utilizar agrupamiento por K-Means para reducir de manera masiva el costo de etiquetado manual de un dataset real de **imágenes de componentes electrónicos** mediante **Aprendizaje Semi-supervisado** y **Aprendizaje Activo**.

---

## Punto 1: Análisis de Clusters Sintéticos y Selección del Número Óptimo de Grupos

### 1. Generador de Centroides Aleatorios y Separados
* **El Problema**: Los generadores estándar como `make_blobs` pueden colocar centroides demasiado juntos si se eligen al azar en un espacio cerrado. Esto dificulta la verificación visual y distorsiona el análisis de métricas.
* **Nuestra Solución**: Implementamos la función `generate_separated_centroids(k, min_dist)` utilizando una estrategia de **muestreo por rechazo**. 
  * Se genera un número aleatorio de clusters $k$ entre 1 y 20 (`k_true`).
  * Cada centroide subsecuente se genera de manera aleatoria, pero se calcula su distancia euclidiana con todos los centroides aceptados previamente.
  * Si la distancia mínima es menor que `min_dist` (configurada en 4.5 unidades), el punto candidato es rechazado y se vuelve a intentar.
  * Esto asegura que los clusters estén distribuidos homogéneamente y completamente separados.
* **Visualización**: Se grafica el dataset bidimensional con `matplotlib` mostrando los cúmulos separados de manera nítida.

### 2. K-Means y Fronteras de Decisión
* Entrenamos el modelo `KMeans` utilizando inicialización inteligente `k-means++` para evitar mínimos locales y acelerar la convergencia.
* Graficamos las fronteras de decisión (teselación de Voronoi) que delimitan la influencia de cada centroide, verificando visualmente que K-Means localiza con precisión el centro de cada agrupación sintética.

### 3. Método del Codo (Elbow Method)
* Calculamos la **inercia** (suma de distancias al cuadrado de las muestras a su centroide asignado) para valores de $k$ desde 1 hasta $k_{\text{true}} + 5$ (máximo 20).
* Al graficar la curva de inercia vs $k$, identificamos claramente una caída abrupta seguida de un comportamiento casi lineal. El punto de inflexión o "codo" coincide exactamente con el número real de clusters, validando visualmente la inercia como una métrica de selección de hiperparámetros.

### 4. Coeficiente de Silueta (Silhouette Score)
* Graficamos el coeficiente de silueta promedio para cada $k$. El pico global de la curva se sitúa exactamente en $k_{\text{true}}$, lo que demuestra que esta métrica es un excelente indicador cuantitativo para determinar el número óptimo de grupos.
* Implementamos **diagramas de silueta por cluster** que grafican los coeficientes individuales de cada muestra ordenados por cluster:
  * Cuando $k = k_{\text{true}}$, todos los clusters muestran perfiles amplios que superan la línea vertical del promedio de silueta, y casi ninguna muestra tiene coeficientes negativos.
  * Cuando $k < k_{\text{true}}$ o $k > k_{\text{true}}$, algunos clusters muestran perfiles muy estrechos o coeficientes negativos abundantes, revelando visualmente la sub/sobreagrupación.

---

## Punto 2: Aprendizaje Semi-supervisado y Activo con Imágenes de Componentes Electrónicos

Para esta sección, sustituimos el dataset genérico de MNIST por el **conjunto de datos real de imágenes de componentes electrónicos** ubicado en la carpeta `lab7\images`.

### 1. Preprocesamiento e Ingeniería de Características de Imágenes
* **Carga**: Recorrimos las carpetas del dataset (e.g., `LED`, `Bypass-capacitor`, `PNP-transistor`, etc.).
* **Optimización y Robustez**: Implementamos un cargador dinámico y tolerante a fallos que:
  * Filtra solo archivos de imagen válidos (`.jpg`, `.jpeg`, `.png`).
  * Convierte las imágenes a escala de grises (`L`) usando `Pillow`.
  * Redimensiona cada imagen a $32 \times 32$ píxeles para mantener la eficiencia de cómputo.
  * Normaliza los valores de los píxeles al rango $[0.0, 1.0]$.
  * Aplana cada matriz a un vector de 1024 características.
  * Carga un subconjunto óptimo de 10 clases de componentes con hasta 100 imágenes por clase (total de 1,000 imágenes) para garantizar un entrenamiento rápido en la máquina local.

### 2. Flujo de Aprendizaje Semi-supervisado
Comparamos cuantitativamente la precisión de la Regresión Logística bajo diferentes regímenes de etiquetado en el conjunto de prueba (80/20 train/test split):

* **Escenario A: Clasificador Base (Línea de Base)**
  * Seleccionamos 50 imágenes al azar del conjunto de entrenamiento y "solicitamos" sus etiquetas reales.
  * Entrenamos una regresión logística básica.
  * *Resultado*: La exactitud es relativamente baja debido a que la selección aleatoria deja muchas clases sin representación y no capta la estructura global de los datos.

* **Escenario B: Etiquetado de Representantes con K-Means**
  * Agrupamos el conjunto de entrenamiento en 50 clusters.
  * Para cada cluster, encontramos la muestra real más cercana al centroide (el **representante** del cluster).
  * Etiquetamos únicamente estos 50 representantes estratégicos.
  * *Resultado*: La exactitud en el conjunto de prueba aumenta de manera notable, ya que los representantes de K-Means cubren uniformemente la diversidad del espacio de características de los componentes electrónicos.

* **Escenario C: Propagación de Etiquetas**
  * Propagamos de manera automática la etiqueta de cada uno de los 50 representantes a todas las demás imágenes pertenecientes a su respectivo cluster.
  * Entrenamos la Regresión Logística sobre todo el conjunto de entrenamiento con estas etiquetas propagadas.
  * *Resultado*: La exactitud aumenta significativamente. Al propagar las etiquetas, el modelo aprovecha la gran cantidad de datos y los límites de decisión reales de las imágenes de componentes electrónicos con costo de etiquetado manual cero.

### 3. Flujo de Aprendizaje Activo (Active Learning)
* Usamos el modelo entrenado con etiquetas propagadas para predecir las probabilidades de clase de todo el conjunto de entrenamiento.
* **Detección de Incertidumbre**: Calculamos la probabilidad máxima asignada a la clase ganadora de cada muestra. Las probabilidades más bajas corresponden a las muestras donde el modelo tiene mayor duda (límites de decisión ambiguos).
* **Intervención del Oráculo**: Tomamos las 50 imágenes con mayor incertidumbre y las etiquetamos con su clase real de componentes.
* **Reentrenamiento**: Reemplazamos sus etiquetas propagadas por las reales y reentrenamos el modelo.
* *Resultado*: Se logra una exactitud sobresaliente en el conjunto de prueba, ya que corregir las muestras dudosas inyecta información de altísimo valor para perfeccionar las fronteras de clasificación.

---

## Resumen del Progreso y Resultados

| Escenario de Aprendizaje | N° de Imágenes Etiquetadas Manualmente | Propósito / Beneficio |
| :--- | :--- | :--- |
| **Línea de Base** | 50 aleatorias | Control básico (Bajo rendimiento). |
| **Representantes** | 50 seleccionadas por K-Means | Cobertura óptima del espacio de componentes electrónicos. |
| **Propagación** | 50 seleccionadas (total auto-etiquetado) | Aprendizaje semi-supervisado masivo a coste de etiquetado cero. |
| **Aprendizaje Activo** | 50 iniciales + 50 dudosas corregidas | Refinamiento de la frontera de decisión resolviendo las dudas clave. |

Este flujo demuestra de manera práctica y rigurosa cómo el aprendizaje no supervisado y el semi-supervisado/activo pueden resolver problemas reales de visión por computadora con una fracción mínima del costo humano tradicional de etiquetado de datos.

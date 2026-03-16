# ==============================================================================
# Regresión Logística - Predicción de Resistencia al Arresto
# ==============================================================================
# Este script implementa el algoritmo de Regresión Logística
# para predecir si un arrestado resistirá (1) o no (0) el arresto
# en base a su 'Edad' (AgeAtArrestTime) y 'Peso' (Weight).
# Dataset utilizado: Dallas Police Arrests.csv

# ------------------------------------------------------------------------------
# 1. Importación de Librerías
# ------------------------------------------------------------------------------
import os
import numpy as np           # Computación vectorial y matemática
import pandas as pd          # Manipulación y carga del dataset CSV
from matplotlib import pyplot # Trazado de gráficos
from scipy import optimize    # Módulo de optimización

# ------------------------------------------------------------------------------
# 2. Carga y Preparación de Datos
# ------------------------------------------------------------------------------
# Ruta al dataset (relativa desde repo/practico2/...)
ruta_dataset = 'cosasvario/Dallas Police Arrests.csv'

print("Cargando el dataset de arrestos en Dallas...")
try:
    # Usamos low_memory=False porque el dataset es grande y tiene tipos mixtos
    data = pd.read_csv(ruta_dataset, low_memory=False)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {ruta_dataset}")
    exit()

print("\n================= ANÁLISIS DE DATOS DEL DATASET =================")
print(f"1. Tamaño del dataset original: {data.shape[0]} filas y {data.shape[1]} columnas.")

# Columnas seleccionadas
columnas_seleccionadas = ['AgeAtArrestTime', 'Weight', 'ArResisted']

# Limpieza inicial: Convertir a numérico y eliminar nulos
for col in ['AgeAtArrestTime', 'Weight']:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Mapeo de ArResisted: Tratamos 'Yes' como 1 y 'No' o vacío como 0
# Nota: Ajustamos según los valores reales del dataset
data['ArResisted_binary'] = data['ArResisted'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

# Filtramos filas que tengan valores nulos en nuestras características
filas_antes = data.shape[0]
data = data.dropna(subset=['AgeAtArrestTime', 'Weight'])
filas_despues = data.shape[0]

print(f"\n2. Selección de características:")
print(f"   -> Características: ['AgeAtArrestTime', 'Weight']")
print(f"   -> Target: 'ArResisted' (binario)")
print(f"   -> Se eliminaron {filas_antes - filas_despues} filas con valores nulos o no numéricos.")

# Tomamos una muestra para el entrenamiento para que sea manejable y visualizable
# Seleccionamos una muestra balanceada si es posible, o simplemente una muestra aleatoria grande
# Dado que la resistencia suele ser rara, tomamos 2000 registros para asegurar presencia de casos positivos
sample_size = min(2000, data.shape[0])
data_sample = data.sample(n=sample_size, random_state=42)

# Extraemos X (Edad, Peso) e y
X = data_sample[['AgeAtArrestTime', 'Weight']].values
y = data_sample['ArResisted_binary'].values

m = y.size # Cantidad de ejemplos

print(f"\nTotal de datos en la muestra: {m}")
print(f"Desglose de 'y' (1 = Resistió, 0 = No Resistió): \n{pd.Series(y).value_counts()}")
print("=================================================================\n")

# ------------------------------------------------------------------------------
# 3. Visualización de los Datos
# ------------------------------------------------------------------------------
def plotData(X, y):
    """
    Grafica los puntos de datos X y y.
    """
    fig = pyplot.figure(figsize=(8, 6))

    pos = (y == 1)
    neg = (y == 0)

    # Grafica los ejemplos
    pyplot.plot(X[pos, 0], X[pos, 1], 'k+', lw=2, ms=8, label='Resistió (1)')
    pyplot.plot(X[neg, 0], X[neg, 1], 'ko', mfc='y', ms=8, mec='k', mew=1, label='No Resistió (0)')
    
    pyplot.xlabel('Edad (AgeAtArrestTime)')
    pyplot.ylabel('Peso (Weight)')
    pyplot.title('Distribución de Resistencia al Arresto vs (Edad y Peso)')
    pyplot.legend()
    pyplot.grid(True)

print("Generando gráfica de distribución de datos...")
plotData(X, y)

# ------------------------------------------------------------------------------
# 4. Implementación - Función Sigmoide
# ------------------------------------------------------------------------------
def sigmoid(z):
    z = np.array(z)
    # Clipping para evitar desbordamiento en exp
    z = np.clip(z, -500, 500)
    g = 1 / (1 + np.exp(-z))
    return g

# ------------------------------------------------------------------------------
# 5. Función de Costo y Gradiente
# ------------------------------------------------------------------------------
# Agregamos la columna de unos a X para el término de intercepción (theta_0)
m, n = X.shape
# Normalización simple para ayudar a la convergencia (opcional pero recomendado)
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_normalized = (X - X_mean) / X_std

X_ready = np.concatenate([np.ones((m, 1)), X_normalized], axis=1)

def costFunction(theta, X, y):
    m = y.size
    h = sigmoid(X.dot(theta))
    epsilon = 1e-15
    J = (1 / m) * np.sum(-y * np.log(h + epsilon) - (1 - y) * np.log(1 - h + epsilon))
    grad = (1 / m) * (h - y).dot(X)
    return J, grad

initial_theta = np.zeros(X_ready.shape[1])
cost, grad = costFunction(initial_theta, X_ready, y)
print(f'Costo con theta inicial (zeros): {cost:.3f}')

# ------------------------------------------------------------------------------
# 6. Optimización de Parámetros
# ------------------------------------------------------------------------------
historial_costo = []
historial_p = []

def callback_optimizacion(theta_actual):
    costo_actual, _ = costFunction(theta_actual, X_ready, y)
    historial_costo.append(costo_actual)
    probabilidades = sigmoid(X_ready.dot(theta_actual))
    p = np.round(probabilidades)
    historial_p.append(p)

print('\nOptimizando parámetros con scipy.optimize.minimize...')
options= {'maxiter': 1000}

res = optimize.minimize(costFunction, 
                        initial_theta, 
                        (X_ready, y), 
                        jac=True, 
                        method='TNC', 
                        callback=callback_optimizacion,
                        options=options)

cost = res.fun
theta_optimizado = res.x

print(f'\nCosto mínimo encontrado: {cost:.3f}')
print(f'Theta optimizados: {theta_optimizado}')

# ------------------------------------------------------------------------------
# 7. Evaluación y Predicción
# ------------------------------------------------------------------------------
def predict(theta, X):
    probabilidades = sigmoid(X.dot(theta))
    p = np.round(probabilidades)
    return p

predicciones = predict(theta_optimizado, X_ready)
precision = np.mean(predicciones == y) * 100
print(f'\nPrecisión del modelo en el set de entrenamiento: {precision:.2f}%')

# Predicción de un caso nuevo (Normalizando primero)
edad_test = 30.0
peso_test = 180.0
X_test_norm = (np.array([edad_test, peso_test]) - X_mean) / X_std
X_test_ready = np.array([1, X_test_norm[0], X_test_norm[1]])

prob_resistencia = sigmoid(np.dot(X_test_ready, theta_optimizado))
print('\n--------------------- PREDICCIÓN ---------------------')
print(f'Sujeto de prueba: Edad {edad_test}, Peso {peso_test}')
print(f'>> Probabilidad de resistencia: {prob_resistencia * 100:.2f}%')
print('------------------------------------------------------')

# Frontera de Decisión (en espacio normalizado)
print('\nGraficando frontera de decisión...')
plot_x = np.array([np.min(X_normalized[:, 0]), np.max(X_normalized[:, 0])])
plot_y = (-1. / theta_optimizado[2]) * (theta_optimizado[1] * plot_x + theta_optimizado[0])

# Volver a escalar para la gráfica original
plot_x_orig = plot_x * X_std[0] + X_mean[0]
plot_y_orig = plot_y * X_std[1] + X_mean[1]

pyplot.plot(plot_x_orig, plot_y_orig, 'b-', label='Frontera de Decisión')
pyplot.legend()
pyplot.show()

# 8. Gráficas de Aprendizaje
print('\nGenerando curvas de aprendizaje...')
iteraciones = np.arange(1, len(historial_costo) + 1)
historial_precision = [np.mean(p == y) * 100 for p in historial_p]

fig, (ax1, ax2) = pyplot.subplots(1, 2, figsize=(14, 5))
ax1.plot(iteraciones, historial_costo, 'b-')
ax1.set_title('Costo vs Iteraciones')
ax1.grid(True)

ax2.plot(iteraciones, historial_precision, 'g-')
ax2.set_title('Precisión vs Iteraciones')
ax2.grid(True)

pyplot.tight_layout()
pyplot.show()

# Mini-demo: dataset inventado (SIN ruido) + modelo de clasificación para d/dx cos(x)
# ES: Este script genera datos ficticios de respuestas de alumnado, entrena un clasificador y da una recomendación.
# EN: This script creates synthetic student-answer data, trains a classifier, and outputs a recommendation.

# ES: Importamos numpy para generar números aleatorios y trabajar con arrays.
# EN: Import numpy to generate random numbers and work with arrays.
import numpy as np

# ES: Importamos pandas para manejar datos en forma de tabla (DataFrame).
# EN: Import pandas to handle tabular data (DataFrame).
import pandas as pd

# ES: Importamos utilidades de scikit-learn para dividir datos en entrenamiento/prueba.
# EN: Import utilities from scikit-learn to split data into train/test sets.
from sklearn.model_selection import train_test_split

# ES: OneHotEncoder convierte categorías (texto) en columnas numéricas binarias.
# EN: OneHotEncoder converts categorical text variables into numeric binary columns.
from sklearn.preprocessing import OneHotEncoder

# ES: ColumnTransformer aplica transformaciones distintas a columnas distintas.
# EN: ColumnTransformer applies different transformations to different columns.
from sklearn.compose import ColumnTransformer

# ES: Pipeline encadena "preprocesado + modelo" en un único objeto.
# EN: Pipeline chains "preprocessing + model" into a single object.
from sklearn.pipeline import Pipeline

# ES: Usamos Regresión Logística como clasificador sencillo para múltiples clases.
# EN: Use Logistic Regression as a simple multi-class classifier.
from sklearn.linear_model import LogisticRegression

# ES: Importamos métricas para evaluar el modelo.
# EN: Import metrics to evaluate the model.
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ----------------------------
# 1) Crear dataset inventado (SIN ruido)
# ----------------------------

# ES: Creamos un generador aleatorio reproducible (siempre dará el mismo resultado).
# EN: Create a reproducible random generator (same results every run).
rng = np.random.default_rng(42)

# ES: Número de intentos/respuestas simuladas del alumnado.
# EN: Number of simulated student attempts.
n = 240

# ES: Definimos las etiquetas posibles (tipo de respuesta/error que queremos clasificar).
# EN: Define the possible labels (types of answers/errors we want to classify).
labels = np.array([
    "correct",              # ES: Respuesta correcta (-sin(x)) | EN: Correct answer (-sin(x))
    "sign_error",           # ES: Error de signo (+sin(x))     | EN: Sign error (+sin(x))
    "confuse_cos",          # ES: Confunde con cos             | EN: Confuses with cos
    "zero_or_constant",     # ES: Dice 0 o 1                   | EN: Answers 0 or 1
    "syntax_or_other"       # ES: Respuesta rara               | EN: Weird/other response
])

# ES: Generamos las etiquetas reales (y) con una distribución razonable.
# EN: Generate the true labels (y) with a reasonable distribution.
y = rng.choice(labels, size=n, p=[0.45, 0.18, 0.14, 0.10, 0.13])

# ES: Creamos listas vacías para ir guardando las "variables observables" del intento.
# EN: Create empty lists to store the observable variables for each attempt.
answers = []
time_s = []
backspaces = []
steps = []
input_mode = []

# ES: Generamos cada intento condicionado por su etiqueta (así el modelo podrá aprender patrones).
# EN: Generate each attempt conditioned on its label (so the model can learn patterns).
for lab in y:
    if lab == "correct":
        # ES: En correctos, suele aparecer -sin(x).
        # EN: For correct answers, -sin(x) appears most of the time.
        answers.append(rng.choice(["-sin(x)", "other"], p=[0.95, 0.05]))
        # ES: Tiempo medio moderado con variación.
        # EN: Moderate average time with variation.
        time_s.append(rng.normal(32, 10))
        # ES: Pocos borrados.
        # EN: Few backspaces.
        backspaces.append(rng.poisson(2))
        # ES: 1-3 pasos típicos.
        # EN: Typical 1-3 steps.
        steps.append(rng.poisson(2))
        # ES: A veces test, a veces escrito.
        # EN: Sometimes multiple-choice, sometimes typed.
        input_mode.append(rng.choice(["multiple_choice", "typed"], p=[0.55, 0.45]))

    elif lab == "sign_error":
        # ES: En error de signo, suele aparecer sin(x).
        # EN: For sign errors, sin(x) appears most of the time.
        answers.append(rng.choice(["sin(x)", "other"], p=[0.8, 0.2]))
        # ES: Tarda algo más.
        # EN: Slightly slower.
        time_s.append(rng.normal(40, 12))
        backspaces.append(rng.poisson(3))
        steps.append(rng.poisson(2))
        input_mode.append(rng.choice(["multiple_choice", "typed"], p=[0.6, 0.4]))

    elif lab == "confuse_cos":
        # ES: Confunde con cos(x) o -cos(x).
        # EN: Confuses with cos(x) or -cos(x).
        answers.append(rng.choice(["-cos(x)", "cos(x)", "other"], p=[0.55, 0.25, 0.2]))
        time_s.append(rng.normal(45, 15))
        backspaces.append(rng.poisson(4))
        steps.append(rng.poisson(3))
        input_mode.append(rng.choice(["multiple_choice", "typed"], p=[0.5, 0.5]))

    elif lab == "zero_or_constant":
        # ES: Responde 0 o 1.
        # EN: Answers 0 or 1.
        answers.append(rng.choice(["0", "1", "other"], p=[0.6, 0.25, 0.15]))
        time_s.append(rng.normal(28, 10))
        backspaces.append(rng.poisson(2))
        steps.append(rng.poisson(1))
        input_mode.append(rng.choice(["multiple_choice", "typed"], p=[0.7, 0.3]))

    else:  # syntax_or_other
        # ES: Respuesta rara o incompleta.
        # EN: Weird or incomplete answer.
        answers.append("other")
        time_s.append(rng.normal(55, 20))
        backspaces.append(rng.poisson(6))
        steps.append(rng.poisson(1))
        input_mode.append(rng.choice(["multiple_choice", "typed"], p=[0.35, 0.65]))

# ES: Creamos el DataFrame final con todas las columnas.
# EN: Build the final DataFrame with all columns.
df = pd.DataFrame({
    "answer": answers,
    # ES: Convertimos tiempo a entero y limitamos a un rango razonable.
    # EN: Convert time to int and clip to a reasonable range.
    "time_s": np.clip(np.array(time_s), 5, 180).round(0).astype(int),
    "backspaces": np.clip(np.array(backspaces), 0, 25),
    "steps": np.clip(np.array(steps), 0, 10),
    "input_mode": input_mode,
    "label": y
})

# ES: Mostramos primeras filas para verificar que el dataset tiene sentido.
# EN: Print first rows to verify the dataset looks reasonable.
print("Primeras filas del dataset:\n")
print(df.head(10))


# ----------------------------
# 2) Entrenar un modelo de clasificación
# ----------------------------

# ES: X son las variables de entrada, y es la etiqueta que queremos predecir.
# EN: X are the input features, y is the label we want to predict.
X = df.drop(columns=["label"])
y = df["label"]

# ES: Dividimos en entrenamiento y prueba; stratify mantiene proporciones de clases.
# EN: Split into train/test; stratify keeps class proportions.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=7, stratify=y
)

# ES: Columnas categóricas (texto) y numéricas.
# EN: Categorical (text) and numeric columns.
categorical_cols = ["answer", "input_mode"]
numeric_cols = ["time_s", "backspaces", "steps"]

# ES: Preprocesado:
# - OneHotEncoder para categorías
# - numéricas pasan tal cual
# EN: Preprocessing:
# - OneHotEncoder for categorical variables
# - numeric variables pass through unchanged
preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols),
    ]
)

# ES: Clasificador: Regresión Logística multiclase.
# EN: Classifier: multi-class Logistic Regression.
clf = LogisticRegression(max_iter=2000)

# ES: Pipeline: primero preprocesa, luego entrena el modelo.
# EN: Pipeline: preprocess first, then train the model.
pipe = Pipeline(steps=[("prep", preprocess), ("clf", clf)])

# ES: Entrenamos el pipeline con datos de entrenamiento.
# EN: Fit the pipeline on training data.
pipe.fit(X_train, y_train)

# ES: Predecimos en el conjunto de prueba para evaluar.
# EN: Predict on the test set to evaluate.
pred = pipe.predict(X_test)

# ES: Calculamos accuracy (porcentaje de aciertos en test).
# EN: Compute accuracy (test correct rate).
print("\nAccuracy (test):", round(accuracy_score(y_test, pred), 3))

# ES: Matriz de confusión: cómo se confunden las clases entre sí.
# EN: Confusion matrix: how classes are confused with each other.
print("\nConfusion matrix (orden:", list(labels), "):\n")
print(confusion_matrix(y_test, pred, labels=labels))

# ES: Informe con precision/recall/f1 por clase.
# EN: Report with precision/recall/f1 per class.
print("\nInforme:\n")
print(classification_report(y_test, pred))


# ----------------------------
# 3) Reglas pedagógicas: traducir diagnóstico a recomendación
# ----------------------------

# ES: Esta función representa la parte "pedagógica" del sistema.
# EN: This function represents the "pedagogical" part of the system.
def next_step_recommendation(diagnosis: str) -> str:
    # ES/EN: Según el diagnóstico, devolvemos el tipo de itinerario recomendado.
    #        Based on the diagnosis, return the recommended next learning step.
    if diagnosis == "correct":
        return "Ampliación: regla de la cadena con cos(g(x)) y derivadas trigonométricas mixtas."
    if diagnosis == "sign_error":
        return "Refuerzo: tabla de derivadas trigonométricas + ejercicios de signos (-sin, -cos)."
    if diagnosis == "confuse_cos":
        return "Refuerzo: distinguir derivar cos vs sin con ejercicios de identificación rápida."
    if diagnosis == "zero_or_constant":
        return "Recuperación de concepto: qué significa derivar + derivadas básicas (constante, x, trig)."
    return "Apoyo: pedir pasos intermedios y feedback guiado; repetir con ejemplos similares."


# ----------------------------
# 4) Ejemplo de uso "como si fuera la app"
# ----------------------------

# ES: Simulamos un alumno que responde sin(x) (probable error de signo).
# EN: Simulate a student answering sin(x) (likely a sign error).
example_student = pd.DataFrame([{
    "answer": "sin(x)",
    "time_s": 37,
    "backspaces": 2,
    "steps": 1,
    "input_mode": "multiple_choice"
}])

# ES: El modelo predice el tipo de error.
# EN: The model predicts the error type.
diagnosis = pipe.predict(example_student)[0]

# ES: Mostramos diagnóstico y recomendación.
# EN: Print diagnosis and recommendation.
print("\n--- Ejemplo de alumno ---")
print(example_student)
print("Diagnóstico:", diagnosis)
print("Recomendación:", next_step_recommendation(diagnosis))

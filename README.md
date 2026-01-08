![alt text](image.png)
---

# 🚴 Predicción de la Demanda de Bicicletas Compartidas

**Bike Sharing Demand Prediction**

**Categoría:** Ciencia de Datos
**Subcategoría:** Científico de Datos (Regresión)
**Dificultad:** Fácil

---

## 📌 Descripción del proyecto

En este proyecto desarrollo un **modelo de Machine Learning para predecir la demanda de bicicletas compartidas**, utilizando datos históricos, temporales, climáticos y de calendario.

El objetivo es **estimar con precisión cuántas bicicletas serán utilizadas en un momento determinado**, aportando una solución basada en datos a un problema real de movilidad urbana.
Este reto me permitió aplicar de forma práctica los conocimientos adquiridos en el curso **Machine Learning A-Z**, integrando preprocesamiento, modelado supervisado y evaluación de resultados.

La demanda de bicicletas no es solo un número: es una señal del pulso de la ciudad.

---

## 🌍 Contexto y motivación

En un entorno urbano en constante cambio, **anticipar la demanda de transporte** es clave para:

* Optimizar la asignación de recursos
* Reducir costos operativos
* Mejorar la experiencia del usuario
* Tomar decisiones basadas en datos y no en intuición

BikeTech propone este desafío como un escenario realista donde los datos se convierten en una herramienta estratégica para la movilidad sostenible.

---

## 📊 Conjunto de datos

Trabajo con un **dataset histórico de bicicletas compartidas** que contiene:

### Variables temporales

* `dteday`: fecha
* `yr`: año
* `mnth`: mes
* `hr`: hora

### Variables climáticas

* `weathersit`: situación climática
* `temp`: temperatura
* `atemp`: sensación térmica
* `hum`: humedad
* `windspeed`: velocidad del viento

### Variables de calendario

* `season`: estación del año
* `holiday`: día festivo
* `weekday`: día de la semana
* `workingday`: día laborable

### Variable objetivo

* `cnt`: demanda total de bicicletas

Estas variables permiten modelar la relación entre **tiempo, clima, estacionalidad y comportamiento humano**.

---

## 🔧 Procesamiento de datos

El pipeline de datos incluye:

1. Limpieza y validación del dataset
2. Conversión y tratamiento de tipos de datos
3. Ingeniería de variables temporales y categóricas
4. Separación de datos de entrenamiento y prueba

El objetivo es garantizar **consistencia, reproducibilidad y calidad** antes del modelado.

---

## 🤖 Modelo predictivo

El problema se aborda como una tarea de **regresión supervisada**, donde se busca aproximar la función:

$$
cnt = f(tiempo, clima, estacionalidad)
$$

Se entrena un modelo predictivo priorizando:

* Capacidad de generalización
* Estabilidad del error
* Interpretabilidad

El modelo final se serializa para su reutilización y despliegue.

---

## 📈 Evaluación

El desempeño del modelo se evalúa utilizando:

* **MAPE (Mean Absolute Percentage Error)**

Esta métrica permite interpretar el error de predicción en términos porcentuales, lo cual es especialmente adecuado para problemas de demanda.

En ciencia de datos, errar poco también es una forma de respeto al dato.

---

## 📤 Resultados y entrega

El resultado final del proyecto es el archivo **`predictions.json`**, que contiene las predicciones de demanda por marca temporal:

```json
{
    "target": {
        "2012-08-07 12:00": 23,
        "2012-08-07 13:00": 52,
        "2012-08-07 14:00": 312,
        "2012-08-07 15:00": 11,
        "2012-08-07 16:00": 125,
        "2012-08-07 17:00": 642,
        "2012-08-07 18:00": 76,
        "2012-08-07 19:00": 53
    }
}
```

Cada clave representa una fecha y hora, y cada valor corresponde a la demanda estimada por el modelo.

---

## 📂 Estructura del repositorio

```
|__ README.md
|__ requirements.txt
|
|__ data
|  |__ train
|  |  |__ train.csv
|  |
|  |__ test
|     |__ test.csv
|
|__ src
|  |__ data_processing.py
|  |__ model_training.py 
|  |__ model_prediction.py
|  |__ utils.py
|
|__ models
|  |__ model.pkl
|
|__ predictions
   |__ example_predictions.json
   |__ predictions.json
```

La estructura sigue buenas prácticas de **modularización, claridad y reproducibilidad**.

---

## 🧠 Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Scikit-learn

Todas las dependencias están especificadas en `requirements.txt`.

---

## ⚠️ Consideraciones éticas y técnicas

* Todo el procesamiento y entrenamiento del modelo se realiza exclusivamente con las librerías permitidas.
* El código puede ser revisado para garantizar la integridad académica.
* El proyecto cumple principios de transparencia y reproducibilidad.

---

## 🚀 Reflexión final

Este proyecto consolida mis bases como **Científico de Datos**, integrando teoría y práctica en un problema real.
Los datos, bien tratados, no solo predicen: **orientan decisiones**.

Este no es un punto final, sino un punto de partida hacia modelos más robustos, escalables y con impacto real en la ciudad.

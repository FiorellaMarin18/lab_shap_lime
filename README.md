# 🧠 Análisis de Aprobación de Créditos con Machine Learning y LIME

Este proyecto permite entrenar un modelo de machine learning para predecir si un cliente es un buen candidato para un crédito, e interpretar sus predicciones usando LIME. 

## 📁 Estructura del Proyecto

LAB_SHAP_LIME/
├── dataset/
│ └── clientes_credito.csv # Dataset con al menos 1000 registros
│ └── data.py
├── main.ipynb # Código principal del proyecto
├── lime_explicacion_aprobado.html
├── lime_explicacion_rechazado.html
└── README.md # Este archivo

---

## 📊 Descripción del Dataset

El archivo `clientes_credito.csv` debe contener las siguientes columnas:

- `Edad`: Edad del cliente (numérico).
- `Ingresos`: Ingresos anuales del cliente (numérico).
- `Historial Crediticio`: "Bueno", "Regular", "Malo".
- `Deuda Total`: Total de deuda pendiente (numérico).
- `Historial de Pagos`: "Excelente", "Bueno", "Regular", "Malo".
- `Target`: 1 (aprobado), 0 (rechazado).

---

## ⚙️ Requisitos

Instala las dependencias necesarias:

```bash
pip install shap lime scikit-learn pandas matplotlib


🚀 Ejecución del Código
Se debe ejecutar cada bloque para obtener las graficas 


📈 Visualización
Una vez ejecutado el script, abre en tu navegador:

lime_explicacion_aprobado.html: Explicación de un caso donde el crédito fue aprobado.

lime_explicacion_rechazado.html: Explicación de un caso donde el crédito fue rechazado.

✅ Estado
 Dataset realista generado manualmente

 Preprocesamiento con One-Hot Encoding

 Entrenamiento de modelo Random Forest

 Evaluación del modelo

 Interpretabilidad con LIME

 Visualización de casos en HTML
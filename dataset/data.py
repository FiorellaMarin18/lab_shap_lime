import pandas as pd
import numpy as np
import os

# Crear carpeta "dataset" si no existe
os.makedirs("dataset", exist_ok=True)

# Definir número de muestras
n_samples = 1000
rng = np.random.default_rng(42)

# Opciones categóricas
historial_crediticio_opciones = ['Bueno', 'Regular', 'Malo']
historial_pagos_opciones = ['Excelente', 'Bueno', 'Regular', 'Malo']

# Generar columnas
edad = rng.integers(20, 70, size=n_samples)
ingresos = rng.integers(20000, 100000, size=n_samples)
historial_crediticio = rng.choice(historial_crediticio_opciones, size=n_samples, p=[0.5, 0.3, 0.2])
deuda_total = rng.integers(1000, 30000, size=n_samples)
historial_pagos = rng.choice(historial_pagos_opciones, size=n_samples, p=[0.3, 0.4, 0.2, 0.1])

# Lógica simplificada para definir el Target
def calcular_target(ingreso, deuda, hist_cred, hist_pago):
    if ingreso > 40000 and deuda < 15000 and hist_cred == 'Bueno' and hist_pago in ['Bueno', 'Excelente']:
        return 1
    return 0

target = [
    calcular_target(ing, deuda, cred, pago)
    for ing, deuda, cred, pago in zip(ingresos, deuda_total, historial_crediticio, historial_pagos)
]

# Crear DataFrame
df = pd.DataFrame({
    'Edad': edad,
    'Ingresos': ingresos,
    'Historial Crediticio': historial_crediticio,
    'Deuda Total': deuda_total,
    'Historial de Pagos': historial_pagos,
    'Target': target
})

# Guardar como CSV
df.to_csv('dataset/clientes_credito.csv', index=False, encoding='utf-8')
print("✅ Dataset generado y guardado en 'dataset/clientes_credito.csv'")

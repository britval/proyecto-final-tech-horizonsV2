import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurar semilla para reproducibilidad
np.random.seed(42)

# Generar datos de ejemplo sobre acceso a educación (ODS 4)
# Simulando datos de diferentes países de Latinoamérica

paises = ['Panama', 'Costa Rica', 'Guatemala', 'Honduras', 'El Salvador', 'Nicaragua', 'Belice']
regiones = ['Urbano', 'Rural']
niveles_educacion = ['Primaria', 'Secundaria', 'Universidad']

# Generar datos para varios años
years = list(range(2015, 2024))
data = []

for year in years:
    for pais in paises:
        for region in regiones:
            for nivel in niveles_educacion:
                # Simular tasas de matriculación con tendencias realistas
                base_rate = {
                    'Primaria': 95 if region == 'Urbano' else 85,
                    'Secundaria': 80 if region == 'Urbano' else 60, 
                    'Universidad': 35 if region == 'Urbano' else 15
                }[nivel]
                
                # Añadir variación por país
                country_factor = {
                    'Panama': 1.1, 'Costa Rica': 1.15, 'Guatemala': 0.8,
                    'Honduras': 0.75, 'El Salvador': 0.85, 'Nicaragua': 0.7, 'Belice': 0.9
                }[pais]
                
                # Tendencia de mejora año a año
                year_improvement = (year - 2015) * 0.5
                
                tasa_matriculacion = min(100, base_rate * country_factor + year_improvement + np.random.normal(0, 3))
                tasa_matriculacion = max(0, tasa_matriculacion)
                
                # Generar otros indicadores relacionados
                tasa_desercion = max(0, 20 - tasa_matriculacion/5 + np.random.normal(0, 2))
                inversion_per_capita = np.random.normal(500, 100) * country_factor
                poblacion_estudiantil = np.random.randint(10000, 100000)
                
                data.append({
                    'Año': year,
                    'País': pais,
                    'Región': region,
                    'Nivel_Educativo': nivel,
                    'Tasa_Matriculación': round(tasa_matriculacion, 1),
                    'Tasa_Deserción': round(tasa_desercion, 1),
                    'Inversión_Per_Capita_USD': round(inversion_per_capita, 2),
                    'Población_Estudiantil': poblacion_estudiantil
                })

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como CSV
df.to_csv('ejemplo-dashboard/data/educacion_latinoamerica.csv', index=False)

print("✅ Datos de ejemplo creados exitosamente!")
print(f"📊 Dataset generado: {len(df)} registros")
print(f"📅 Años: {df['Año'].min()} - {df['Año'].max()}")
print(f"🌍 Países: {len(df['País'].unique())}")
print(f"📚 Niveles educativos: {len(df['Nivel_Educativo'].unique())}")

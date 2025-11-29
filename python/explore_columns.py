"""
Script para explorar valores en columnas específicas y ayudar a identificar
cuál corresponde a 'interés en medio ambiente' y uso de redes sociales
"""

import pandas as pd
import numpy as np

print("="*70)
print("Explorador de Columnas - Latinobarómetro 2024")
print("Identificación de columnas para Power BI")
print("="*70)

# Cargar datos
df = pd.read_csv('../data/Latinobarometro_2024.csv', sep=';', encoding='utf-8')

print(f"\nDataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas\n")

# Analizar columnas P30ST (posibles temas de interés)
print("="*70)
print("ANÁLISIS DE COLUMNAS P30ST (Posibles temas de interés)")
print("="*70)

p30_columns = [col for col in df.columns if col.startswith('P30ST')]
for col in p30_columns:
    valores = sorted(df[col].dropna().unique())
    conteo = df[col].value_counts().sort_index()
    print(f"\n{col}:")
    print(f"  Valores únicos: {valores}")
    print(f"  Distribución de valores:")
    for val, count in conteo.head(10).items():
        porcentaje = (count / len(df)) * 100
        print(f"    {val}: {count:,} ({porcentaje:.1f}%)")
    
    # Verificar si hay valores que indiquen escala (ej: 1-4, 1-5)
    valores_validos = [v for v in valores if v not in [-1, -2, -3, -5, 96, 97, 98, 99]]
    if valores_validos:
        print(f"  Rango de valores válidos: {min(valores_validos)} - {max(valores_validos)}")
        print(f"  Promedio (valores válidos): {df[df[col].isin(valores_validos)][col].mean():.2f}")

# Analizar P31ST (posible pregunta única sobre ambiente)
print("\n" + "="*70)
print("ANÁLISIS DE P31ST (Posible interés en ambiente)")
print("="*70)

if 'P31ST' in df.columns:
    valores = sorted(df['P31ST'].dropna().unique())
    conteo = df['P31ST'].value_counts().sort_index()
    print(f"\nP31ST:")
    print(f"  Valores únicos: {valores}")
    print(f"  Distribución:")
    for val, count in conteo.items():
        porcentaje = (count / len(df)) * 100
        print(f"    {val}: {count:,} ({porcentaje:.1f}%)")
    
    valores_validos = [v for v in valores if v not in [-1, -2, -3, -5, 96, 97, 98, 99]]
    if valores_validos:
        print(f"  Rango válido: {min(valores_validos)} - {max(valores_validos)}")
        print(f"  Promedio: {df[df['P31ST'].isin(valores_validos)]['P31ST'].mean():.2f}")

# Analizar P28ST (uso de redes sociales)
print("\n" + "="*70)
print("ANÁLISIS DE P28ST (Uso de redes sociales)")
print("="*70)

if 'P28ST' in df.columns:
    valores = sorted(df['P28ST'].dropna().unique())
    conteo = df['P28ST'].value_counts().sort_index()
    print(f"\nP28ST:")
    print(f"  Valores únicos: {valores}")
    print(f"  Distribución:")
    for val, count in conteo.items():
        porcentaje = (count / len(df)) * 100
        print(f"    {val}: {count:,} ({porcentaje:.1f}%)")

# Analizar P29ST (más sobre redes sociales)
print("\n" + "="*70)
print("ANÁLISIS DE P29ST (Más sobre redes sociales)")
print("="*70)

p29_columns = [col for col in df.columns if col.startswith('P29ST')]
for col in p29_columns[:5]:  # Primeras 5
    valores = sorted(df[col].dropna().unique())
    print(f"\n{col}:")
    print(f"  Valores únicos: {valores[:10]}...")  # Primeros 10
    conteo = df[col].value_counts().sort_index()
    print(f"  Distribución (primeros valores):")
    for val, count in conteo.head(5).items():
        porcentaje = (count / len(df)) * 100
        print(f"    {val}: {count:,} ({porcentaje:.1f}%)")

# Analizar confianza en medios
print("\n" + "="*70)
print("ANÁLISIS DE CONFIANZA EN MEDIOS (P23STM)")
print("="*70)

p23_columns = ['P23STM.1', 'P23STM.2', 'P23STM.3']
nombres_medios = ['TV', 'Redes Sociales', 'Otro Medio']

for col, nombre in zip(p23_columns, nombres_medios):
    if col in df.columns:
        valores_validos = df[col].replace([-1, -2, -3, -5, 96, 97, 98, 99], np.nan)
        promedio = valores_validos.mean()
        print(f"\n{col} ({nombre}):")
        print(f"  Promedio de confianza: {promedio:.2f}")
        print(f"  Rango: {valores_validos.min():.0f} - {valores_validos.max():.0f}")
        print(f"  Valores válidos: {valores_validos.notna().sum():,} de {len(df):,}")

# Resumen de columnas importantes
print("\n" + "="*70)
print("RESUMEN Y RECOMENDACIONES")
print("="*70)

print("\n📋 COLUMNAS IDENTIFICADAS:")
print(f"  • Confianza en TV: P23STM.1")
print(f"  • Confianza en Redes Sociales: P23STM.2")
print(f"  • Confianza en Otro Medio: P23STM.3")

print(f"\n🔍 COLUMNAS A VERIFICAR EN CODEBOOK:")
print(f"  • Interés en ambiente: Revisar P30ST.A-E o P31ST")
print(f"  • Uso de redes sociales: Revisar P28ST, P29ST.A-H")

print(f"\n✅ SIGUIENTE PASO:")
print(f"  1. Abre el archivo 'Codebook Latinobarómetro.xlsx'")
print(f"  2. Busca las preguntas relacionadas con:")
print(f"     - Medio ambiente / Ambiente / Clima")
print(f"     - Uso de redes sociales / Redes sociales")
print(f"  3. Identifica los códigos de columna correspondientes")
print(f"  4. Actualiza las fórmulas DAX con los nombres correctos")

print("\n" + "="*70)


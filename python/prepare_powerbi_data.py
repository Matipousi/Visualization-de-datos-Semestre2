"""
Script para preparar y explorar datos de Latinobarómetro 2024 para Power BI
Identifica columnas relevantes y prepara el dataset optimizado
"""

import pandas as pd
import numpy as np

print("="*60)
print("Preparación de Datos para Power BI - Latinobarómetro 2024")
print("="*60)

# Carga de datos
print("\n1. Cargando datos...")
df = pd.read_csv('../data/Latinobarometro_2024.csv', sep=';', encoding='utf-8')
country_codes = pd.read_csv('../data/country_codes.csv', encoding='utf-8')

print(f"   Dataset principal: {df.shape[0]} filas, {df.shape[1]} columnas")
print(f"   Códigos de países: {country_codes.shape[0]} países")

# Identificar columnas relevantes
print("\n2. Identificando columnas relevantes...")

# Columnas básicas de filtros
columnas_filtros = {
    'IDENPA': 'Código de país',
    'EDAD': 'Edad',
    'SEXO': 'Sexo (1=Hombre, 2=Mujer)',
    'REEDUC.3': 'Años de estudio alcanzados'
}

# Columnas de confianza en medios (P23STM)
columnas_medios = [col for col in df.columns if 'P23STM' in col]
print(f"\n   Columnas de confianza en medios (P23STM):")
for col in columnas_medios:
    print(f"   - {col}")

# Buscar columnas relacionadas con ambiente
columnas_ambiente = []
keywords_ambiente = ['AMBIENTE', 'AMBIENTAL', 'MEDIO', 'CLIMA', 'CLIMATICO', 'P30', 'P31', 'P32']
for col in df.columns:
    if any(keyword in col.upper() for keyword in keywords_ambiente):
        columnas_ambiente.append(col)

print(f"\n   Columnas potenciales de interés en ambiente:")
if columnas_ambiente:
    for col in columnas_ambiente[:10]:  # Mostrar primeras 10
        print(f"   - {col}")
else:
    print("   No se encontraron columnas obvias. Revisar codebook.")

# Buscar columnas de redes sociales/uso
columnas_redes = []
keywords_redes = ['REDES', 'SOCIAL', 'FACEBOOK', 'TWITTER', 'INSTAGRAM', 'P28', 'P29']
for col in df.columns:
    if any(keyword in col.upper() for keyword in keywords_redes):
        columnas_redes.append(col)

print(f"\n   Columnas potenciales de uso de redes sociales:")
if columnas_redes:
    for col in columnas_redes[:15]:  # Mostrar primeras 15
        print(f"   - {col}")
else:
    print("   Revisar codebook para identificar columnas de uso de redes.")

# Analizar valores de confianza en medios
print("\n3. Análisis de valores en columnas de confianza en medios:")

if columnas_medios:
    for col in columnas_medios:
        valores_unicos = sorted(df[col].dropna().unique())[:20]  # Primeros 20 valores únicos
        print(f"\n   {col}:")
        print(f"   - Valores únicos (muestra): {valores_unicos}")
        print(f"   - No nulos: {df[col].notna().sum()} de {len(df)}")
        print(f"   - Valores inválidos típicos: {df[col].isin([-1, -2, -3, -5, 96, 97, 98, 99]).sum()}")

# Crear dataset preparado
print("\n4. Preparando dataset para Power BI...")

# Merge con country codes
df_prepared = df.copy()
df_prepared = df_prepared.merge(
    country_codes, 
    left_on='IDENPA', 
    right_on='Country Code', 
    how='left'
)

# Crear columnas calculadas limpias
print("\n5. Creando columnas limpias...")

# Sexo con etiquetas
df_prepared['Sexo_Labels'] = df_prepared['SEXO'].map({1: 'Hombre', 2: 'Mujer'})

# Grupos de edad
df_prepared['Grupo_Edad'] = pd.cut(
    df_prepared['EDAD'],
    bins=[0, 25, 35, 45, 55, 65, 100],
    labels=['16-25', '26-35', '36-45', '46-55', '56-65', '66+']
)

# Limpiar confianza en medios (reemplazar valores inválidos con NaN)
valores_invalidos = [-1, -2, -3, -5, 96, 97, 98, 99]

if 'P23STM.1' in df_prepared.columns:
    df_prepared['Confianza_TV_Limpia'] = df_prepared['P23STM.1'].replace(valores_invalidos, np.nan)
    
if 'P23STM.2' in df_prepared.columns:
    df_prepared['Confianza_Redes_Limpia'] = df_prepared['P23STM.2'].replace(valores_invalidos, np.nan)
    
if 'P23STM.3' in df_prepared.columns:
    df_prepared['Confianza_Otro_Limpia'] = df_prepared['P23STM.3'].replace(valores_invalidos, np.nan)

# Limpiar años de estudio
if 'REEDUC.3' in df_prepared.columns:
    df_prepared['Anos_Estudio_Limpio'] = df_prepared['REEDUC.3'].replace(valores_invalidos, np.nan)

# Seleccionar columnas relevantes para Power BI
columnas_exportar = [
    'IDENPA',
    'Country Name',
    'EDAD',
    'Grupo_Edad',
    'SEXO',
    'Sexo_Labels',
    'REEDUC.3',
    'Anos_Estudio_Limpio'
]

# Agregar columnas de medios si existen
if 'P23STM.1' in df_prepared.columns:
    columnas_exportar.extend(['P23STM.1', 'Confianza_TV_Limpia'])
if 'P23STM.2' in df_prepared.columns:
    columnas_exportar.extend(['P23STM.2', 'Confianza_Redes_Limpia'])
if 'P23STM.3' in df_prepared.columns:
    columnas_exportar.extend(['P23STM.3', 'Confianza_Otro_Limpia'])

# Agregar columnas de ambiente si se encontraron
if columnas_ambiente:
    columnas_exportar.extend(columnas_ambiente[:5])  # Agregar primeras 5

# Agregar columnas de redes si se encontraron
if columnas_redes:
    columnas_exportar.extend(columnas_redes[:10])  # Agregar primeras 10

# Filtrar solo columnas que existen
columnas_exportar = [col for col in columnas_exportar if col in df_prepared.columns]

print(f"\n   Columnas seleccionadas para exportar: {len(columnas_exportar)}")
print(f"   - Filtros: {len([c for c in columnas_exportar if c in ['IDENPA', 'Country Name', 'EDAD', 'Grupo_Edad', 'SEXO', 'Sexo_Labels', 'REEDUC.3', 'Anos_Estudio_Limpio']])}")
print(f"   - Medios: {len([c for c in columnas_exportar if 'P23STM' in c or 'Confianza' in c])}")
print(f"   - Otras: {len(columnas_exportar) - len([c for c in columnas_exportar if any(x in c for x in ['IDENPA', 'Country', 'EDAD', 'Grupo', 'SEXO', 'REEDUC', 'P23STM', 'Confianza'])])}")

# Exportar dataset preparado
output_file = '../data/Latinobarometro_2024_PowerBI.csv'
print(f"\n6. Exportando dataset preparado a {output_file}...")

df_export = df_prepared[columnas_exportar].copy()
df_export.to_csv(output_file, index=False, encoding='utf-8', sep=';')

print(f"   ✓ Dataset exportado: {df_export.shape[0]} filas, {df_export.shape[1]} columnas")

# Crear resumen
print("\n7. Generando resumen de columnas...")
resumen = pd.DataFrame({
    'Columna': columnas_exportar,
    'Tipo': [str(df_export[col].dtype) for col in columnas_exportar],
    'No_Nulos': [df_export[col].notna().sum() for col in columnas_exportar],
    'Valores_Únicos': [df_export[col].nunique() for col in columnas_exportar]
})

resumen_file = '../data/Resumen_Columnas_PowerBI.csv'
resumen.to_csv(resumen_file, index=False, encoding='utf-8', sep=';')
print(f"   ✓ Resumen exportado a {resumen_file}")

# Recomendaciones
print("\n" + "="*60)
print("RECOMENDACIONES PARA POWER BI:")
print("="*60)
print("\n1. IMPORTAR:")
print(f"   - {output_file} (dataset principal preparado)")
print(f"   - ../data/country_codes.csv (ya está en el dataset principal)")

print("\n2. RELACIONES:")
print("   - IDENPA → Country Code (si cargas country_codes por separado)")

print("\n3. FILTROS A CREAR:")
print("   - Grupo_Edad (segmentador)")
print("   - Country Name (segmentador)")
print("   - Sexo_Labels (segmentador)")
print("   - Anos_Estudio_Limpio (segmentador numérico)")

print("\n4. MEDIDAS DAX SUGERIDAS:")
print("   - Promedio_Confianza_Redes = AVERAGE(Confianza_Redes_Limpia)")
print("   - Promedio_Confianza_TV = AVERAGE(Confianza_TV_Limpia)")

print("\n5. PRÓXIMOS PASOS:")
print("   - Identificar columna de 'interés en ambiente' en el codebook")
print("   - Identificar columnas de 'uso de redes sociales'")
print("   - Seguir la guía en POWERBI_GUIDE.md")

print("\n" + "="*60)
print("¡Preparación completada!")
print("="*60)


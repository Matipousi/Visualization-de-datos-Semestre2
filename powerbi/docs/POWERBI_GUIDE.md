# Guía para Dashboard Power BI - Latinobarómetro 2024

## Parte 2: Visualización en Power BI

### Paso 1: Carga de Datos

1. Abre Power BI Desktop
2. Ve a "Obtener datos" → "Archivo" → "Texto/CSV"
3. Selecciona `Latinobarometro_2024.csv`
   - Separador: punto y coma (;)
   - Codificación: UTF-8
4. Carga también `country_codes.csv` de la misma manera

### Paso 2: Modelo en Estrella

1. **Tabla de Hechos**: `Latinobarometro_2024`
   - Contiene todas las métricas y respuestas individuales

2. **Tabla Dimensión**: `country_codes`
   - Relación: `IDENPA` (tabla de hechos) → `Country Code` (dimensión)
   - Tipo: Uno a muchos (Many-to-one)
   - Nombre de relación: "País"

### Paso 3: Preparación de Columnas Necesarias

#### Columnas para Filtros:
- **Edad**: `EDAD` (numérica)
- **País**: Relación con `country_codes` → `Country Name`
- **Sexo**: `SEXO` (1=Hombre, 2=Mujer) - Crear columna calculada para etiquetas
- **Nivel Educativo**: `REEDUC.3` (años de estudio alcanzados)

#### Columnas para Visualizaciones:

**Hoja 1 - Confianza en Medios:**
- `P23STM.2` - Confianza en Redes Sociales
- `P23STM.1` - Confianza en TV (o radio/diario según disponibilidad)
- `P23STM.3` - Otro medio para comparar

**Hoja 2 - Interés en Ambiente:**
- Buscar columna relacionada con "interés en medio ambiente" (puede estar en P30, P31, o similar)

**Hoja 3 - Redes Sociales:**
- `P23STM.2` - Confianza en Redes Sociales
- Columnas sobre uso de redes sociales (buscar en sección P28-P29)

### Paso 4: Columnas Calculadas Necesarias

#### En la tabla Latinobarometro_2024:

```DAX
Sexo_Labels = 
SWITCH(
    TRUE(),
    Latinobarometro_2024[SEXO] = 1, "Hombre",
    Latinobarometro_2024[SEXO] = 2, "Mujer",
    "No especificado"
)

Grupo_Edad = 
SWITCH(
    TRUE(),
    Latinobarometro_2024[EDAD] <= 25, "16-25",
    Latinobarometro_2024[EDAD] <= 35, "26-35",
    Latinobarometro_2024[EDAD] <= 45, "36-45",
    Latinobarometro_2024[EDAD] <= 55, "46-55",
    Latinobarometro_2024[EDAD] <= 65, "56-65",
    "66+"
)

Confianza_Redes_Limpia = 
IF(
    Latinobarometro_2024[P23STM.2] IN {-1, -2, -3, -5, 96, 97, 98, 99},
    BLANK(),
    Latinobarometro_2024[P23STM.2]
)

Confianza_TV_Limpia = 
IF(
    Latinobarometro_2024[P23STM.1] IN {-1, -2, -3, -5, 96, 97, 98, 99},
    BLANK(),
    Latinobarometro_2024[P23STM.1]
)

Anos_Estudio_Limpio = 
IF(
    Latinobarometro_2024[REEDUC.3] IN {-1, -2, -3, -5, 96, 97, 98, 99},
    BLANK(),
    Latinobarometro_2024[REEDUC.3]
)
```

### Paso 5: Medidas DAX

#### Medidas Generales:

```DAX
Promedio_Confianza_Redes = 
AVERAGE(Latinobarometro_2024[Confianza_Redes_Limpia])

Promedio_Confianza_TV = 
AVERAGE(Latinobarometro_2024[Confianza_TV_Limpia])

Conteo_Respuestas = 
COUNTROWS(Latinobarometro_2024)
```

#### Para Hoja 1 - Confianza en Medios:

```DAX
Promedio_Confianza_Redes_por_Pais = 
CALCULATE(
    [Promedio_Confianza_Redes],
    ALLSELECTED(Latinobarometro_2024)
)

Promedio_Confianza_TV_por_Pais = 
CALCULATE(
    [Promedio_Confianza_TV],
    ALLSELECTED(Latinobarometro_2024)
)
```

#### Para Hoja 2 - Interés en Ambiente:

```DAX
Promedio_Interes_Ambiente = 
VAR Interes_Limpio = 
    IF(
        Latinobarometro_2024[COLUMNA_AMBIENTE] IN {-1, -2, -3, -5, 96, 97, 98, 99},
        BLANK(),
        Latinobarometro_2024[COLUMNA_AMBIENTE]
    )
RETURN
    AVERAGE(Interes_Limpio)

Promedio_Interes_Ambiente_por_Pais = 
CALCULATE(
    [Promedio_Interes_Ambiente],
    ALLSELECTED(Latinobarometro_2024)
)
```

### Paso 6: Configuración de Hojas

#### Hoja 1: "Confianza_en medios"

1. **Filtros (Slicers):**
   - Grupo de Edad (segmentador)
   - País (segmentador)
   - Sexo (segmentador)
   - Años de Estudio (segmentador numérico o agrupado)

2. **Visualización Principal:**
   - Tipo: Gráfico de columnas agrupadas o gráfico de líneas
   - Eje X: País
   - Valores: Promedio_Confianza_Redes_por_Pais, Promedio_Confianza_TV_por_Pais
   - Permite comparar confianza en redes sociales vs TV entre países

#### Hoja 2: "Interés en ambiente"

1. **Filtros (mismos que Hoja 1)**

2. **Gráfico de Comparación:**
   - Tipo: Gráfico de columnas o barras
   - Eje: País
   - Valor: Promedio_Interes_Ambiente_por_Pais

3. **Mapa Coroplético:**
   - Tipo: Mapa (Map visual)
   - Ubicación: country_codes[Country Name] o código ISO
   - Color: Promedio_Interes_Ambiente_por_Pais
   - Formato de color: Escala verde (más verde = mayor interés)

#### Hoja 3: "Redes sociales"

1. **Filtros (mismos que anteriores)**

2. **Visualización 1:** Uso de redes sociales por grupo de edad
   - Tipo: Gráfico de barras apiladas o columnas agrupadas
   - Eje X: Grupo_Edad
   - Valores: Conteo de respuestas por uso de redes

3. **Visualización 2:** Confianza en redes sociales por nivel educativo
   - Tipo: Gráfico de líneas o columnas
   - Eje X: Años de estudio (agrupado)
   - Valor: Promedio_Confianza_Redes

### Paso 7: Hoja de Conclusiones

Crea una nueva hoja llamada "Conclusiones" con:
- Texto descriptivo con al menos 3 observaciones clave
- Puedes incluir imágenes o capturas de las visualizaciones principales
- Formato profesional y claro

### Notas Importantes:

1. **Limpieza de Datos:** Los valores -1, -2, -3, -5, 96, 97, 98, 99 suelen ser códigos de "No sabe/No responde" y deben tratarse como BLANK().

2. **Estética:**
   - Usa paletas de colores consistentes
   - Agrega títulos descriptivos a cada visualización
   - Ajusta formatos de números (decimales)
   - Usa fuentes legibles y tamaños apropiados

3. **Interactividad:**
   - Todos los filtros deben afectar todas las visualizaciones
   - Verifica que las relaciones estén bien configuradas

4. **Rendimiento:**
   - Considera crear columnas calculadas en lugar de medidas cuando sea posible para mejorar rendimiento
   - Usa agregaciones apropiadas

## Próximos Pasos

1. Ejecuta el script `prepare_powerbi_data.py` para identificar todas las columnas relevantes
2. Revisa el código de preparación de datos para limpiar el dataset antes de importar
3. Sigue esta guía paso a paso en Power BI Desktop


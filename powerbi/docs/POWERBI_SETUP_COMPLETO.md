# Setup Completo Power BI - Latinobarómetro 2024

## 📋 Checklist de Preparación

### Paso 1: Importar Datos (5 min)

1. **Abrir Power BI Desktop**
2. **Importar dataset preparado:**
   - Click en "Obtener datos" → "Texto/CSV"
   - Seleccionar: `data/Latinobarometro_2024_PowerBI.csv`
   - Separador: **Punto y coma (;)**
   - Codificación: **UTF-8**
   - Click en "Cargar"

3. **Verificar datos cargados:**
   - Deberías ver 19,214 filas
   - Panel derecho → Verifica que aparezcan las columnas preparadas

### Paso 2: Configurar Modelo de Datos (10 min)

**NOTA:** El dataset ya incluye `Country Name` fusionado, así que NO necesitas cargar `country_codes.csv` por separado a menos que quieras usarlo como dimensión independiente.

Si quieres modelo en estrella estricto:
1. Cargar también `country_codes.csv`
2. Crear relación: `IDENPA` → `Country Code` (Many-to-One)
3. Usar `Country Name` de la tabla de dimensión en visualizaciones

### Paso 3: Crear Columnas Calculadas Necesarias (15 min)

En el panel "Datos", selecciona la tabla y crea estas columnas calculadas:

#### A. Grupo de Años de Estudio (para filtro más útil):

```DAX
Grupo_Educativo = 
SWITCH(
    TRUE(),
    Latinobarometro_2024_PowerBI[Anos_Estudio_Limpio] <= 6, "Primaria (0-6 años)",
    Latinobarometro_2024_PowerBI[Anos_Estudio_Limpio] <= 12, "Secundaria (7-12 años)",
    Latinobarometro_2024_PowerBI[Anos_Estudio_Limpio] > 12, "Universidad (13+ años)",
    BLANK()
)
```

#### B. Identificar columna de interés en ambiente:

**IMPORTANTE:** Necesitas revisar el codebook para identificar cuál de las columnas P30ST.A-E o P31ST corresponde a "interés en medio ambiente". Por ahora, asumimos que es una de ellas. Crea una medida temporal:

```DAX
Interes_Ambiente_Limpio = 
// Reemplaza 'P31ST' con la columna correcta del codebook
VAR Valor = Latinobarometro_2024_PowerBI[P31ST]  // O P30ST.A, P30ST.B, etc.
VAR Limpio = IF(
    Valor IN {-1, -2, -3, -5, 96, 97, 98, 99},
    BLANK(),
    Valor
)
RETURN Limpio
```

### Paso 4: Crear Medidas DAX (20 min)

#### Medidas Generales:

```DAX
Total_Respuestas = COUNTROWS(Latinobarometro_2024_PowerBI)

Promedio_Confianza_Redes = 
AVERAGE(Latinobarometro_2024_PowerBI[Confianza_Redes_Limpia])

Promedio_Confianza_TV = 
AVERAGE(Latinobarometro_2024_PowerBI[Confianza_TV_Limpia])

Promedio_Confianza_Otro = 
AVERAGE(Latinobarometro_2024_PowerBI[Confianza_Otro_Limpia])
```

#### Medidas para Comparaciones por País:

```DAX
Promedio_Confianza_Redes_por_Pais = 
CALCULATE(
    [Promedio_Confianza_Redes],
    ALLSELECTED(Latinobarometro_2024_PowerBI)
)

Promedio_Confianza_TV_por_Pais = 
CALCULATE(
    [Promedio_Confianza_TV],
    ALLSELECTED(Latinobarometro_2024_PowerBI)
)

Promedio_Interes_Ambiente_por_Pais = 
CALCULATE(
    AVERAGE(Latinobarometro_2024_PowerBI[Interes_Ambiente_Limpio]),
    ALLSELECTED(Latinobarometro_2024_PowerBI)
)
```

#### Medidas para Conteos (Redes Sociales):

```DAX
Usa_Redes_Sociales = 
CALCULATE(
    COUNTROWS(Latinobarometro_2024_PowerBI),
    Latinobarometro_2024_PowerBI[P28ST] IN {1, 2}  // Ajustar según codebook
)

Porcentaje_Usa_Redes = 
DIVIDE(
    [Usa_Redes_Sociales],
    [Total_Respuestas],
    0
) * 100
```

---

## 🎨 HOJA 1: "Confianza_en medios"

### Filtros (Segmentadores):

1. **Grupo de Edad:**
   - Visualización: Segmentador
   - Campo: `Grupo_Edad`
   - Selección: Múltiple

2. **País:**
   - Visualización: Segmentador
   - Campo: `Country Name`
   - Selección: Múltiple

3. **Sexo:**
   - Visualización: Segmentador
   - Campo: `Sexo_Labels`
   - Selección: Múltiple

4. **Años de Estudio:**
   - Visualización: Segmentador numérico (o agrupado)
   - Campo: `Grupo_Educativo` (recomendado) o `Anos_Estudio_Limpio`
   - Selección: Entre (rango)

### Visualización Principal:

**Gráfico de Comparación: Confianza en Redes vs. TV**

- Tipo: **Gráfico de columnas agrupadas** o **Gráfico de líneas**
- Eje X: `Country Name`
- Valores:
  - `Promedio_Confianza_Redes_por_Pais`
  - `Promedio_Confianza_TV_por_Pais`
- Leyenda: "Tipo de Medio" (crear columna calculada si es necesario)
- Formato:
  - Título: "Comparación de Confianza en Redes Sociales vs. TV por País"
  - Colores diferenciados para cada medio

**Alternativa - Gráfico de Líneas:**
- Eje X: País
- Línea 1: Confianza Redes
- Línea 2: Confianza TV
- Permite ver tendencias y diferencias más claramente

---

## 🌍 HOJA 2: "Interés en ambiente"

### Filtros:
- **Mismos que Hoja 1** (puedes copiar los segmentadores)

### Visualización 1: Comparación entre Países

- Tipo: **Gráfico de barras horizontales** o **Columnas**
- Eje Y (si barras): `Country Name`
- Eje X (si columnas): `Country Name`
- Valor: `Promedio_Interes_Ambiente_por_Pais`
- Ordenar por: Valor (descendente)
- Formato:
  - Título: "Interés Promedio en Medio Ambiente por País"
  - Color: Escala verde (más verde = mayor interés)
  - Formato de número: 1 decimal

### Visualización 2: Mapa Coroplético

- Tipo: **Mapa** (Map visual)
- Ubicación: `Country Name`
  - **NOTA:** Si el mapa no reconoce nombres, necesitarás:
    - Agregar columna ISO de países (código de 3 letras)
    - O usar latitud/longitud
    - Ver sección "Preparar para Mapa" más abajo
- Color: `Promedio_Interes_Ambiente_por_Pais`
- Formato de color:
  - Tipo: Escala de colores
  - Mínimo: Verde claro
  - Máximo: Verde oscuro
  - Revertir si es necesario
- Título: "Interés en Medio Ambiente por País - Mapa"

**Preparar para Mapa (si es necesario):**
```DAX
// Crear tabla de códigos ISO si no los tienes
// O usar coordenadas de países
```

---

## 📱 HOJA 3: "Redes sociales"

### Filtros:
- **Mismos que anteriores**

### Visualización 1: Uso de Redes Sociales por Grupo de Edad

- Tipo: **Gráfico de barras apiladas** o **Columnas agrupadas**
- Eje X: `Grupo_Edad`
- Valores: 
  - Usa `P28ST` o `P29ST.A-H` según corresponda
  - Crear medidas de conteo por categoría
- Título: "Uso de Redes Sociales por Grupo de Edad"

**Medidas sugeridas para esta visualización:**
```DAX
Usa_Redes_Diariamente = 
CALCULATE(
    COUNTROWS(Latinobarometro_2024_PowerBI),
    Latinobarometro_2024_PowerBI[P28ST] = 1  // Verificar valor en codebook
)

Usa_Redes_Semanalmente = 
CALCULATE(
    COUNTROWS(Latinobarometro_2024_PowerBI),
    Latinobarometro_2024_PowerBI[P28ST] = 2  // Verificar valor
)
```

### Visualización 2: Confianza en Redes Sociales por Nivel Educativo

- Tipo: **Gráfico de líneas** o **Columnas agrupadas**
- Eje X: `Grupo_Educativo`
- Valor: `Promedio_Confianza_Redes`
- Título: "Confianza en Redes Sociales según Nivel Educativo"

### Visualización 3 (Opcional): Distribución de Uso

- Tipo: **Gráfico de anillo** o **Pie**
- Valores: Distribución de `P28ST` o `P29ST.A-H`
- Título: "Distribución del Uso de Redes Sociales"

---

## 📊 HOJA 4: "Conclusiones"

Crea una hoja con texto y visualizaciones clave:

1. **Texto descriptivo** con al menos 3 observaciones/conclusiones:
   - Observación 1: Sobre confianza en medios
   - Observación 2: Sobre interés en ambiente
   - Observación 3: Sobre uso de redes sociales

2. **Capturas o miniaturas** de visualizaciones principales

3. **Formato profesional:**
   - Títulos claros
   - Numeración de observaciones
   - Fondo limpio

---

## 🎨 MEJORAS DE ESTÉTICA

### Temas y Colores:
1. Ve a "Vista" → "Temas"
2. Elige un tema profesional o personaliza
3. Usa paleta consistente en todas las hojas

### Formato de Números:
1. Selecciona cada medida
2. Formato → Decimales → 1-2 decimales según necesidad

### Títulos y Etiquetas:
- Títulos descriptivos en todas las visualizaciones
- Ejes con nombres claros
- Leyendas visibles

### Interactividad:
1. Ve a "Vista" → "Modo de edición" → "Interacciones"
2. Configura que todos los filtros afecten todas las visualizaciones
3. Prueba la interactividad haciendo clic en segmentadores

---

## ✅ CHECKLIST FINAL

Antes de entregar, verifica:

- [ ] Todos los filtros funcionan correctamente
- [ ] Las 3 hojas principales tienen las visualizaciones requeridas
- [ ] Hoja de conclusiones tiene al menos 3 observaciones
- [ ] Mapa coroplético muestra correctamente los países
- [ ] Todas las medidas DAX funcionan sin errores
- [ ] Colores y formato son consistentes
- [ ] Los títulos son descriptivos
- [ ] El modelo de datos está correctamente configurado

---

## 🔍 IDENTIFICAR COLUMNAS DEL CODEBOOK

**IMPORTANTE:** Necesitas revisar estos archivos para identificar exactamente:
1. `Codebook Latinobarómetro.xlsx` - Para nombres de columnas
2. `Latinobarometro_2024_Cuestionario_esp.pdf` - Para entender las preguntas

**Columnas a identificar:**
- Cuál de P30ST.A-E o P31ST es "interés en medio ambiente"
- Qué significan los valores en P28ST, P29ST para uso de redes
- Qué representan P23STM.1, P23STM.2, P23STM.3 exactamente

---

## 💡 TIPS ADICIONALES

1. **Rendimiento:**
   - Si el reporte es lento, considera reducir columnas importadas
   - Usa columnas calculadas en lugar de medidas cuando sea posible

2. **Reutilizar filtros:**
   - Crea los segmentadores una vez y cópialos a otras hojas

3. **Bookmarks:**
   - Crea marcadores para estados específicos del dashboard

4. **Tooltips:**
   - Agrega información adicional que aparezca al pasar el mouse

---

¡Buena suerte con tu dashboard! 🚀


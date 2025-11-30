# ⚡ Quick Start - Power BI Dashboard

## 🎯 Resumen del Proyecto

Necesitas crear un dashboard en Power BI con 4 hojas según los requisitos del trabajo final.

## ✅ Lo que Ya Está Listo

1. ✅ Dataset preparado: `powerbi/data/Latinobarometro_2024_PowerBI.csv` (se genera ejecutando el script)
2. ✅ Columnas limpias y calculadas ya incluidas
3. ✅ Guías completas de setup
4. ✅ Fórmulas DAX listas para copiar

## 🚀 Pasos para Empezar (15 minutos)

### 1. Importar Datos (2 min)
- Abre Power BI Desktop
- "Obtener datos" → "Texto/CSV"
- Selecciona: `powerbi/data/Latinobarometro_2024_PowerBI.csv`
- Separador: **Punto y coma (;)**
- Click "Cargar"

### 2. Verificar Columnas Preparadas (1 min)
En el panel de datos, deberías ver:
- ✅ `Country Name` (país)
- ✅ `EDAD`, `Grupo_Edad`
- ✅ `SEXO`, `Sexo_Labels`
- ✅ `Anos_Estudio_Limpio`
- ✅ `Confianza_Redes_Limpia`
- ✅ `Confianza_TV_Limpia`
- ✅ Columnas P28ST, P29ST, P30ST, P31ST

### 3. Crear Columnas Calculadas Básicas (5 min)

**Grupo Educativo:**
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

**Interés en Ambiente (AJUSTAR según codebook):**
```DAX
Interes_Ambiente_Limpio = 
VAR Valor = Latinobarometro_2024_PowerBI[P31ST]  // Verificar en codebook
VAR Limpio = IF(
    Valor IN {-1, -2, -3, -5, 96, 97, 98, 99},
    BLANK(),
    Valor
)
RETURN Limpio
```

### 4. Crear Medidas DAX Esenciales (7 min)

**Copia estas medidas desde `DAX_FORMULAS_REFERENCE.md`:**
- `Promedio_Confianza_Redes`
- `Promedio_Confianza_TV`
- `Promedio_Confianza_Redes_por_Pais`
- `Promedio_Confianza_TV_por_Pais`
- `Promedio_Interes_Ambiente_por_Pais`

## 📋 Columnas Identificadas vs. Por Verificar

### ✅ Confirmadas:
- **Confianza Redes Sociales**: `Confianza_Redes_Limpia` (de P23STM.2)
- **Confianza TV**: `Confianza_TV_Limpia` (de P23STM.1)
- **Uso de Redes**: `P28ST` (valores 1,2,3)
- **Más Redes**: `P29ST.A-H` (varios aspectos)

### ⚠️ Verificar en Codebook:
- **Interés en Ambiente**: Revisar si es `P31ST` o alguna de `P30ST.A-E`
  - P31ST tiene valores 1-4 (posible escala de interés)
  - P30ST.A-E tienen valores 1-4 (posibles temas diferentes)

**Cómo verificar:**
1. Abre `data/Codebook Latinobarómetro.xlsx`
2. Busca "medio ambiente" o "ambiente"
3. Identifica el código de columna
4. Actualiza las fórmulas DAX con el nombre correcto

## 🎨 Estructura de Hojas

### Hoja 1: "Confianza_en medios"
**Filtros:**
- Grupo_Edad (segmentador)
- Country Name (segmentador)
- Sexo_Labels (segmentador)
- Grupo_Educativo (segmentador)

**Visualización:**
- Gráfico de columnas agrupadas
- Eje X: Country Name
- Valores: Promedio_Confianza_Redes_por_Pais, Promedio_Confianza_TV_por_Pais

### Hoja 2: "Interés en ambiente"
**Filtros:** Mismos

**Visualizaciones:**
1. Gráfico de barras: Country Name vs. Promedio_Interes_Ambiente_por_Pais
2. Mapa coroplético: Country Name + Promedio_Interes_Ambiente_por_Pais (escala verde)

### Hoja 3: "Redes sociales"
**Filtros:** Mismos

**Visualizaciones (mínimo 2):**
1. Uso de redes por grupo de edad (barras con P28ST)
2. Confianza en redes por nivel educativo (líneas o columnas)

### Hoja 4: "Conclusiones"
- Texto con al menos 3 observaciones/conclusiones

## 📚 Documentos de Referencia

1. **Setup Completo**: `docs/POWERBI_SETUP_COMPLETO.md` - Instrucciones detalladas
2. **Fórmulas DAX**: `docs/DAX_FORMULAS_REFERENCE.md` - Todas las fórmulas
3. **Guía General**: `docs/POWERBI_GUIDE.md` - Conceptos y contexto

## 💡 Tips Rápidos

1. **Copiar Filtros:** Crea los segmentadores en la primera hoja, luego cópialos (Ctrl+C, Ctrl+V) a otras hojas
2. **Nombres de Tablas:** Si Power BI cambió el nombre de tu tabla, actualiza todas las fórmulas DAX
3. **Mapa:** Si no muestra países, necesitarás códigos ISO. Considera usar nombres en inglés o agregar coordenadas.
4. **Valores Inválidos:** Ya están limpiados en las columnas "_Limpia"

## ⏱️ Tiempo Estimado

- Importar y configurar: **15 min**
- Crear Hoja 1: **20 min**
- Crear Hoja 2: **25 min** (mapa puede tomar más tiempo)
- Crear Hoja 3: **20 min**
- Crear Hoja 4: **15 min**
- Ajustes finales: **15 min**

**Total: ~2 horas**

## 🆘 Ayuda Rápida

**Error en importación:**
- Verifica separador: punto y coma (;)
- Verifica codificación: UTF-8

**Medidas DAX no funcionan:**
- Verifica nombre exacto de tabla y columnas
- Usa corchetes [ ] alrededor de nombres

**Filtros no afectan visualizaciones:**
- Ve a "Vista" → "Modo de edición" → "Interacciones"
- Configura que filtros afecten todas las visualizaciones

---

**¡Empieza con `docs/POWERBI_SETUP_COMPLETO.md` para instrucciones detalladas!** 🚀


# 🎯 Guía Completa para Dashboard Power BI - Latinobarómetro 2024

Esta carpeta contiene todos los recursos necesarios para crear el dashboard de Power BI según los requisitos del trabajo final.

## 📁 Estructura de Archivos

```
powerbi/
├── docs/
│   ├── POWERBI_SETUP_COMPLETO.md    - Guía paso a paso completa
│   ├── POWERBI_GUIDE.md              - Guía general y conceptos
│   ├── DAX_FORMULAS_REFERENCE.md     - Todas las fórmulas DAX
│   ├── QUICK_START_POWERBI.md        - Inicio rápido
│   └── README_POWERBI.md             - Este archivo (índice)
├── scripts/
│   ├── prepare_powerbi_data.py       - Prepara dataset optimizado
│   └── explore_columns.py            - Explora columnas del dataset
└── data/
    ├── Latinobarometro_2024_PowerBI.csv      - Dataset preparado (se genera)
    └── Resumen_Columnas_PowerBI.csv          - Resumen de columnas (se genera)
```

**Nota:** Los datos originales están en `../data/` (un nivel arriba)

## 🚀 Inicio Rápido

### Paso 1: Ejecutar Script de Preparación
```bash
cd powerbi/scripts
python prepare_powerbi_data.py
```

Esto genera:
- Dataset optimizado: `powerbi/data/Latinobarometro_2024_PowerBI.csv`
- Resumen de columnas: `powerbi/data/Resumen_Columnas_PowerBI.csv`

### Paso 2: Abrir Power BI Desktop

1. Abre Power BI Desktop
2. Click en "Obtener datos" → "Texto/CSV"
3. Selecciona: `powerbi/data/Latinobarometro_2024_PowerBI.csv`
4. Separador: **Punto y coma (;)**
5. Codificación: **UTF-8**
6. Click en "Cargar"

### Paso 3: Seguir la Guía Completa

Abre **`docs/POWERBI_SETUP_COMPLETO.md`** y sigue las instrucciones paso a paso.

## 📋 Estructura del Dashboard Requerido

### Hoja 1: "Confianza_en medios"
- ✅ Filtros: Edad, País, Sexo, Nivel Educativo
- ✅ Comparación: Confianza en Redes Sociales vs. otro medio (TV) entre países

### Hoja 2: "Interés en ambiente"
- ✅ Filtros: Mismos que Hoja 1
- ✅ Comparación de interés en ambiente entre países
- ✅ Mapa coroplético con color verde (más verde = mayor interés)

### Hoja 3: "Redes sociales"
- ✅ Filtros: Mismos que anteriores
- ✅ Al menos 2 visualizaciones sobre uso de redes sociales

### Hoja 4: "Conclusiones"
- ✅ Al menos 3 observaciones/conclusiones del análisis

## 🔍 Identificar Columnas del Codebook

**IMPORTANTE:** Antes de crear todas las visualizaciones, necesitas:

1. Abrir `data/Codebook Latinobarómetro.xlsx`
2. Buscar:
   - **Interés en medio ambiente** → Identificar columna (probablemente P30ST.A-E o P31ST)
   - **Uso de redes sociales** → Identificar columnas (P28ST, P29ST.A-H)
   - **Confianza en medios** → Verificar significado de P23STM.1, P23STM.2, P23STM.3

3. Ejecutar script exploratorio:
```bash
cd powerbi/scripts
python explore_columns.py
```

Este script te mostrará los valores en cada columna para ayudarte a identificar cuál usar.

## 📊 Columnas Ya Identificadas

### ✅ Confirmadas:
- **Confianza en TV**: `P23STM.1`
- **Confianza en Redes Sociales**: `P23STM.2`
- **Confianza en Otro Medio**: `P23STM.3`
- **Edad**: `EDAD`
- **Sexo**: `SEXO` (1=Hombre, 2=Mujer)
- **Años de Estudio**: `REEDUC.3`
- **País**: `Country Name` (ya fusionado)

### ⚠️ Por Verificar en Codebook:
- **Interés en ambiente**: P30ST.A, P30ST.B, P30ST.C, P30ST.D, P30ST.E, o P31ST
- **Uso de redes sociales**: P28ST, P29ST.A-H

## 🛠️ Herramientas y Recursos

### Fórmulas DAX:
Consulta **`docs/DAX_FORMULAS_REFERENCE.md`** para copiar y pegar fórmulas listas.

### Configuración Detallada:
Sigue **`docs/POWERBI_SETUP_COMPLETO.md`** para instrucciones paso a paso de cada visualización.

## ✅ Checklist de Trabajo

- [ ] Importar datos a Power BI
- [ ] Crear columnas calculadas necesarias
- [ ] Crear medidas DAX
- [ ] Configurar modelo de datos (relaciones)
- [ ] Crear Hoja 1: Confianza_en medios
  - [ ] Filtros (4 segmentadores)
  - [ ] Gráfico de comparación
- [ ] Crear Hoja 2: Interés en ambiente
  - [ ] Filtros
  - [ ] Gráfico de comparación
  - [ ] Mapa coroplético
- [ ] Crear Hoja 3: Redes sociales
  - [ ] Filtros
  - [ ] Visualización 1
  - [ ] Visualización 2
- [ ] Crear Hoja 4: Conclusiones
  - [ ] Al menos 3 observaciones
- [ ] Revisar estética y formato
- [ ] Probar interactividad de filtros
- [ ] Revisar checklist final en guía

## 💡 Tips Importantes

1. **Valores Inválidos**: Los valores -1, -2, -3, -5, 96, 97, 98, 99 representan "No sabe/No responde" y deben tratarse como BLANK() en DAX.

2. **Rendimiento**: Si el reporte es lento, considera reducir el número de columnas importadas o usar agregaciones.

3. **Filtros**: Crea los segmentadores una vez y cópialos entre hojas para consistencia.

4. **Mapa**: Si el mapa no reconoce nombres de países, necesitarás códigos ISO o coordenadas. Puedes agregar esto desde country_codes si es necesario.

5. **DAX**: Usa `ALLSELECTED()` cuando quieras que las medidas respeten los filtros de los segmentadores.

## 📚 Recursos Adicionales

- **Codebook**: `data/Codebook Latinobarómetro.xlsx`
- **Cuestionario**: `data/Latinobarometro_2024_Cuestionario_esp.pdf`
- **Instrucciones originales**: `data/Trabajo final_2doSem_2025_instrucción.pdf`

## 🆘 Solución de Problemas

### Error al importar CSV:
- Verifica que el separador sea punto y coma (;)
- Verifica codificación UTF-8

### Medidas DAX no funcionan:
- Verifica que los nombres de tablas y columnas sean exactos
- Asegúrate de usar `[` y `]` alrededor de nombres con espacios

### Mapas no muestran países:
- Necesitas códigos ISO o coordenadas
- Considera usar nombres de países en inglés o agregar columna de códigos

### Filtros no funcionan:
- Verifica que los filtros estén configurados como "Básico" o "Avanzado"
- Asegúrate de que las relaciones estén bien configuradas

## 📞 Próximos Pasos

1. **Ahora mismo:**
   - ✅ Datos ya preparados
   - ⏭️ Abrir Power BI y seguir `POWERBI_SETUP_COMPLETO.md`

2. **Esta sesión:**
   - Importar datos
   - Crear columnas y medidas DAX básicas
   - Configurar primeras visualizaciones

3. **Siguiente sesión:**
   - Completar todas las hojas
   - Mejorar estética
   - Escribir conclusiones

---

**¡Todo listo para empezar!** 🚀

Abre `POWERBI_SETUP_COMPLETO.md` y comienza a crear tu dashboard.


# 📚 Guía Completa de Archivos - Power BI

Esta guía explica qué contiene cada archivo y cuándo usarlo.

---

## 📁 Estructura

```
powerbi/
├── README.md                    ← Índice principal
├── GUIDE_FOR_GUIDES.md         ← Este archivo (en raíz del repo)
├── docs/                        ← 8 guías diferentes
├── scripts/                     ← 2 scripts Python
└── data/                        ← Datos generados
```

---

## 📄 Archivos Principales (Raíz de `powerbi/`)

### `README.md`
**Propósito:** Índice y punto de entrada  
**Cuándo leer:** Primero que nada  
**Contiene:** Estructura de carpetas, enlaces, inicio rápido básico

---

## 📖 Documentación (`docs/`)

### 1. `QUICK_START_POWERBI.md` ⚡
**Propósito:** Guía de inicio rápido (15 minutos)  
**Cuándo leer:** Si quieres empezar YA sin leer todo  
**Contiene:**
- Pasos rápidos para importar datos
- Columnas ya preparadas
- Medidas DAX esenciales
- Checklist rápido

**Úsalo cuando:** Tengas poco tiempo y quieras resultados rápidos

---

### 2. `POWERBI_CLEANUP_GUIDE.md` 🧹
**Propósito:** Guía para limpiar tu Power BI cuando cargaste el PDF por error  
**Cuándo leer:** SI tienes muchas tablas (Table001-Table024, Page001-007) en Power BI  
**Contiene:**
- Cómo eliminar tablas innecesarias del PDF
- Por qué NO necesitas cargar el PDF
- Cómo empezar correctamente

**Úsalo cuando:** Tengas ese problema de muchas tablas del PDF

---

### 3. `WORKFLOW_RAPIDO.md` ⚡
**Propósito:** Flujo de trabajo visual paso a paso  
**Cuándo leer:** Para entender el proceso completo de principio a fin  
**Contiene:**
- Diagrama visual del flujo
- Checklist por etapas
- Tiempos estimados
- Recursos por etapa

**Úsalo cuando:** Quieras una visión general del proceso completo

---

### 4. `COLUMNAS_REFERENCIA.md` 📋
**Propósito:** Referencia rápida de columnas (en lugar de cargar el PDF)  
**Cuándo leer:** Cuando necesites entender qué significa cada columna  
**Contiene:**
- Mapeo de columnas principales
- Valores y sus significados
- Valores inválidos comunes
- Cómo identificar columnas específicas

**Úsalo cuando:** Necesites consultar qué columna usar o qué significa un valor

---

### 5. `POWERBI_SETUP_COMPLETO.md` 📖
**Propósito:** La guía más completa y detallada paso a paso  
**Cuándo leer:** Cuando estés listo para crear el dashboard completo  
**Contiene:**
- Configuración detallada del modelo
- Instrucciones para cada hoja del dashboard
- Configuración de cada visualización
- Tips de estética y formato

**Úsalo cuando:** Estés creando las hojas del dashboard (hoja 1, 2, 3, 4)

---

### 6. `POWERBI_GUIDE.md` 📚
**Propósito:** Guía general y conceptos de Power BI  
**Cuándo leer:** Si quieres entender conceptos generales  
**Contiene:**
- Conceptos básicos
- Estructura del modelo en estrella
- Columnas calculadas vs medidas
- Generalidades

**Úsalo cuando:** Quieras entender mejor los conceptos detrás del dashboard

---

### 7. `DAX_FORMULAS_REFERENCE.md` 📋
**Propósito:** Todas las fórmulas DAX organizadas por categoría  
**Cuándo leer:** Cuando necesites copiar fórmulas DAX  
**Contiene:**
- Columnas calculadas (DAX)
- Medidas básicas
- Medidas por país
- Medidas para redes sociales
- Medidas avanzadas

**Úsalo cuando:** Estés creando medidas o columnas calculadas - copia y pega directamente

---

### 8. `README_POWERBI.md` 📑
**Propósito:** Índice completo de todos los recursos y resumen detallado  
**Cuándo leer:** Para navegar todos los recursos disponibles  
**Contiene:**
- Lista completa de archivos
- Descripción de cada recurso
- Checklist de trabajo
- Solución de problemas

**Úsalo cuando:** Quieras explorar todos los recursos disponibles

---

## 🛠️ Scripts (`scripts/`)

### 1. `prepare_powerbi_data.py` 🐍
**Propósito:** Script de Python que prepara y limpia los datos  
**Cuándo ejecutarlo:** ANTES de importar datos a Power BI  
**Hace:**
- Limpia valores inválidos (-1, -2, -3, etc.)
- Crea columnas calculadas (Grupo_Edad, Sexo_Labels)
- Fusiona códigos de países
- Exporta dataset optimizado
- Genera resumen de columnas

**Genera:**
- `data/Latinobarometro_2024_PowerBI.csv`
- `data/Resumen_Columnas_PowerBI.csv`

**Ejecuta:** `python prepare_powerbi_data.py` (desde la carpeta scripts/)

---

### 2. `explore_columns.py` 🔍
**Propósito:** Script que explora valores en columnas específicas  
**Cuándo ejecutarlo:** Para identificar qué columna usar (ej: interés en ambiente)  
**Hace:**
- Analiza valores en P30ST.A-E, P31ST
- Analiza valores en P28ST, P29ST (redes sociales)
- Muestra distribuciones de valores
- Ayuda a identificar columnas correctas

**Ejecuta:** `python explore_columns.py` (desde la carpeta scripts/)

---

## 📊 Datos (`data/`)

### `Latinobarometro_2024_PowerBI.csv` (Se genera)
**Propósito:** Dataset preparado y optimizado para Power BI  
**Cuándo usarlo:** Para importar en Power BI Desktop  
**Contiene:**
- 19,214 filas de datos
- Columnas limpias (valores inválidos convertidos a NULL)
- Columnas calculadas (Grupo_Edad, Sexo_Labels, etc.)
- Country Name ya fusionado

**Se genera ejecutando:** `scripts/prepare_powerbi_data.py`

---

### `Resumen_Columnas_PowerBI.csv` (Se genera)
**Propósito:** Resumen técnico de las columnas exportadas  
**Cuándo usarlo:** Para referencia técnica (opcional)  
**Contiene:**
- Lista de columnas
- Tipo de datos
- Cantidad de valores no nulos
- Cantidad de valores únicos

**Se genera ejecutando:** `scripts/prepare_powerbi_data.py`

---

## 🗺️ Mapa de Uso Recomendado

### Si eres nuevo y tienes muchas tablas del PDF:
1. `docs/POWERBI_CLEANUP_GUIDE.md` ← Empieza aquí
2. `docs/WORKFLOW_RAPIDO.md` ← Luego esto
3. `docs/QUICK_START_POWERBI.md` ← Para empezar rápido

### Si quieres empezar desde cero:
1. `powerbi/README.md` ← Vista general
2. Ejecuta `powerbi/scripts/prepare_powerbi_data.py`
3. `powerbi/docs/QUICK_START_POWERBI.md` ← Inicio rápido
4. `powerbi/docs/POWERBI_SETUP_COMPLETO.md` ← Guía completa

### Si necesitas crear el dashboard:
1. `powerbi/docs/POWERBI_SETUP_COMPLETO.md` ← Guía paso a paso
2. `powerbi/docs/DAX_FORMULAS_REFERENCE.md` ← Fórmulas DAX
3. `powerbi/docs/COLUMNAS_REFERENCIA.md` ← Referencia de columnas

### Si necesitas referencia rápida:
- `powerbi/docs/COLUMNAS_REFERENCIA.md` ← Columnas
- `powerbi/docs/DAX_FORMULAS_REFERENCE.md` ← Fórmulas
- Ejecuta `powerbi/scripts/explore_columns.py` ← Explorar datos

---

## 📋 Resumen Rápido por Archivo

| Archivo | Tipo | Cuándo Usar | Tiempo |
|---------|------|-------------|--------|
| `powerbi/README.md` | Índice | Primero | 2 min |
| `powerbi/docs/QUICK_START_POWERBI.md` | Guía rápida | Inicio rápido | 15 min |
| `powerbi/docs/POWERBI_CLEANUP_GUIDE.md` | Guía | Limpiar tablas PDF | 5 min |
| `powerbi/docs/WORKFLOW_RAPIDO.md` | Flujo | Ver proceso completo | 10 min |
| `powerbi/docs/COLUMNAS_REFERENCIA.md` | Referencia | Consultar columnas | 5 min |
| `powerbi/docs/POWERBI_SETUP_COMPLETO.md` | Guía completa | Crear dashboard | 2-3 horas |
| `powerbi/docs/POWERBI_GUIDE.md` | Conceptos | Entender conceptos | 20 min |
| `powerbi/docs/DAX_FORMULAS_REFERENCE.md` | Referencia | Copiar fórmulas DAX | 10 min |
| `powerbi/docs/README_POWERBI.md` | Índice | Navegar recursos | 10 min |
| `powerbi/scripts/prepare_powerbi_data.py` | Script | Preparar datos | 2 min |
| `powerbi/scripts/explore_columns.py` | Script | Explorar columnas | 2 min |

---

## 💡 Tips de Uso

1. **No necesitas leer todo** - Empieza con `QUICK_START_POWERBI.md`
2. **Ten abiertas las referencias** - `DAX_FORMULAS_REFERENCE.md` y `COLUMNAS_REFERENCIA.md`
3. **Sigue el workflow** - `WORKFLOW_RAPIDO.md` te guía paso a paso
4. **Ejecuta los scripts primero** - Preparan los datos antes de importar

---

## 🔍 Búsqueda Rápida

**¿Cómo limpiar las tablas del PDF?**  
→ `powerbi/docs/POWERBI_CLEANUP_GUIDE.md`

**¿Qué columna usar para interés en ambiente?**  
→ `powerbi/docs/COLUMNAS_REFERENCIA.md` o ejecuta `powerbi/scripts/explore_columns.py`

**¿Cómo crear una medida DAX?**  
→ `powerbi/docs/DAX_FORMULAS_REFERENCE.md`

**¿Cómo crear la hoja 1 del dashboard?**  
→ `powerbi/docs/POWERBI_SETUP_COMPLETO.md`

**¿Dónde empezar?**  
→ `powerbi/docs/QUICK_START_POWERBI.md`

---

**¡Ahora sabes qué archivo usar en cada momento!** 🎯


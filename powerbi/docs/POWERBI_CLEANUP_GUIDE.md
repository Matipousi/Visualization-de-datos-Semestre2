# 🧹 Guía de Limpieza y Configuración Correcta - Power BI

## ❌ Problema Actual

Has cargado el PDF del cuestionario (`Latinobarometro_2024_Cuestionario_esp.pdf`) en Power BI, lo que creó múltiples tablas (Table001-Table024, Page001-Page007, etc.). 

**Esto NO es necesario.** El PDF es solo documentación de referencia, no datos para análisis.

## ✅ Solución: Limpiar y Empezar Correctamente

### Paso 1: Limpiar el Modelo Actual

1. **Eliminar todas las tablas del PDF:**
   - En el panel derecho "Data", busca y elimina todas las tablas que empiezan con:
     - `Table001` hasta `Table024`
     - `Page001` hasta `Page007`
     - `Hoja 1`, `Hoja2` (si existen)
   - **Mantén solo:** `country_codes` (si la necesitas) y tu tabla principal de datos

2. **Cómo eliminar:**
   - Click derecho en cada tabla → "Delete" (Eliminar)
   - O selecciona la tabla y presiona `Delete`

### Paso 2: Cargar Solo los Datos Necesarios

**NO cargues el PDF.** En su lugar:

1. **Carga el CSV preparado:**
   - Click en "Obtener datos" → "Texto/CSV"
   - Navega a: `powerbi/data/Latinobarometro_2024_PowerBI.csv`
     - Si no existe, ejecuta primero: `powerbi/scripts/prepare_powerbi_data.py`
   - Separador: **Punto y coma (;)**
   - Codificación: **UTF-8**
   - Click en **"Transformar datos"** (Transform Data) para revisar antes de cargar
   - Click en **"Cerrar y aplicar"** (Close & Apply)

2. **O carga el CSV original y limpia en Power BI:**
   - Cargar: `data/Latinobarometro_2024.csv`
   - Separador: Punto y coma (;)
   - En "Transformar datos", haz las limpiezas necesarias (como en el script Python)

### Paso 3: Modelo Limpio Final

Tu modelo debería tener solo:

- ✅ **Latinobarometro_2024** (o el nombre que le diste) - Tabla principal con los datos
- ✅ **country_codes** (opcional, si quieres modelo en estrella estricto)

**NO deberías tener:**
- ❌ Table001-Table024
- ❌ Page001-Page007
- ❌ Cualquier tabla del PDF

---

## 📚 ¿Qué Hacer con el PDF del Cuestionario?

El PDF es **solo referencia**. Úsalo para:

1. **Entender qué significan las columnas** (P23STM, P30ST, P31ST, etc.)
2. **Identificar códigos de valores** (qué significa 1, 2, 3 en cada pregunta)
3. **Consultar cuando necesites** - No lo cargues en Power BI

### Alternativa: Extraer Información Clave

Si realmente necesitas tener la información del cuestionario disponible en Power BI:

1. **Crea una tabla manual pequeña** con solo la información que necesites:
   - Códigos de columnas y sus significados
   - Valores y sus etiquetas
   - Etc.

2. **O crea un archivo de mapeo:**
   - Un Excel o CSV simple con: Columna | Descripción | Valores
   - Esto es más útil que cargar todo el PDF

---

## 🔧 Si Ya Tienes Datos Cargados Correctamente

Si ya tienes `Latinobarometro_2024` cargado con datos:

1. **Solo elimina las tablas del PDF** (Table001-Table024, etc.)
2. **Verifica que tu tabla principal tenga las columnas correctas:**
   - `IDENPA`, `EDAD`, `SEXO`, `REEDUC.3`
   - `P23STM.1`, `P23STM.2`, `P23STM.3`
   - `P28ST`, `P29ST.A-H`, `P30ST.A-E`, `P31ST`
   - Etc.

3. **Continúa con la configuración normal** según `POWERBI_SETUP_COMPLETO.md`

---

## 🎯 Resumen Rápido

1. ❌ **Elimina:** Todas las tablas Table001-Table024, Page001-Page007
2. ✅ **Mantén:** Solo tu tabla de datos principal
3. ✅ **Usa el PDF:** Solo como referencia, no lo cargues en Power BI
4. ✅ **Sigue:** Las guías en `POWERBI_SETUP_COMPLETO.md`

---

## 💡 Tips Adicionales

- **Si no ves la opción de eliminar:** Click derecho en la tabla en el panel "Fields" o en el panel "Data"
- **Si accidentalmente guardaste:** Puedes eliminar las tablas en cualquier momento, no afectará tus datos
- **Para referencia rápida:** Mantén el PDF abierto en otra ventana o crea un archivo de referencia pequeño

---

**¡Después de limpiar, continúa con `POWERBI_SETUP_COMPLETO.md`!** 🚀


# ⚡ Workflow Rápido - Power BI Dashboard

## 🎯 Flujo de Trabajo Recomendado

### Situación Actual: Tienes muchas tablas del PDF cargadas

```
┌─────────────────────────────────────────────────┐
│  PASO 1: LIMPIEZA (5 minutos)                  │
│  ────────────────────────────────────────────   │
│  1. Elimina todas las tablas Table001-Table024 │
│  2. Elimina Page001-Page007                     │
│  3. Elimina Hoja 1, Hoja2 (si existen)         │
│  4. Mantén solo country_codes si la necesitas   │
│                                                 │
│  📖 Guía: POWERBI_CLEANUP_GUIDE.md             │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  PASO 2: CARGAR DATOS (5 minutos)              │
│  ────────────────────────────────────────────   │
│  1. Ejecuta: python/scripts/prepare_powerbi_   │
│     data.py (si no lo has hecho)               │
│                                                 │
│  2. En Power BI:                                │
│     - Obtener datos → Texto/CSV                 │
│     - Seleccionar: powerbi/data/               │
│       Latinobarometro_2024_PowerBI.csv         │
│     - Separador: ; (punto y coma)              │
│     - UTF-8                                     │
│                                                 │
│  ✅ Resultado: Una sola tabla limpia           │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  PASO 3: CONFIGURAR MODELO (10 minutos)        │
│  ────────────────────────────────────────────   │
│  1. Crear columnas calculadas:                  │
│     - Grupo_Educativo                           │
│     - Interes_Ambiente_Limpio (ajustar)        │
│                                                 │
│  2. Crear medidas DAX básicas                  │
│                                                 │
│  📖 Guía: POWERBI_SETUP_COMPLETO.md            │
│  📋 Fórmulas: DAX_FORMULAS_REFERENCE.md        │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  PASO 4: CREAR HOJAS (1-2 horas)               │
│  ────────────────────────────────────────────   │
│  Hoja 1: Confianza_en medios                   │
│  Hoja 2: Interés en ambiente                   │
│  Hoja 3: Redes sociales                        │
│  Hoja 4: Conclusiones                          │
│                                                 │
│  📖 Guía: POWERBI_SETUP_COMPLETO.md            │
└─────────────────────────────────────────────────┘
```

---

## 🚨 Solución Rápida: Si Tienes Muchas Tablas

### Opción A: Eliminar Todo y Empezar de Nuevo

1. En Power BI: **Archivo → Nuevo → Nuevo archivo**
2. Carga solo el CSV preparado (`Latinobarometro_2024_PowerBI.csv`)
3. Ignora el PDF completamente

### Opción B: Limpiar el Archivo Actual

1. Ve al panel "Fields" (Campos) o "Data" (Datos)
2. Elimina todas las tablas que NO sean tu tabla principal
3. Guarda el archivo

---

## 📋 Checklist Rápido

- [ ] ✅ Eliminé todas las tablas del PDF (Table001-Table024, etc.)
- [ ] ✅ Cargué solo el CSV de datos (no el PDF)
- [ ] ✅ Tengo una sola tabla principal con datos
- [ ] ✅ Creé columnas calculadas necesarias
- [ ] ✅ Creé medidas DAX básicas
- [ ] ✅ Estoy listo para crear visualizaciones

---

## 💡 Recursos por Etapa

### Si tienes problemas con muchas tablas:
→ **[POWERBI_CLEANUP_GUIDE.md](POWERBI_CLEANUP_GUIDE.md)**

### Si necesitas identificar columnas:
→ **[COLUMNAS_REFERENCIA.md](COLUMNAS_REFERENCIA.md)**
→ Ejecuta: `python/scripts/explore_columns.py`

### Si necesitas fórmulas DAX:
→ **[DAX_FORMULAS_REFERENCE.md](DAX_FORMULAS_REFERENCE.md)**

### Si necesitas crear las hojas:
→ **[POWERBI_SETUP_COMPLETO.md](POWERBI_SETUP_COMPLETO.md)**

---

## ⏱️ Tiempos Estimados

- **Limpieza:** 5 minutos
- **Carga de datos:** 5 minutos  
- **Configuración inicial:** 15 minutos
- **Creación de hojas:** 1-2 horas
- **Ajustes finales:** 30 minutos

**Total: ~2.5-3 horas**

---

**¡Empieza por la limpieza y luego sigue el flujo!** 🚀


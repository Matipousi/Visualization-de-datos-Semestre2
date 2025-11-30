# 📊 Recursos Power BI - Latinobarómetro 2024

Esta carpeta contiene todos los recursos necesarios para crear el dashboard de Power BI según los requisitos del trabajo final.

## 📁 Estructura

```
powerbi/
├── README.md                    ← Estás aquí
├── docs/                        ← Documentación y guías
│   ├── README_POWERBI.md        ← Índice completo y resumen
│   ├── QUICK_START_POWERBI.md   ← ⚡ Inicio rápido (empieza aquí)
│   ├── POWERBI_SETUP_COMPLETO.md ← Guía paso a paso detallada
│   ├── POWERBI_GUIDE.md         ← Guía general y conceptos
│   └── DAX_FORMULAS_REFERENCE.md ← Referencia de fórmulas DAX
├── scripts/                     ← Scripts de Python
│   ├── prepare_powerbi_data.py  ← Prepara dataset para Power BI
│   └── explore_columns.py       ← Explora columnas del dataset
└── data/                        ← Datos preparados (se generan)
    ├── Latinobarometro_2024_PowerBI.csv
    └── Resumen_Columnas_PowerBI.csv
```

## 🚀 Inicio Rápido

1. **Lee primero**: `docs/QUICK_START_POWERBI.md`
2. **Genera el dataset**: 
   ```bash
   cd scripts
   python prepare_powerbi_data.py
   ```
3. **Sigue la guía completa**: `docs/POWERBI_SETUP_COMPLETO.md`

## 📚 Documentación

### ⚡ Inicio Rápido
- **[QUICK_START_POWERBI.md](docs/QUICK_START_POWERBI.md)** - Empieza aquí para un inicio rápido

### 🧹 Limpieza y Configuración
- **[POWERBI_CLEANUP_GUIDE.md](docs/POWERBI_CLEANUP_GUIDE.md)** - **NUEVO:** Si cargaste el PDF y tienes muchas tablas, lee esto primero
- **[COLUMNAS_REFERENCIA.md](docs/COLUMNAS_REFERENCIA.md)** - **NUEVO:** Referencia rápida de columnas (en lugar de cargar el PDF)

### 📖 Guías Completas
- **[README_POWERBI.md](docs/README_POWERBI.md)** - Índice completo de todos los recursos
- **[POWERBI_SETUP_COMPLETO.md](docs/POWERBI_SETUP_COMPLETO.md)** - Guía detallada paso a paso
- **[POWERBI_GUIDE.md](docs/POWERBI_GUIDE.md)** - Guía general y conceptos

### 📋 Referencias
- **[DAX_FORMULAS_REFERENCE.md](docs/DAX_FORMULAS_REFERENCE.md)** - Todas las fórmulas DAX listas para copiar

## 🛠️ Scripts

- **prepare_powerbi_data.py** - Genera el dataset optimizado para Power BI
- **explore_columns.py** - Ayuda a identificar columnas relevantes

## 📊 Datos

Los datos originales están en `../data/` (un nivel arriba).

Los datos preparados se generan en `powerbi/data/` al ejecutar el script de preparación.

## 💡 Notas Importantes

- Los datos deben generarse ejecutando el script primero
- Revisa el codebook para identificar columnas específicas (interés en ambiente, etc.)
- Las fórmulas DAX están listas para copiar y pegar

---

**¡Todo listo para crear tu dashboard!** 🎯


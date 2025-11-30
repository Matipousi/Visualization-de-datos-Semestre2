# 📋 Referencia Rápida de Columnas - Latinobarómetro 2024

Basado en el cuestionario PDF. Úsalo como referencia rápida en lugar de cargar todo el PDF.

## 🔑 Columnas Principales para el Dashboard

### Filtros

| Columna | Descripción | Valores |
|---------|-------------|---------|
| `IDENPA` | Código de país | Numérico (32=Argentina, 858=Uruguay, etc.) |
| `EDAD` | Edad del encuestado | 16-100+ años |
| `SEXO` | Sexo | 1=Hombre, 2=Mujer |
| `REEDUC.3` | Años de estudio alcanzados | Numérico (0-99) |

### Confianza en Medios (Hoja 1)

**P23STM - Confianza en medios de comunicación:**

Según el cuestionario, P23STM pregunta sobre "¿Quién cree Ud. que tiene más poder?" pero las columnas P23STM.1, P23STM.2, P23STM.3 representan confianza en diferentes medios.

- **`P23STM.1`** - Confianza en TV
- **`P23STM.2`** - Confianza en Redes Sociales  
- **`P23STM.3`** - Confianza en otro medio (radio/diario)

**Escala de confianza:** (verificar en codebook)
- Valores típicos: 1-10 (o similar)
- Valores inválidos: -1, -2, -3, -5, 96, 97, 98, 99 (No sabe/No responde)

### Interés en Medio Ambiente (Hoja 2)

**Necesitas verificar en el codebook cuál columna es específicamente "interés en medio ambiente":**

Opciones probables:
- **`P31ST`** - Una pregunta única (valores 1-4 observados)
- **`P30ST.A`** - Tema A de interés (valores 1-4)
- **`P30ST.B`** - Tema B de interés (valores 1-4)
- **`P30ST.C`** - Tema C de interés (valores 1-4)
- **`P30ST.D`** - Tema D de interés (valores 1-4)
- **`P30ST.E`** - Tema E de interés (valores 1-4)

**Escala:** Probablemente 1=Muy interesado, 4=No interesado (verificar)

### Uso de Redes Sociales (Hoja 3)

- **`P28ST`** - Frecuencia de uso de redes sociales
  - Valores observados: 1, 2, 3, -5
  - (Verificar significados en codebook: ej. 1=Diario, 2=Semanal, 3=Nunca)

- **`P28ST.A`, `P28ST.B`, `P28ST.C`, `P28ST.D`** - Aspectos específicos de uso

- **`P29ST.A` hasta `P29ST.H`** - Más aspectos de redes sociales
  - Valores típicos: 1-4
  - (Verificar significados en codebook)

---

## 📖 Valores Inválidos Comunes

En todas las columnas, estos valores suelen indicar "No sabe/No responde" y deben tratarse como `BLANK()` en DAX:

- `-1` - No aplica
- `-2` - No sabe
- `-3` - No responde
- `-5` - No sabe/No contesta
- `96`, `97`, `98`, `99` - Códigos de no respuesta

---

## 🔍 Cómo Identificar Columnas Específicas

1. **Abre el codebook Excel:** `data/Codebook Latinobarómetro.xlsx`
2. **Busca por:**
   - "medio ambiente" o "ambiente" para interés en ambiente
   - "redes sociales" para uso de redes
   - "confianza" para confianza en medios
3. **Ejecuta el script exploratorio:**
   ```bash
   cd powerbi/scripts
   python explore_columns.py
   ```

---

## 💡 Columnas Ya Preparadas (si usaste el script)

Si ejecutaste `prepare_powerbi_data.py`, ya tienes estas columnas limpias:

- `Confianza_Redes_Limpia` - P23STM.2 sin valores inválidos
- `Confianza_TV_Limpia` - P23STM.1 sin valores inválidos
- `Confianza_Otro_Limpia` - P23STM.3 sin valores inválidos
- `Anos_Estudio_Limpio` - REEDUC.3 sin valores inválidos
- `Grupo_Edad` - Edad agrupada (16-25, 26-35, etc.)
- `Sexo_Labels` - Sexo con etiquetas (Hombre/Mujer)
- `Country Name` - Nombre del país (ya fusionado)

---

## 📝 Notas Importantes

- **Este documento es solo referencia** - No lo cargues en Power BI
- **Verifica siempre en el codebook** los significados exactos de valores
- **Los valores pueden variar** según el país o la pregunta específica
- **Usa el PDF del cuestionario** como referencia visual, no como datos

---

**Mantén este archivo abierto como referencia mientras trabajas en Power BI** 📋


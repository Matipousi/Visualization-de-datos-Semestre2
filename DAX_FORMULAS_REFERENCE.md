# Referencia Rápida de Fórmulas DAX - Power BI

## 📝 Columnas Calculadas

### 1. Sexo con Etiquetas
```DAX
Sexo_Labels = 
SWITCH(
    TRUE(),
    Latinobarometro_2024_PowerBI[SEXO] = 1, "Hombre",
    Latinobarometro_2024_PowerBI[SEXO] = 2, "Mujer",
    "No especificado"
)
```

### 2. Grupo de Edad
```DAX
Grupo_Edad = 
SWITCH(
    TRUE(),
    Latinobarometro_2024_PowerBI[EDAD] <= 25, "16-25",
    Latinobarometro_2024_PowerBI[EDAD] <= 35, "26-35",
    Latinobarometro_2024_PowerBI[EDAD] <= 45, "36-45",
    Latinobarometro_2024_PowerBI[EDAD] <= 55, "46-55",
    Latinobarometro_2024_PowerBI[EDAD] <= 65, "56-65",
    "66+"
)
```

### 3. Grupo Educativo
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

### 4. Interés en Ambiente (Limpio)
**⚠️ REEMPLAZAR 'P31ST' con la columna correcta del codebook**
```DAX
Interes_Ambiente_Limpio = 
VAR Valor = Latinobarometro_2024_PowerBI[P31ST]  // Cambiar según codebook
VAR Limpio = IF(
    Valor IN {-1, -2, -3, -5, 96, 97, 98, 99},
    BLANK(),
    Valor
)
RETURN Limpio
```

---

## 📊 Medidas Básicas

### Conteos
```DAX
Total_Respuestas = COUNTROWS(Latinobarometro_2024_PowerBI)

Total_Por_Pais = 
CALCULATE(
    [Total_Respuestas],
    ALLSELECTED(Latinobarometro_2024_PowerBI)
)
```

### Promedios
```DAX
Promedio_Confianza_Redes = 
AVERAGE(Latinobarometro_2024_PowerBI[Confianza_Redes_Limpia])

Promedio_Confianza_TV = 
AVERAGE(Latinobarometro_2024_PowerBI[Confianza_TV_Limpia])

Promedio_Confianza_Otro = 
AVERAGE(Latinobarometro_2024_PowerBI[Confianza_Otro_Limpia])

Promedio_Interes_Ambiente = 
AVERAGE(Latinobarometro_2024_PowerBI[Interes_Ambiente_Limpio])
```

---

## 🌍 Medidas por País (con filtros)

### Confianza en Medios por País
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

Diferencia_Confianza_Redes_vs_TV = 
[Promedio_Confianza_Redes_por_Pais] - [Promedio_Confianza_TV_por_Pais]
```

### Interés en Ambiente por País
```DAX
Promedio_Interes_Ambiente_por_Pais = 
CALCULATE(
    [Promedio_Interes_Ambiente],
    ALLSELECTED(Latinobarometro_2024_PowerBI)
)

Max_Interes_Ambiente = 
MAXX(
    ALLSELECTED(Latinobarometro_2024_PowerBI[Country Name]),
    [Promedio_Interes_Ambiente_por_Pais]
)

Min_Interes_Ambiente = 
MINX(
    ALLSELECTED(Latinobarometro_2024_PowerBI[Country Name]),
    [Promedio_Interes_Ambiente_por_Pais]
)
```

---

## 📱 Medidas para Redes Sociales

### Uso de Redes Sociales
**⚠️ Ajustar valores según codebook (P28ST o P29ST)**
```DAX
Usa_Redes_Sociales = 
CALCULATE(
    COUNTROWS(Latinobarometro_2024_PowerBI),
    Latinobarometro_2024_PowerBI[P28ST] IN {1, 2}  // Verificar valores
)

Porcentaje_Usa_Redes = 
DIVIDE(
    [Usa_Redes_Sociales],
    [Total_Respuestas],
    0
) * 100

Usa_Redes_Diariamente = 
CALCULATE(
    COUNTROWS(Latinobarometro_2024_PowerBI),
    Latinobarometro_2024_PowerBI[P28ST] = 1  // Verificar valor
)

Usa_Redes_Semanalmente = 
CALCULATE(
    COUNTROWS(Latinobarometro_2024_PowerBI),
    Latinobarometro_2024_PowerBI[P28ST] = 2  // Verificar valor
)
```

### Confianza en Redes por Segmentos
```DAX
Promedio_Confianza_Redes_por_Edad = 
CALCULATE(
    [Promedio_Confianza_Redes],
    ALLSELECTED(Latinobarometro_2024_PowerBI)
)

Promedio_Confianza_Redes_por_Educacion = 
CALCULATE(
    [Promedio_Confianza_Redes],
    ALLSELECTED(Latinobarometro_2024_PowerBI)
)
```

---

## 📈 Medidas Avanzadas

### Percentiles
```DAX
Percentil_50_Confianza_Redes = 
PERCENTILE.INC(
    Latinobarometro_2024_PowerBI[Confianza_Redes_Limpia],
    0.5
)

Percentil_75_Confianza_Redes = 
PERCENTILE.INC(
    Latinobarometro_2024_PowerBI[Confianza_Redes_Limpia],
    0.75
)
```

### Rankings
```DAX
Ranking_Interes_Ambiente = 
RANKX(
    ALLSELECTED(Latinobarometro_2024_PowerBI[Country Name]),
    [Promedio_Interes_Ambiente_por_Pais],
    ,
    DESC
)
```

### Medidas Condicionales
```DAX
Confianza_Redes_Alta = 
CALCULATE(
    COUNTROWS(Latinobarometro_2024_PowerBI),
    Latinobarometro_2024_PowerBI[Confianza_Redes_Limpia] >= 7
)

Porcentaje_Confianza_Alta = 
DIVIDE(
    [Confianza_Redes_Alta],
    [Total_Respuestas],
    0
) * 100
```

---

## 🎯 Medidas con Filtros Contextuales

### Promedio con Filtro de País Específico
```DAX
Promedio_Confianza_Redes_Uruguay = 
CALCULATE(
    [Promedio_Confianza_Redes],
    Latinobarometro_2024_PowerBI[Country Name] = "Uruguay"
)
```

### Comparación con Promedio Regional
```DAX
Promedio_Regional_Confianza_Redes = 
CALCULATE(
    [Promedio_Confianza_Redes],
    ALL(Latinobarometro_2024_PowerBI[Country Name])
)

Diferencia_vs_Regional = 
[Promedio_Confianza_Redes_por_Pais] - [Promedio_Regional_Confianza_Redes]
```

---

## 💡 Tips para Usar las Fórmulas

1. **Reemplazar nombres de tablas:** Si tu tabla se llama diferente, reemplaza `Latinobarometro_2024_PowerBI` con tu nombre de tabla

2. **Verificar valores:** Los valores como {-1, -2, -3, -5, 96, 97, 98, 99} son códigos de "No sabe/No responde" y deben tratarse como BLANK()

3. **Ajustar según codebook:** Las columnas P28ST, P29ST, P30ST, P31ST necesitan verificarse en el codebook para saber qué significan exactamente

4. **Probar medidas:** Crea las medidas una por una y prueba que funcionen antes de continuar

5. **ALLSELECTED vs ALL:**
   - `ALLSELECTED`: Respeta los filtros de segmentadores
   - `ALL`: Ignora todos los filtros
   - Elige según lo que necesites

---

## 🔧 Solución de Problemas Comunes

### Error: "La función 'AVERAGE' no reconoce la columna..."
- Verifica que la columna existe y tiene datos
- Asegúrate de usar el nombre exacto de la tabla y columna

### Medidas no se actualizan con filtros:
- Usa `ALLSELECTED()` en lugar de `ALL()` cuando quieras respetar filtros
- Verifica que los filtros estén configurados correctamente

### Valores en blanco aparecen:
- Es normal si hay valores inválidos que se convierten en BLANK()
- Usa `FILTER()` para excluir valores específicos si es necesario

---

**Nota:** Recuerda revisar el codebook para identificar las columnas exactas de interés en ambiente y uso de redes sociales.


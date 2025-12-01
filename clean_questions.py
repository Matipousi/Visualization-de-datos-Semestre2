#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para limpiar y corregir el CSV de preguntas.
"""

import csv
import re

def clean_question_text(text):
    """Limpia el texto de la pregunta."""
    if not text:
        return ""
    
    # Eliminar texto después del último signo de interrogación si hay mucho texto extra
    if '?' in text:
        # Buscar el último ? que parece ser el final de la pregunta
        last_q = text.rfind('?')
        if last_q > 0:
            # Si después del último ? hay mucho texto (más de 50 caracteres), cortar ahí
            remaining = text[last_q + 1:].strip()
            if len(remaining) > 50 and not ('¿' in remaining):
                text = text[:last_q + 1]
    
    # Eliminar opciones de respuesta comunes que aparecen después
    text = re.sub(r'\s+No responde.*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+Está progresando.*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+Está estancado.*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+Está en retroceso.*$', '', text, flags=re.IGNORECASE)
    
    # Eliminar códigos de otras preguntas que puedan haber quedado
    text = re.sub(r'\s+[A-Z]\d+[A-Z]+[A-Z0-9]*\.[A-Z]?\s+', ' ', text)
    
    # Limpiar espacios
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Leer el CSV actual
questions = []
with open('data/preguntas_codigos.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        code = row['clave']
        text = row['valor']
        
        # Limpiar el texto
        cleaned_text = clean_question_text(text)
        
        if cleaned_text:
            questions.append((code, cleaned_text))

# Agregar P1ST que falta (basado en el ejemplo del usuario)
# Verificar si ya existe
has_p1st = any(code == 'P1ST' for code, _ in questions)
if not has_p1st:
    # Insertar P1ST al principio (después del encabezado)
    questions.insert(0, ('P1ST', 'En términos generales, ¿diría Ud. que está satisfecho con su vida? ¿Diría Ud. que está....?'))

# Limpiar P2ST específicamente
for i, (code, text) in enumerate(questions):
    if code == 'P2ST':
        questions[i] = (code, '¿Diría Ud. que este país...?')
        break

# Limpiar P3N
for i, (code, text) in enumerate(questions):
    if code == 'P3N':
        # Ya está bien, solo asegurarse de que esté limpio
        if 'P12STGBS.B' in text:
            questions[i] = (code, '¿Tomando en cuenta los últimos 10 años, como ha avanzado Ud y su familia?')
        break

# Ordenar por código
questions.sort(key=lambda x: x[0])

# Escribir el CSV limpio
with open('data/preguntas_codigos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['clave', 'valor'])
    for code, text in questions:
        writer.writerow([code, text])

print(f"CSV limpiado. Total de preguntas: {len(questions)}")
print("\nPrimeras 5 preguntas:")
for i, (code, text) in enumerate(questions[:5], 1):
    print(f"{i}. {code}: {text[:80]}...")


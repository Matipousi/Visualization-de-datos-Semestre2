#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para extraer códigos de preguntas y sus textos del cuestionario PDF
y generar un archivo CSV con formato clave-valor.
"""

import pdfplumber
import re
import csv
import sys

def extract_questions_from_pdf(pdf_path):
    """
    Extrae códigos de preguntas y sus textos del PDF.
    """
    questions = []
    
    print("Leyendo PDF...")
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                full_text += text + "\n"
            if (i + 1) % 10 == 0:
                print(f"  Procesadas {i + 1} páginas...")
    
    print(f"Texto extraído: {len(full_text)} caracteres")
    
    # Guardar una muestra del texto para debugging
    # with open('debug_text.txt', 'w', encoding='utf-8') as f:
    #     f.write(full_text[:5000])
    
    # Patrón mejorado para encontrar códigos de preguntas
    # Formato: **P1ST.** o P1ST. seguido del texto de la pregunta
    # Los códigos pueden tener formato: P1ST, P2ST, P3N, P4ST, S15A, etc.
    
    # Primero intentar con formato **P1ST.**
    pattern1 = r'\*\*([A-Z]\d+[A-Z]+[A-Z0-9]*)\*\*\.?\s*(.*?)(?=\*\*[A-Z]\d+[A-Z]+[A-Z0-9]*\*\*|$)'
    matches1 = list(re.finditer(pattern1, full_text, re.DOTALL))
    
    # Si no encontramos suficientes, intentar sin los asteriscos
    if len(matches1) < 5:
        pattern2 = r'([A-Z]\d+[A-Z]+[A-Z0-9]*)\.\s+(.*?)(?=[A-Z]\d+[A-Z]+[A-Z0-9]*\.|$)'
        matches1 = list(re.finditer(pattern2, full_text, re.DOTALL))
    
    print(f"Encontrados {len(matches1)} posibles preguntas con el patrón inicial")
    
    for match in matches1:
        code = match.group(1).strip()
        question_text = match.group(2).strip()
        
        # Limpiar el texto de la pregunta
        # Normalizar espacios
        question_text = re.sub(r'\s+', ' ', question_text)
        
        # Extraer solo la pregunta principal (hasta las instrucciones o tablas)
        # La pregunta generalmente termina con un signo de interrogación o antes de instrucciones
        # Buscar el final de la pregunta (antes de instrucciones entre paréntesis o tablas)
        
        # Dividir por líneas y tomar solo las que contienen la pregunta
        lines = question_text.split('\n')
        question_lines = []
        
        for line in lines:
            line = line.strip()
            # Saltar líneas vacías
            if not line:
                continue
            # Saltar líneas que son solo números, tablas o alternativas
            if re.match(r'^[\d\s\|\-]+$', line):
                break  # Detener cuando encontramos una tabla
            # Saltar instrucciones comunes
            if re.match(r'^\(.*\)$', line) or re.match(r'^NO LEER', line, re.IGNORECASE):
                break
            # Saltar líneas que son solo alternativas de respuesta (ej: "Muy satisfecho | 1")
            if re.match(r'^[^¿]*\s+\|\s*\d+$', line):
                break
            # Si la línea contiene la pregunta o es parte de ella
            if '¿' in line or '?' in line or len(line) > 20:
                question_lines.append(line)
            # Si encontramos una línea que parece ser el inicio de instrucciones, detener
            if re.match(r'^\(LEA|^\(ESPERE|^\(MARQUE|^\(ANOTE|^\(MOSTRAR', line, re.IGNORECASE):
                break
        
        question_text = ' '.join(question_lines).strip()
        
        # Limpiar más: eliminar instrucciones que puedan haber quedado
        question_text = re.sub(r'\s*\(LEA ALTERNATIVAS.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(ESPERE RESPUESTA.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(MARQUE.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(ANOTE.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(MOSTRAR.*?\)', '', question_text, flags=re.IGNORECASE)
        
        # Tomar solo hasta el último signo de interrogación si hay múltiples
        if '?' in question_text:
            # Encontrar el último signo de interrogación
            last_q = question_text.rfind('?')
            if last_q > 0:
                question_text = question_text[:last_q + 1]
        
        # Validar que tenemos una pregunta válida
        if code and question_text and len(question_text) > 10:
            # Verificar que contiene al menos un signo de interrogación o es una pregunta válida
            if '¿' in question_text or '?' in question_text or len(question_text) > 30:
                questions.append((code, question_text))
    
    # Eliminar duplicados manteniendo el orden
    seen = set()
    unique_questions = []
    for code, text in questions:
        if code not in seen:
            seen.add(code)
            unique_questions.append((code, text))
    
    return unique_questions

def main():
    pdf_path = 'data/Latinobarometro_2024_Cuestionario_esp.pdf'
    output_csv = 'data/preguntas_codigos.csv'
    
    print(f"Extrayendo preguntas de {pdf_path}...")
    questions = extract_questions_from_pdf(pdf_path)
    
    print(f"Se encontraron {len(questions)} preguntas.")
    
    # Escribir al CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['clave', 'valor'])  # Encabezados
        
        for code, question_text in questions:
            writer.writerow([code, question_text])
    
    print(f"Archivo CSV creado: {output_csv}")
    print("\nPrimeras 5 preguntas extraídas:")
    for i, (code, text) in enumerate(questions[:5], 1):
        print(f"{i}. {code}: {text[:80]}...")

if __name__ == '__main__':
    main()


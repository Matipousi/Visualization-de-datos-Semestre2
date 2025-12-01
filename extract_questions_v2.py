#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script mejorado para extraer códigos de preguntas y sus textos del cuestionario PDF
y generar un archivo CSV con formato clave-valor.
"""

import pdfplumber
import re
import csv

def clean_question_text(text):
    """Limpia el texto de la pregunta eliminando instrucciones y tablas."""
    if not text:
        return ""
    
    # Dividir por líneas para procesar mejor
    lines = text.split('\n')
    question_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detener si encontramos el inicio de otra pregunta (código seguido de punto)
        if re.match(r'^[A-Z]\d+[A-Z]+[A-Z0-9]*\.?\s+', line):
            break
        
        # Saltar líneas que son tablas o alternativas
        if re.match(r'^[\d\s\|\-\.]+$', line):
            break  # Detener cuando encontramos una tabla
        if re.match(r'^[A-Z][a-z]+\s+\|\s*\d+$', line):
            break
        if re.match(r'^\d+\s+\d+$', line):
            break
        
        # Detener si encontramos instrucciones que indican el final de la pregunta
        if re.match(r'^\(LEA|^\(ESPERE|^\(MARQUE|^\(ANOTE|^\(MOSTRAR', line, re.IGNORECASE):
            break
        
        # Detener si encontramos "NO LEER"
        if re.match(r'^NO LEER', line, re.IGNORECASE):
            break
        
        # Si la línea parece ser parte de la pregunta, agregarla
        if len(line) > 3:
            question_lines.append(line)
    
    text = ' '.join(question_lines)
    
    # Normalizar espacios
    text = re.sub(r'\s+', ' ', text)
    
    # Eliminar instrucciones comunes entre paréntesis que puedan haber quedado
    text = re.sub(r'\(LEA ALTERNATIVAS.*?\)', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\(ESPERE RESPUESTA.*?\)', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\(MARQUE.*?\)', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\(ANOTE.*?\)', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\(MOSTRAR.*?\)', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\(LEA.*?\)', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Eliminar "NO LEER" y variantes
    text = re.sub(r'NO LEER.*?(?=\s|$)', '', text, flags=re.IGNORECASE)
    
    # Tomar solo hasta el último signo de interrogación si hay múltiples
    # Pero mantener todo si hay múltiples preguntas en una
    if '?' in text:
        # Si hay múltiples signos de interrogación, tomar hasta el último que tenga sentido
        # Buscar el último "?" que esté seguido de espacio o fin de texto
        matches = list(re.finditer(r'\?', text))
        if matches:
            last_q_pos = matches[-1].end()
            # Verificar que después del último ? no hay mucho más texto relevante
            remaining = text[last_q_pos:].strip()
            if len(remaining) < 50 or not ('¿' in remaining or '?' in remaining):
                text = text[:last_q_pos]
    
    # Limpiar espacios finales
    text = text.strip()
    
    return text

def extract_questions_from_pdf(pdf_path):
    """Extrae códigos de preguntas y sus textos del PDF."""
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
    
    # Patrón para encontrar códigos de preguntas
    # Formato: **P1ST.** o P1ST. seguido del texto
    # Los códigos pueden ser: P1ST, P2ST, P3N, S15A, etc.
    
    # Buscar todos los códigos posibles en el texto
    # Patrón: letra(s) + número(s) + letra(s) + número(s) opcionales
    code_pattern = r'\b([A-Z]\d+[A-Z]+[A-Z0-9]*)\b'
    all_codes = re.findall(code_pattern, full_text)
    
    # Encontrar posiciones de cada código
    code_positions = []
    for match in re.finditer(code_pattern, full_text):
        code = match.group(1)
        pos = match.start()
        # Verificar que el código está seguido de un punto o espacio y texto
        context = full_text[pos:pos+50]
        if re.match(r'[A-Z]\d+[A-Z]+[A-Z0-9]*\.?\s+', context):
            code_positions.append((code, pos))
    
    # Ordenar por posición
    code_positions.sort(key=lambda x: x[1])
    
    print(f"Encontrados {len(code_positions)} códigos de preguntas")
    
    # Extraer el texto de cada pregunta
    for i, (code, start_pos) in enumerate(code_positions):
        # Determinar el final de esta pregunta (inicio de la siguiente o fin del texto)
        if i + 1 < len(code_positions):
            end_pos = code_positions[i + 1][1]
        else:
            end_pos = len(full_text)
        
        # Extraer el texto de la pregunta
        question_text = full_text[start_pos:end_pos]
        
        # Remover el código del inicio (con o sin asteriscos, con o sin punto)
        question_text = re.sub(r'^\*\*?' + re.escape(code) + r'\*\*?\.?\s*', '', question_text)
        question_text = re.sub(r'^' + re.escape(code) + r'\.?\s*', '', question_text)
        
        # Limpiar el texto
        question_text = clean_question_text(question_text)
        
        # Validar que tenemos una pregunta válida
        if question_text and len(question_text) > 10:
            # Verificar que parece una pregunta
            if '¿' in question_text or '?' in question_text or len(question_text) > 30:
                questions.append((code, question_text))
    
    # Eliminar duplicados manteniendo el orden
    seen = set()
    unique_questions = []
    for code, text in questions:
        if code not in seen:
            seen.add(code)
            unique_questions.append((code, text))
        else:
            # Si es duplicado, mantener el que tiene más texto (más completo)
            for i, (c, t) in enumerate(unique_questions):
                if c == code and len(text) > len(t):
                    unique_questions[i] = (code, text)
    
    return unique_questions

def main():
    pdf_path = 'data/Latinobarometro_2024_Cuestionario_esp.pdf'
    output_csv = 'data/preguntas_codigos.csv'
    
    print(f"Extrayendo preguntas de {pdf_path}...")
    questions = extract_questions_from_pdf(pdf_path)
    
    print(f"\nSe encontraron {len(questions)} preguntas únicas.")
    
    # Ordenar por código para facilitar la revisión
    questions.sort(key=lambda x: x[0])
    
    # Escribir al CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['clave', 'valor'])  # Encabezados
        
        for code, question_text in questions:
            writer.writerow([code, question_text])
    
    print(f"Archivo CSV creado: {output_csv}")
    print("\nPrimeras 10 preguntas extraídas:")
    for i, (code, text) in enumerate(questions[:10], 1):
        print(f"{i}. {code}: {text[:100]}...")

if __name__ == '__main__':
    main()


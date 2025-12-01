#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para extraer TODAS las preguntas del PDF de manera sistemática
"""

import pdfplumber
import re
import csv

def extract_all_questions(pdf_path):
    """Extrae todas las preguntas del PDF de manera sistemática."""
    questions = []
    
    print("Leyendo PDF completo...")
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    
    print(f"Texto extraído: {len(full_text)} caracteres")
    
    # Patrón para encontrar códigos de preguntas
    # Formato: P1ST., P2ST., S15 A-B., etc.
    # Los códigos pueden tener formato: P1ST, P2ST, P3N, S15A, P14STGBS A-N, etc.
    
    # Buscar todos los códigos posibles
    # Patrón más flexible: letra(s) + número(s) + letra(s) + número(s) opcionales + punto
    # También puede tener espacios y guiones: "S15 A-B", "P14STGBS A-N"
    pattern = r'([A-Z]\d+[A-Z]*[A-Z0-9]*\s*[A-Z]?[-]?[A-Z]?[0-9]?)\s*\.'
    
    matches = list(re.finditer(pattern, full_text))
    print(f"Encontrados {len(matches)} posibles códigos de preguntas")
    
    # Procesar cada código encontrado
    for i, match in enumerate(matches):
        code = match.group(1).strip()
        start_pos = match.end()
        
        # Determinar el final de esta pregunta (inicio de la siguiente o fin del texto)
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = min(start_pos + 500, len(full_text))  # Limitar a 500 caracteres si es la última
        
        # Extraer el texto de la pregunta
        question_text = full_text[start_pos:end_pos]
        
        # Limpiar el texto
        # Remover saltos de línea múltiples
        question_text = re.sub(r'\n+', ' ', question_text)
        # Remover espacios múltiples
        question_text = re.sub(r'\s+', ' ', question_text)
        
        # Extraer solo la pregunta principal (hasta las instrucciones o tablas)
        # Buscar el final de la pregunta
        lines = question_text.split('.')
        question_parts = []
        
        for part in lines:
            part = part.strip()
            if not part:
                continue
            
            # Detener si encontramos instrucciones comunes
            if re.match(r'\(LEA|\(ESPERE|\(MARQUE|\(ANOTE|\(MOSTRAR|\(ELIJA|\(CODIFICAR', part, re.IGNORECASE):
                break
            
            # Detener si encontramos "NO LEER"
            if re.match(r'NO LEER', part, re.IGNORECASE):
                break
            
            # Detener si encontramos tablas (solo números)
            if re.match(r'^[\d\s\|\-\.]+$', part):
                break
            
            # Si la parte contiene la pregunta o es parte de ella
            if '¿' in part or '?' in part or len(part) > 15:
                question_parts.append(part)
                # Si encontramos un signo de interrogación, podemos detener
                if '?' in part:
                    break
        
        question_text = '. '.join(question_parts).strip()
        
        # Limpiar más: eliminar instrucciones que puedan haber quedado
        question_text = re.sub(r'\s*\(LEA.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(ESPERE.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(MARQUE.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(ANOTE.*?\)', '', question_text, flags=re.IGNORECASE)
        question_text = re.sub(r'\s*\(MOSTRAR.*?\)', '', question_text, flags=re.IGNORECASE)
        
        # Tomar solo hasta el último signo de interrogación si hay múltiples
        if '?' in question_text:
            last_q = question_text.rfind('?')
            if last_q > 0:
                question_text = question_text[:last_q + 1]
        
        # Validar que tenemos una pregunta válida
        if question_text and len(question_text) > 10:
            # Verificar que parece una pregunta
            if '¿' in question_text or '?' in question_text or len(question_text) > 20:
                questions.append((code, question_text))
    
    # Eliminar duplicados manteniendo el orden
    seen = set()
    unique_questions = []
    for code, text in questions:
        # Normalizar código (eliminar espacios extra)
        code_normalized = re.sub(r'\s+', '', code)
        if code_normalized not in seen:
            seen.add(code_normalized)
            unique_questions.append((code, text))
        else:
            # Si es duplicado, mantener el que tiene más texto (más completo)
            for i, (c, t) in enumerate(unique_questions):
                c_norm = re.sub(r'\s+', '', c)
                if c_norm == code_normalized and len(text) > len(t):
                    unique_questions[i] = (code, text)
    
    return unique_questions

def main():
    pdf_path = 'data/Latinobarometro_2024_Cuestionario_esp.pdf'
    output_csv = 'data/preguntas_codigos_completo.csv'
    
    print(f"Extrayendo TODAS las preguntas de {pdf_path}...")
    questions = extract_all_questions(pdf_path)
    
    print(f"\nSe encontraron {len(questions)} preguntas únicas.")
    
    # Ordenar por código para facilitar la revisión
    questions.sort(key=lambda x: x[0])
    
    # Escribir al CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['clave', 'valor'])
        
        for code, question_text in questions:
            writer.writerow([code, question_text])
    
    print(f"Archivo CSV creado: {output_csv}")
    print("\nPrimeras 20 preguntas extraídas:")
    for i, (code, text) in enumerate(questions[:20], 1):
        print(f"{i}. {code}: {text[:80]}...")
    
    print(f"\nÚltimas 10 preguntas extraídas:")
    for i, (code, text) in enumerate(questions[-10:], len(questions)-9):
        print(f"{i}. {code}: {text[:80]}...")

if __name__ == '__main__':
    main()




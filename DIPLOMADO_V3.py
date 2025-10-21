"""
DIPLOMADO_V3
"""

#!/usr/bin/env python
# coding: utf-8

# In[2]:


from openai import OpenAI
from docx import Document
import os, sys
from docxtpl import DocxTemplate as DocTemp
from docxtpl import InlineImage
from docx.shared import Cm, Inches, Mm, Emu
from docxtpl import DocxTemplate
import time

from openai import OpenAI
from docxtpl import DocxTemplate

client = OpenAI(api_key="YOUR_API_KEY_HERE")

def generar_mensaje_rol(role, template, nombre_de_materia):
    return {
        "role": role,
        "content": template.format(nombre_de_materia, nombre_de_materia)
    }

def interactuar_chatgpt(nombre_de_materia, user_prompt):
    system_template = """
    En el marco de la elaboración de un programa académico para maestrías y diplomados ofrecidos por una universidad, 
    se está desarrollando un curso dedicado a {}. Este curso tiene como objetivo proporcionar una base sólida en temas relacionados a {}, 
    Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave para impulsar y gestionar 
    empresas y el entorno empresarial. La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
    y tecnológicos actuales, manteniendo un tono serio y académico que sea coherente con los estándares universitarios de enseñanza de posgrado. 
    No utilices fórmulas de cortesía. La respuesta debe ser directa, sin introducciones, similar a una humana sin que se note que es generada por IA.
    """

    messages = [
        generar_mensaje_rol("system", system_template, nombre_de_materia),
        generar_mensaje_rol("user", user_prompt, nombre_de_materia)
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    return response.choices[0].message.content

# Funciones específicas que reutilizan interactuar_chatgpt
def resumen(nombre_de_materia):
    prompt = """
    Podrías proporcionar un resumen detallado y académico para el curso titulado {}, que será parte de un programa de maestría o diplomado? 
    Incluye el nombre del curso y un resumen general que explique el enfoque principal de la materia. La respuesta no debe exceder 50 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def temas(nombre_de_materia):
    prompt = """
    Necesito un resumen exhaustivo y académico de los temas específicos que se cubrirán en el curso titulado {}. 
    Proporciona un listado detallado de cinco temas clave. Cada descripción no debe superar los 30 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def competencia(nombre_de_materia):
    prompt = """
    Describe con un tono serio y académico la competencia clave que los estudiantes deben desarrollar en el curso {}. 
    La respuesta debe empezar con un verbo en infinitivo y no exceder 50 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def objetivo(nombre_de_materia):
    prompt = """
    Proporciona una explicación detallada y académica sobre el objetivo principal del curso titulado {}. La respuesta no debe exceder 50 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def saber(nombre_de_materia):
    prompt = """
    Proporciona una lista de cinco conocimientos fundamentales que se impartirán en el curso {}. 
    Cada punto debe ser conciso y no exceder los 30 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def hacer(nombre_de_materia):
    prompt = """
    Describe en cinco puntos claros las habilidades prácticas que los estudiantes adquirirán en el curso {}. 
    Cada punto no debe exceder los 30 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def ser(nombre_de_materia):
    prompt = """
    Proporciona una lista de cinco competencias blandas (saber ser) que se desarrollarán en el curso {}. 
    Cada punto no debe exceder los 30 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def estrategias(nombre_de_materia):
    prompt = """
    Proporciona cinco estrategias de enseñanza efectivas para el curso {}. Cada punto no debe exceder los 30 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)

def recursos(nombre_de_materia):
    prompt = """
    Proporciona cinco recomendaciones de recursos didácticos (libros, artículos) en formato APA que respalden el curso {}. 
    Cada punto no debe exceder los 30 tokens.
    """
    return interactuar_chatgpt(nombre_de_materia, prompt)


def desarrollo_materias(M1, M2, M3, M4, M5, M6):
    modulos_diplo = [M1, M2, M3, M4, M5, M6]
    modulos = {}  # Inicializar fuera del ciclo para almacenar la información de todos los módulos

    for j in range(1, len(modulos_diplo) + 1):
        nombre_de_materia = modulos_diplo[j-1]  # Ajustar el índice
        print(f"Procesando módulo {j}: {nombre_de_materia}")
        # Añadir la información de cada módulo al diccionario 'modulos'
        modulos[f'nombre_materia_{j}'] = nombre_de_materia
        modulos[f'resumen_materia_{j}'] = resumen(nombre_de_materia)
        modulos[f'detalle_temas_materia_{j}'] = temas(nombre_de_materia)
        modulos[f'competencia_materia_{j}'] = competencia(nombre_de_materia)
        modulos[f'objetivo_materia_{j}'] = objetivo(nombre_de_materia)
        modulos[f'competencias_saber_materia_{j}'] = saber(nombre_de_materia)
        modulos[f'competencias_hacer_materia_{j}'] = hacer(nombre_de_materia)
        modulos[f'competencias_ser_materia_{j}'] = ser(nombre_de_materia)
        modulos[f'estrategias_enseñanaza_materia_{j}'] = estrategias(nombre_de_materia)
        modulos[f'recursos_didacticos_materia_{j}'] = recursos(nombre_de_materia)

    # El return está fuera del ciclo para devolver la información de todos los módulos
    return modulos

# Guardar el contenido en un documento
path_in = r"C:\Users\HP\Desktop\PROPUESTAS DE DIPLOMADO\Propuesta DIPLOMADO A RAFEAL\PROPUESTAS DE DIPLOMADOS\Temp_prpouesta_diplomado.docx"
path_out = r"C:\Users\HP\Desktop\PROPUESTAS DE DIPLOMADO\Propuesta DIPLOMADO A RAFEAL\PROPUESTAS DE DIPLOMADOS\pruebas\Propuesta_diplomado_completa.docx"
Nombre_diplomado = "Metodologia de la investigación cientifica"
M1 = "Epistemologia"
M2 = "Protocolo de investigación"
M3 = "Investigación cuantitativa"
M4 = "Investigación cualitativa"
M5 = "Herramientas de colecta de informacion en investigacion cientifica"
M6 = "Redacción financiamiento y publicación de artículos de investigación científica"

materias_info = desarrollo_materias(M1,M2,M3,M4,M5,M6)


doc = DocxTemplate(path_in)
doc.render(materias_info)
time.sleep(3)
doc.save(path_out)

print("Documento completado y guardado en:", path_out)


# In[ ]:






if __name__ == "__main__":
    pass

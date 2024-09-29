from llama_index import SimpleDirectoryReader, VectorStoreIndex
from langchain_openai import OpenAI
import gradio as gr
import os
 
# Configurar la clave de OpenAI
os.environ["OPENAI_API_KEY"] = ''  # Reemplaza con tu clave de OpenAI

# Función para construir el índice
def construct_index(directory_path):
    # Cargar documentos desde el directorio
    documents = SimpleDirectoryReader(directory_path).load_data()

    # Crear el índice a partir de los documentos
    index = VectorStoreIndex.from_documents(documents)

    # Guardar el índice en disco
    index.storage_context.persist(persist_dir="index")
 
    return index

# Función de chatbot básico
def chatbot(input_text):
    # Cargar el índice guardado
    index = VectorStoreIndex(storage_context="index")
    
    # Crear un motor de consulta
    query_engine = index.as_query_engine()
    
    # Realizar la consulta
    response = query_engine.query(input_text)
    
    return response.response

# Función para generar preguntas
def generar_preguntas(input_text):
    # Cargar el índice guardado
    index = VectorStoreIndex(storage_context="index")
    
    # Crear un motor de consulta
    query_engine = index.as_query_engine()
    
    # Generar preguntas
    preguntas = query_engine.query(f"Genera 5 preguntas sobre el siguiente texto: {input_text}")
    
    return preguntas.response

# Función para generar resúmenes
def generar_resumen(input_text):
    # Cargar el índice guardado
    index = VectorStoreIndex(storage_context="index")
    
    # Crear un motor de consulta
    query_engine = index.as_query_engine()
    
    # Generar resumen
    resumen = query_engine.query(f"Resume el siguiente texto: {input_text}")
    
    return resumen.response

# Función para respuestas detalladas
def generar_respuesta_detallada(input_text):
    # Cargar el índice guardado
    index = VectorStoreIndex(storage_context="index")
    
    # Crear un motor de consulta
    query_engine = index.as_query_engine()
    
    # Proporcionar respuesta detallada
    respuesta_detallada = query_engine.query(f"Proporciona una respuesta detallada sobre: {input_text}")
    
    return respuesta_detallada.response

# Función para clasificar documentos
def clasificar_documento(input_text):
    # Cargar el índice guardado
    index = VectorStoreIndex(storage_context="index")
    
    # Crear un motor de consulta
    query_engine = index.as_query_engine()
    
    # Clasificar el documento
    clasificacion = query_engine.query(f"Clasifica el siguiente texto en una categoría: {input_text}")
    
    return clasificacion.response

# Función para comparar contenido
def comparar_contenido(input_text1, input_text2):
    # Cargar el índice guardado
    index = VectorStoreIndex(storage_context="index")
    
    # Crear un motor de consulta
    query_engine = index.as_query_engine()
    
    # Comparar los textos
    comparacion = query_engine.query(f"Compara los siguientes textos: {input_text1} y {input_text2}")
    
    return comparacion.response

# Función para buscar en documentos específicos
def buscar_en_documentos_especificos(input_text, documentos):
    # Cargar el índice guardado
    index = VectorStoreIndex(storage_context="index")
    
    # Crear un motor de consulta
    query_engine = index.as_query_engine()

    # Buscar información en los documentos específicos
    respuesta = query_engine.query(f"Busca información solo en estos documentos: {documentos}. {input_text}")
    
    return respuesta.response

# Función para manejar las opciones de usuario en la interfaz
def manejar_consulta(tipo, input_text, input_text2=None, documentos=None):
    if tipo == 'chatbot':
        return chatbot(input_text)
    elif tipo == 'generar_preguntas':
        return generar_preguntas(input_text)
    elif tipo == 'generar_resumen':
        return generar_resumen(input_text)
    elif tipo == 'respuesta_detallada':
        return generar_respuesta_detallada(input_text)
    elif tipo == 'clasificar_documento':
        return clasificar_documento(input_text)
    elif tipo == 'comparar_contenido':
        return comparar_contenido(input_text, input_text2)
    elif tipo == 'buscar_en_documentos_especificos':
        return buscar_en_documentos_especificos(input_text, documentos)
    else:
        return "Opción no válida."

# Interfaz de usuario con Gradio
def interfaz_usuario(tipo, input_text, input_text2=None, documentos=None):
    return manejar_consulta(tipo, input_text, input_text2, documentos)
 
# Configuración de Gradio
iface = gr.Interface(fn=interfaz_usuario,
                     inputs=[
                         gr.Dropdown(choices=['chatbot', 'generar_preguntas', 'generar_resumen', 'respuesta_detallada', 'clasificar_documento', 'comparar_contenido', 'buscar_en_documentos_especificos'], label="Selecciona una función"),
                         gr.Textbox(lines=7, label="Texto o consulta principal"),
                         gr.Textbox(lines=7, label="Texto secundario solo para comparar contenidos"),
                         gr.Textbox(lines=7, label="Documentos específicos"),
                     ],
                     outputs="text",
                     title="Mi chatbot de IA")

# Construir el índice y lanzar la interfaz
index = construct_index("docs")
iface.launch(server_name="0.0.0.0", server_port=7860, share=True)

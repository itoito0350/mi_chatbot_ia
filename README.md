# mi_chatbot_ia
Chatbot de IA usando Gradio, LangChain y OpenAI

## Estructura del Proyecto
```
/tu-proyecto 
├── Dockerfile # Archivo para construir la imagen Docker del chatbot
├── my_chatbot.py # Script principal del chatbot, contiene la lógica y las funciones
├── requirements.txt # Lista de dependencias necesarias para ejecutar el chatbot 
└── docs/ # Carpeta que contiene los documentos utilizados para las consultas 
   └── [tus documentos aquí] # Documentos que el chatbot puede usar para responder a las consultas
```


## Requisitos

Asegúrate de tener Docker instalado en tu máquina. Para instalar Docker, puedes seguir las instrucciones en la [documentación oficial](https://docs.docker.com/get-docker/).

## Instalación y Ejecución

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```

2. **Construir la imagen Docker**:

   ```
   docker build -t my_chatbot .
   ```

3. **Ejecutar la imagen Docker**:

   ```
   docker run -p 7860:7860 my_chatbot
   ```

4. **Acceder al Chatbot**:

   Abre tu navegador y dirígete a http://localhost:7860 para interactuar con el chatbot.

## Funcionalidades

   El chatbot permite realizar las siguientes consultas:  

   - **Chatbot**: Responde a preguntas utilizando información contenida en documentos proporcionados.
   - **Generar Preguntas**: Crea preguntas sobre un texto dado.
   - **Generar Resumen**: Resume el texto proporcionado.
   - **Respuesta Detallada**: Proporciona respuestas más elaboradas sobre un tema.
   - **Clasificar Documentos**: Clasifica un texto en una categoría.
   - **Comparar Contenido**: Compara dos textos diferentes.
   - **Buscar en Documentos Específicos**: Busca información en documentos específicos.

## Requisitos de Dependencias

   El archivo requirements.txt incluye todas las bibliotecas necesarias para ejecutar el chatbot.  
   Al construir la imagen Docker, se instalarán automáticamente las dependencias.  
   ```
   llama_index
   langchain
   langchain-openai
   gradio
   openai
   ```

## Notas

   -**Asegúrate de configurar tu clave de API de OpenAI.** Puedes establecer la variable de entorno OPENAI_API_KEY dentro del contenedor si es necesario.

   -**Este proyecto es un trabajo en progreso, y se pueden agregar más funcionalidades en el futuro.**

## Contribuciones

   Las contribuciones son bienvenidas. Si tienes alguna idea o sugerencia, no dudes en abrir un issue o enviar un pull request.

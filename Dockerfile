# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script Python y la carpeta de documentos al contenedor
COPY my_chatbot.py my_chatbot.py
COPY docs/ docs/

# Exponer el puerto 7860
EXPOSE 7860

# Define el comando por defecto para ejecutar el script
CMD ["python", "my_chatbot.py"]


# Usa una imagen base con Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia todos los archivos al contenedor
COPY . .

# Expone el puerto 8050, que es el puerto por defecto para Dash
EXPOSE 8050

# Comando para ejecutar la aplicación Dash
CMD ["python", "main.py"]

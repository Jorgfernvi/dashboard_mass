# Usa la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código actual al directorio de trabajo
COPY . .

# Expone el puerto 5000 para que la aplicación esté disponible
EXPOSE 5000

# Ejecuta la aplicación cuando el contenedor se inicie
CMD ["python", "main.py"]

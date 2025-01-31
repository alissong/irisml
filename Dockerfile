FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the models directory exists
RUN mkdir -p /app/models

# Copia TUDO (incluindo a pasta app)
COPY . .  

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
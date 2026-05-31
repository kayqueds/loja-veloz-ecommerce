FROM python:3.11-slim

# Variáveis de ambiente para o Python não criar arquivos desnecessários
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências de sistema necessárias para conectar ao banco de dados (libpq-dev)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia e instala os requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expose a porta padrão do Flask/Gunicorn
EXPOSE 5000

# Executa o Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "2"]
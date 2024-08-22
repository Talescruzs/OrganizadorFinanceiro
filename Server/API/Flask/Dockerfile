# Dockerfile para o flask-api
FROM python:3.11-slim

WORKDIR /app

COPY . /app/

# Dar permissão de execução ao script
RUN chmod +x /app/wait-for-it.sh

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Usar sh para rodar o script
CMD ["sh", "-c", "./wait-for-it.sh db-finan:3306 -t 120 -- python app.py"]
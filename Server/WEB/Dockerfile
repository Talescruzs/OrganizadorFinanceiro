# Usando uma imagem leve do Python como base
FROM python:3.11-slim

# Definindo o diretório de trabalho
WORKDIR /app

COPY requirements.txt /app/

# Instalando as dependências listadas em requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiando os arquivos da aplicação para o diretório de trabalho
COPY . /app/

# Expondo a porta onde o Flask vai rodar
EXPOSE 5000

# Definindo o comando de inicialização da aplicação Flask
CMD ["sh", "-c", "python app.py"]
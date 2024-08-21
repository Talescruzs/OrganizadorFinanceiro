# Usando uma imagem leve do Python como base
FROM python:3-alpine3.15

# Definindo os argumentos de build
ARG host_name
ARG user_name
ARG user_password
ARG db_name

# Definindo as variáveis de ambiente com base nos argumentos de build
ENV DB_HOST=${host_name}
ENV DB_USER=${user_name}
ENV DB_PASSWORD=${user_password}
ENV DB_NAME=${db_name}

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos da aplicação para o diretório de trabalho
COPY . /app/

# Instalando as dependências listadas em requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expondo a porta onde o Flask vai rodar
EXPOSE 5000

# Definindo o comando de inicialização da aplicação Flask
CMD ["python", "./app.py", "$DB_HOST", "$DB_USER", "$DB_PASSWORD", "$DB_NAME"]
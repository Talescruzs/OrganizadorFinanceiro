# API

> [!NOTE]
> Em desenvolvimento!

## Comandos
1- Cria a imagem docker do banco de dados descrito no arquivo Dockerfile com nome orgfin-db:

```bash
sudo docker build -t orgfin-db .
```

2- Cria as senhas de root, usuario e cria a database do projeto

```bash
sudo docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=senha_root -e MYSQL_DATABASE=database -e MYSQL_USER=user -e MYSQL_PASSWORD=senha_usuario - orgfin-db
```

3- 
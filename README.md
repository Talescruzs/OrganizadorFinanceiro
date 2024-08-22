# OrganizadorFinanceiro

> [!NOTE]
> Em desenvolvimento!
## Sobre
### Propósito inicial
Este projeto foi idealizado com o objetivo de estudar requisições entre servidor e clientes no formato de api de dados. Bem como estudar docker, posteriormente.

Desta forma, estou utilizando um computador antigo como servidor caseiro, onde vou rodar, inicialmente, esta aplicação para ser acessada pelo meu novo computador e posteriormente pelo celular.

O plano é armazenar os dados no servidor e receber as requisições de `insert`, `select` e `delete` dos clientes.

Também foi levado em conta que o problema a ser resolvido pelo sistema me interessa e vai ajudar na organização das finanças.

### Infraestrutura
Como infraestrutura do projeto estou utilizando meu computador antigo com debian 12 isntalado, durante as tentativas de encontrar a distro ideal para ele esbarrei em um problema um tanto diferente. Quando tentava utilizar uma instalação mínima de um sistema sem interface gráfica a rede não era localizada. Desta forma, para não perder mais tempo (passei 2 dias pesquisando), resolvi instalar o Debian com Xfce. 

Mesmo com a interface gráfica, o objetivo é estudar, então estou fazendo os ajustes do servidor pelo computador novo via ssh.

## Instalação

Execute o comando

```bash
conda env create -f environment.yml
```

## Comandos

### Usuário

> [!NOTE]
> Ainda não implementado!

### Servidor

```bash
pip install mysql-connector-python
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
### Desenvolvimento

Execute

```bash
ssh Usuario@Endereço
```

Onde:

* `Usuario`: Usuário do servidor, geralmente `root`
* `Endereço`: Endereço do servidor na rede local, geralmente `192.168.xxx.xxx`

Após isso, insira a senha da conta
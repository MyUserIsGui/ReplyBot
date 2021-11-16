# ReplyBot

## Chat Bot for Telegram

### **Pré-requisitos**

Você vai precisar ter instalado em sua máquina as seguintes ferramentas:

* [Git](https://git-scm.com/)
* [Python v3.9.8](https://www.python.org/downloads/release/python-398/)
* [Mysql](https://dev.mysql.com/downloads/installer/)

**🤖 Rodando o bot localmente**

```
# Clone este repositório
$ git clone https://github.com/MyUserIsGui/ReplyBot.git

# crie o banco de dados replybot

# Importe o banco de dados
$ mysql -u user -psenha replybot < db.sql

# Instale as dependências

# Usando o PIP:
$ pip install -r requirements.txt

# renomeie o .env.example para .env e coloque suas credenciais

# Acesse a pasta do projeto no terminal/cmd
$ cd bot

# Execute a aplicação
$ python -m ReplyBot
```

## Pronto, o bot já estará rodando.

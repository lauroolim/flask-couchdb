# Flask + CouchDB Notes App

Uma aplicação web simples para gerenciar notas usando Flask e CouchDB como banco de dados NoSQL

## Pré-requisitos

- Docker
- Docker Compose

## Instalação e Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/lauroolim/flask-couchdb.git
cd flask-couchdb
```

2. **Execute com Docker Compose:**
```bash
docker-compose up --build -d
```

3. **Acesse a aplicação:**
- Web: http://localhost:5000
- CouchDB Fauxton (Interface Web): http://localhost:5984/_utils

### Comandos Úteis

```bash
# Iniciar os serviços
docker-compose up

# Iniciar com rebuild
docker-compose up --build

# Parar os serviços
docker-compose down

# Ver logs
docker-compose logs app
docker-compose logs couchdb

# Limpar volumes e containers
docker-compose down -v
```

### Executar localmente (sem Docker)

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Configure a variável de ambiente:**
```bash
export COUCHDB_URL=http://admin:root@localhost:5984/
```

3. **Execute a aplicação:**
```bash
python app.py
```

## CouchDB

O CouchDB armazena os dados em formato JSON. A estrutura básica de um documento é a seguinte:

```json
{
  "_id": "document_id",
  "_rev": "revision_id",
  "type": "user",
  "name": "teste",
  "email": "teste@teste.com",
  "created_at": "2025-06-29T12:43:02.943267Z"
}
```
obs.: O `type` pode ser `user`, `tag` ou `note` dependendo do tipo de documento

## Links Úteis

- [Flask Documentation](https://flask.palletsprojects.com/)
- [CouchDB Documentation](https://docs.couchdb.org/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
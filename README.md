# Feira API

Uma API Restful contendo todas as "feiras abertas" de São Paulo.

### Instruções:

A aplicação suporta o inject de variáveis de ambiente através de um arquivo .env no root do arquivo.

    Variáveis de ambiente suportadas:

        DATABASE_URL - Postgres String "postgres://user:pass@host:port/database"
        DEBUG - 1 ou 0
        SECRET_KEY - Controle interno do Django(Sessoes, csrf, etc)
        LOG_LEVEL - Level do log
        WORKERS - Número de workers gunicorn

- [Python 3.6 +](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Docker-Compose](https://docs.docker.com/compose/)
- [Documentação](./docs/api.apib)

- Ambiente local:

        feiras:/$ sudo docker-compose up -d
        feiras:/$ firefox localhost:8000/api

- Carregar fixtures:

        feiras:/$ sudo docker-compose exec api make dump_data

- Testes:

        feiras:/$ sudo docker-compose exec api make test

- Formatação, lint:

        feiras:/$ sudo docker-compose exec api make lint
        feiras:/$ sudo docker-compose exec api make format
        feiras:/$ sudo docker-compose exec api make sort



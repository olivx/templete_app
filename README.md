# Feira API
### Projeto modelo para ser seguido em outros apps

Uma API Restful contendo todas as "feiras abertas" de São Paulo.

### Instruções:

A aplicação suporta o inject de variáveis de ambiente através de um arquivo .env no root do projeto.

    Variáveis de ambiente necessárias:

        DATABASE_URL(obrigatório) - Postgres String "postgres://user:pass@host:port/database"
        SECRET_KEY(obrigatório) - Controle interno do Django(Sessoes, csrf, etc)
        WORKERS(obrigatório) - Número de workers gunicorn
        DEBUG(opcional, default 0) - 1 ou 0
        LOG_LEVEL(opcional, default INFO) - Level do log

Os logs são direcionados para stdout e /var/log/app/gunicorn.log e /var/log/app/app.log

- [Python 3.6 +](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Docker-Compose](https://docs.docker.com/compose/)

- Documentação:
    - [Blueprint](./docs/api.apib)
    - [Html](./docs/api.html)
    - [Postman](.docs/api.postman_collection.json)

- Ambiente local:

        feiras:/$ sudo docker-compose up -d
        feiras:/$ firefox localhost:8000/api

- Carregar fixtures:

        feiras:/$ docker-compose run --entrypoint=make api dump_data

- Testes:

        feiras:/$ docker-compose run --entrypoint=make api test
        feiras:/$ docker-compose run --entrypoint=pytest api -k ".*textpattern" <- roda test específico

- Formatação, lint:

        feiras:/$ docker-compose run --entrypoint=make api lint
        feiras:/$ docker-compose run --entrypoint=make api format
        feiras:/$ docker-compose run --entrypoint=make api sort

- Gerar documentação:

        feiras:/$ docker-compose run --entrypoint=make api doc

- Terminal interativo:

        feiras:/$ docker-compose exec api bash

- Desencriptar os secrets do k8s:
[kubesec](https://github.com/shyiko/kubesec#installation) 

        kubesec decrypt k8s/secret-postgres.yml -o k8s/secret-postgres.yml -- Necessário possuir a chave privada de desencriptação
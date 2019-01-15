FROM python:3.6-alpine

COPY . /app

WORKDIR /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev

# RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
#     py-gdal gdal-dev geos geos-dev linux-headers

RUN sh -c "pip install -r requirements.txt"

RUN apk del build-deps

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

USER appuser

CMD ["sh", "-c", "/usr/local/bin/gunicorn --access-logfile - -b 0.0.0.0:8000 feira.wsgi"]

EXPOSE 8000
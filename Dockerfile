FROM python:3.7.3-slim-stretch

COPY . /app

WORKDIR /app

RUN pip install pipenv && \
    pipenv install --system --deploy

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

RUN mkdir /var/log/app && chown appuser /var/log/app

USER appuser

ENTRYPOINT ["gunicorn", "-c", "gunicorn.py", "feira.wsgi"]

EXPOSE 8000
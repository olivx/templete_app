SHELL := /bin/sh

doc:
	snowboard html -o docs/api.html docs/api.apib
	vanadia --input docs/api.apib --output docs/api.postman_collection.json

clean:
	@rm -f .coverage 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@find . -name "__pycache__" -delete

format:
	@black api

sort:
	@isort

lint:
	@flake8 api

test: clean lint
	@black --check api
	@isort -c
	python -m pytest --cov=api --cov=feira

dump_data:
	python manage.py load_data -f DEINFO_AB_FEIRASLIVRES_2014.csv
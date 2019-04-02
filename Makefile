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
	python -m pytest template_app --cov=api,feira
SHELL := /bin/sh

docs:
	aglio -i api.apib -o docs.html

clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;

test:
	pytest

format:
	black .

lint:
	flake8 .

sort:
	isort

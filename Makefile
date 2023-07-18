install:
	poetry install

test:
	poetry run pytest -vv -s

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

check: test lint

build:
	poetry build

publish:
	poetry publish --dry-run

run:
	poetry run gendiff -- -h

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	pip uninstall hexlet-code

.PHONY: install test lint check build

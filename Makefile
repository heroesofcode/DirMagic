setup: ## Dependencies
	poetry update
	poetry install
	poetry shell

inspect: ## Run code analysis
	poetry run flake8 dir_magic tests

test: ## Run tests
	poetry run pytest -vv --cov-report=xml --cov=dir_magic tests/

build: ## Run build
	poetry build

deploy: ## Deploy package
	poetry config pypi-token.pypi $(token)
	poetry build
	poetry publish

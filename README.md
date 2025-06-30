# SMCP Cash Register

Une petite bibliothèque Python pour simuler une caisse enregistreuse.

## Poetry Installation

```bash
brew install poetry
pipx install poetry
poetry init
```

## Run unit tests

```bash
poetry run pytest --cov=cash_register --cov-report=term-missing -ra
```

## Lint & Formatting

```bash
poetry run black cash_register tests
poetry run isort cash_register tests
poetry run flake8
```

## Static types
```bash
poetry run mypy cash_register
```
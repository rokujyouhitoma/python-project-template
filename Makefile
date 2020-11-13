PYTHON=poetry run python
SRC=src
TESTS=tests

all: clean format static_analysis test run

.PHONY: help
help: ## help command
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## clean
	echo "clean"

.PHONY: format
format: isort black flake8 ## execute format

.PHONY: static_analysis
static_analysis: xenon mypy ## static analysis

.PHONY: test
test: pytest ## pytest

.PHONY: run
run: ## run python code
	${PYTHON} ${SRC}/parser.py

.PHONY: isort
isort: ## isort
	isort ${SRC}

.PHONY: black
black: ## black
	black ${SRC}

.PHONY: flake8
flake8: ## flake8
	flake8 ${SRC}

.PHONY: xenon
xenon: ## xenon
	xenon --max-absolute A --max-modules A --max-average A ${SRC}

.PHONY: mypy
mypy: ## mypy
	mypy ${SRC}

.PHONY: pytest
pytest: ## pytest
	PYTHONPATH=${SRC} pytest --cov=${SRC} --cov-fail-under=70 -v ${TESTS} --cov-report=term-missing -n 2

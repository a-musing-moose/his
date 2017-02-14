.PHONY: flake8 isort mypy pytest test

flake8:
	flake8 almanac/

isort:
	isort --recursive --check-only --quiet almanac/

mypy:
	mypy --ignore-missing-imports --fast-parser almanac/

pytest:
	py.test --spec --cov=almanac tests


test: flake8 isort mypy pytest

build: test
	python setup.py bdist_wheel


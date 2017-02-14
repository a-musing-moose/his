.PHONY: flake8 isort mypy pytest test build run

flake8:
	flake8 src/

isort:
	isort --recursive --check-only --quiet src/

mypy:
	mypy --ignore-missing-imports --fast-parser src/

pytest:
	py.test --spec --cov=src/shopping --cov=src/wamp src

test: flake8 isort mypy

build: test
	cp ../../shared/almanac/dist/his.almanac-0.0.1-py3-none-any.whl .
	docker build -t his/shopping .
	rm his.almanac-0.0.1-py3-none-any.whl

run: build
	docker run --rm --network=his_default -e AUTOBAHN_ROUTER="wss://crossbar:8080/ws" his/shopping



.PHONY: run build shell

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

build:
	docker-compose build

up:
	docker-compose up

up-build:
	docker-compose up --build

shell:
	docker-compose exec app bash

.PHONY: install test run deploy clean

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

run-api:
	PYTHONPATH=./src python src/app.py

run-docker:
	docker-compose up --build

deploy-ibm:
	chmod +x deploy_ibm_cloud.sh
	./deploy_ibm_cloud.sh

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info/

format:
	black src/ tests/
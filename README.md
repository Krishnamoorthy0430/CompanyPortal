
# company-portal (in-memory demo)

This is a small FastAPI demo application that exposes CRUD endpoints for a simple Employee resource. Data is stored in-memory (non-persistent) and is intended for development/testing.

Quick start (Windows cmd.exe):

1. Create a virtual environment and activate it:

	python -m venv .venv
	.venv\Scripts\activate

2. Install requirements:

	pip install -r requirements.txt

3. Run the app:

	python -m app.main

The API will be available at http://127.0.0.1:8000 and OpenAPI docs at http://127.0.0.1:8000/docs

4. Run tests:

	pytest -q

Notes:
- Storage is in-memory and will be lost when the process exits.
- This repository is intentionally simple and focuses on illustrating logging, a clean folder layout, and basic CRUD.


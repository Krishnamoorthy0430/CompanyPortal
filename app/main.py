from fastapi import FastAPI
import logging

from app.controller import router
from app.config.logging_config import setup_logging


def create_app() -> FastAPI:
	setup_logging()
	app = FastAPI(title="company-portal")
	app.include_router(router.router)

	@app.get("/", tags=["root"])
	def read_root():
		return {"service": "company-portal", "status": "ok"}

	return app


app = create_app()

if __name__ == "__main__":
	# Handy local runner: `python -m app.main`
	import uvicorn

	logging.getLogger("uvicorn").setLevel(logging.INFO)
	uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="info")


from fastapi import FastAPI
import logging
from app.controller import router
from app.config.logging_config import setup_logging
import uvicorn

	# When running locally we still configure logging early so the console
	# output is readable. Uvicorn will call the startup event when it runs
	# with the module as an application.
setup_logging()
logging.getLogger("uvicorn").setLevel(logging.INFO)

def create_app() -> FastAPI:
	"""Create and return the FastAPI application.

	Note: we avoid configuring logging at import time so `uvicorn app.main:app`
	can safely import this module. Logging is configured during application
	startup instead.
	"""
	app = FastAPI(title="company-portal")
	app.include_router(router.router)

	@app.get("/", tags=["root"])
	def read_root():
		return {"service": "company-portal", "status": "ok"}

	# Configure logging when the app starts (uvicorn triggers startup events).
	@app.on_event("startup")
	def _startup_config():
		# Use default INFO level; setup_logging is idempotent for repeated calls.
		setup_logging()

	return app

app = create_app()

if __name__ == "__main__":
	# Handy local runner: `python -m app.main`
	# Run using the app object directly.
	uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


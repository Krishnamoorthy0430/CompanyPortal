from fastapi import FastAPI
import logging
from app.controller.router import router
from app.config.logging_config import setup_logging
from app.middleware import BeautifyMiddleware
import uvicorn

	# When running locally we still configure logging early so the console
	# output is readable. Uvicorn will call the startup event when it runs
	# with the module as an application.
setup_logging()
# Enable detailed access logging
logging.getLogger("uvicorn.access").setLevel(logging.INFO)
logging.getLogger("uvicorn.error").setLevel(logging.INFO)


app = FastAPI(title="company-portal")

# Add middleware
middleware = BeautifyMiddleware()
app.middleware("http")(middleware)

# Include router
app.include_router(router, prefix="/api")

@app.get("/", tags=["root"])
def read_root():
	return {"service": "company-portal", "status": "ok"}

@app.get("/status")
def get_status():
    return {"status": "running", "version": "1.0"}


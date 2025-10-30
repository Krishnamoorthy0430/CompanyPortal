from fastapi import FastAPI
import logging
from pathlib import Path
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

def print_project_structure():
    # Get current working directory (root of your app)
    root_path = Path.cwd()
    print(f"\n🔍 Current working directory: {root_path}")

    # List all files and folders in the root directory
    print("\n📁 Contents of root folder:")
    for item in root_path.iterdir():
        if item.is_dir():
            print(f"   📂 {item.name}/")
        else:
            print(f"   📄 {item.name}")

    # Get parent directory
    parent_path = root_path.parent
    print(f"\n⬆️ Parent directory: {parent_path}")

    # List all files and folders in parent directory
    print("\n📁 Contents of parent folder:")
    for item in parent_path.iterdir():
        if item.is_dir():
            print(f"   📂 {item.name}/")
        else:
            print(f"   📄 {item.name}")

    print("\n✅ Directory listing complete.\n")

# Call it when app starts
print_project_structure()

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


# ---------- Base Image ----------
FROM python:3.11-slim

# ---------- Set working directory ----------
WORKDIR /company_portal_service

# ---------- Copy dependency file ----------
COPY requirements.txt .

# ---------- Install dependencies ----------
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy only necessary files ----------
# (adjust these according to your project structure)
COPY main.py .
COPY app/ ./app

# ---------- Expose FastAPI port ----------
EXPOSE 8000

# ---------- Default command ----------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

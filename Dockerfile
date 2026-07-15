# Deliberately old base image — carries known OS-level CVEs
FROM python:3.6-slim-buster

WORKDIR /app

# Install the intentionally outdated dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]

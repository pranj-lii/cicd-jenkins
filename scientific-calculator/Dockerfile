FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create data directory
RUN mkdir -p /app/data

CMD ["python", "app.py"]

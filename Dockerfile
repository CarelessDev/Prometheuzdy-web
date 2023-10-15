FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy App directory
COPY main.py .
COPY ./app /app/app

EXPOSE 8000

# Create environment folder
RUN mkdir -p environments

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

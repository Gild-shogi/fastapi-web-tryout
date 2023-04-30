FROM python:3.11-slim

WORKDIR /app

COPY ./app/ .
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

EXPOSE 8080
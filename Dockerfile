FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/src \
    FLASK_APP=interface.api_app \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

EXPOSE 5000

CMD ["flask", "run"]

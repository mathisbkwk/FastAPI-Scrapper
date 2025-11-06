FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8888

WORKDIR /app

RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential gcc \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
	&& pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN useradd -m appuser || true \
	&& chown -R appuser:appuser /app
USER appuser

EXPOSE ${PORT}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888", "--proxy-headers", "--workers", "1"]

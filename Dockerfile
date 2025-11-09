FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential gcc curl \
	&& curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
	&& rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.cargo/bin:${PATH}"

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip \
	&& python -m pip install --prefix /install -r /app/requirements.txt

COPY src /app/src

FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PORT=8888

WORKDIR /app

COPY --from=builder /install /usr/local

COPY src /app/src

RUN useradd -m appuser || true \
	&& chown -R appuser:appuser /app
USER appuser

EXPOSE ${PORT}

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8888", "--proxy-headers", "--workers", "1"]

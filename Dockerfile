FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git perl && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x /app/.github/scripts/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/.github/scripts/entrypoint.sh"]

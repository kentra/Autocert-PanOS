FROM ghcr.io/astral-sh/uv:alpine3.22


RUN apk update && apk add bash curl openssl
# Copy the project into the image
ADD . /app

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

CMD ["sh"]
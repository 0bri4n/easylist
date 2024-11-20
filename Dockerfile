FROM python:3.13-slim-bookworm AS backend
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

COPY pyproject.toml uv.lock ./ 
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

COPY . . 
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

CMD ["uv", "run", "uvicorn", "easylist.api.server:app", "--host", "0.0.0.0", "--port", "8000"]

FROM oven/bun:latest AS frontend
WORKDIR /web

COPY easylist/web/package.json easylist/web/bun.lockb ./
RUN bun install

COPY easylist/web ./

ENV WEB_PORT=3000
EXPOSE $WEB_PORT

CMD ["bun", "dev"]

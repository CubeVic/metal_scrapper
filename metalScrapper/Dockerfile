
FROM        python:3.10 AS python-base

ENV         POETRY_VERSION=1.2.2
ENV         POETRY_HOME=/opt/poetry
ENV         POETRY_VENV=/opt/poetry-venv
ENV         POETRY_CACHE_DIR=/opt/.cahce

###

FROM        python-base AS poetry-base

RUN         python3 -m venv $POETRY_VENV \
	          && $POETRY_VENV/bin/pip install -U pip setuptools \
	          && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

###

FROM        python-base AS Application

COPY        --from=poetry-base ${POETRY_VENV}   ${POETRY_VENV}

ENV         PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR     /app

COPY        poetry.lock pyproject.toml  ./

RUN         poetry check

RUN         poetry install -vv -n --no-dev --no-root --remove-untracked

COPY        .   /app

ENTRYPOINT  ["poetry"]
CMD         ["run", "scrapy", "crawl", "kitco"]

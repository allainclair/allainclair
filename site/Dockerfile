# syntax=docker/dockerfile:1

FROM python:3.12.3-slim-bookworm AS base-python
WORKDIR /app


FROM python:3.12.3-slim-bookworm AS base
WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
      curl \
    && curl -sSL https://pdm-project.org/install-pdm.py > install-pdm.py \
      && python3 install-pdm.py -p /usr \
      && rm install-pdm.py \
      && apt-get remove -y curl && apt-get autoremove -y

COPY ${BASE_DIR}/pyproject.toml .


FROM base AS base-tests
RUN pdm update -dG "test"
COPY app app
COPY tests tests
#COPY _tests _tests


FROM base AS base-lint
RUN pdm update -dG "test,lint"
COPY app app
COPY tests tests
#COPY _tests _tests


FROM base AS base-requirements
# RUN pdm install --global --prod  # Not working
RUN pdm lock --prod  && \
    pdm export --prod -o requirements.txt


FROM base-python AS base-run
COPY app app
COPY --from=base-requirements ["/app/requirements.txt", "."]
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt


FROM base-lint AS lint-run
ENTRYPOINT ["pdm", "run", "lint"]


FROM base-tests AS tests-run
ENTRYPOINT ["pdm", "run", "cov"]


FROM base-lint AS lint-tests-run
ENTRYPOINT ["pdm", "run", "lint-test"]


FROM base-run AS dev
EXPOSE 8000
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "app.main:app", "--reload"]


FROM base-run AS prod
COPY .env .env
EXPOSE 8000
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]

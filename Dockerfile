FROM python:3.12-rc-bullseye AS kecal-base
WORKDIR /src
COPY pyproject.toml /src/pyproject.toml
COPY . .
RUN pip install -e .

FROM kecal-base AS kecal-tester
RUN pip install -e .[dev]
# stop the build if there are Python syntax errors or undefined names
RUN flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
RUN flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
RUN pytest

FROM kecal-base AS kecal-server
ENTRYPOINT [ "kecal-server" ]

FROM kecal-base AS kecal-client
ENTRYPOINT [ "kecal-client" ]

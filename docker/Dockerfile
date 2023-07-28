FROM archlinux:latest

RUN pacman -Syu --noconfirm

RUN pacman -S git curl python3 python-pip --noconfirm

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry --version

COPY pyproject.toml ./

RUN poetry config virtualenvs.create false

RUN poetry install

COPY src/tools ./tools


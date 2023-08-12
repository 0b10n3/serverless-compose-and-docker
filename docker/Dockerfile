FROM amazon/aws-lambda-python:3.11 

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR ${LAMBDA_TASK_ROOT}

COPY pyproject.toml ./

RUN poetry config virtualenvs.create false

RUN poetry install

RUN mkdir tools
COPY src/tools/ ./tools


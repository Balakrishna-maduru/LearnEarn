ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

ARG APP_DIR
ARG REQ_FILE

WORKDIR ${APP_DIR}

COPY ${REQ_FILE} ./
RUN pip install --no-cache-dir -r ${REQ_FILE}

CMD [ "python", "generate_report.py" ]

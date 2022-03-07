ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

ARG DAGSTER_HOME
ARG REQ_FILE

RUN mkdir -p ${DAGSTER_HOME}
ENV DAGSTER_HOME=${DAGSTER_HOME}
WORKDIR ${DAGSTER_HOME}


COPY ${REQ_FILE} ./
RUN pip install --no-cache-dir -r ${REQ_FILE}
RUN pip install dagit dagster-postgres

EXPOSE 3000
ENTRYPOINT ["dagit", "-h", "0.0.0.0", "-p", "3000"]
FROM python:3.8
				
RUN pip install flask flask-restful flask-limiter sqlalchemy psycopg2-binary scipy gunicorn==19.10.0 jsonschema pyyaml tabulate structlog pandas==0.25.3 argparse inflection flasgger simplejson tx-functional==0.1.2 numpy statsmodels==0.12.0 pydantic==1.6.1
RUN mkdir icees-api
COPY ./requirements.txt /icees-api/requirements.txt

RUN pip install -r icees-api/requirements.txt

COPY ./app.py /icees-api/app.py
COPY ./handlers.py /icees-api/handlers.py
COPY ./models.py /icees-api/models.py
COPY ./dependencies.py /icees-api/dependencies.py
COPY ./db.py /icees-api/db.py
COPY ./utils.py /icees-api/utils.py
COPY ./terms.txt /icees-api/terms.txt
COPY ./TranslatorReasonersAPI.yaml /icees-api/TranslatorReasonersAPI.yaml
COPY ./features /icees-api/features
COPY ./examples icees-api/examples
COPY ./static /icees-api/static
COPY ./main.sh /icees-api/main.sh

WORKDIR /icees-api

CMD ["./main.sh"]

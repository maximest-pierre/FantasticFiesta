FROM python:3.6-alpine3.7

RUN apk add --no-cache \
    linux-headers \
    bash \
    gcc \
    musl-dev \
    libjpeg \
    libpng \
    libpq \
    gettext \
    postgresql-client \
    postgresql-dev \
    uwsgi \
    uwsgi-python3

WORKDIR /code
COPY ./ /code/

RUN pip3 install -r requirements.txt

CMD ["/code/util/run.sh"]
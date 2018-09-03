# Build assets
FROM node:8-alpine AS build

ARG prod=0

WORKDIR /code
COPY ./ /code/

RUN npm install

RUN npm rebuild node-sass

RUN npm run-script build

# Build the app container
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
COPY --from=build /code/assets/output /code/assets/output

RUN pip3 install -r requirements.txt

CMD ["/code/util/run.sh"]
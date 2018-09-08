# FantasticFiesta
[![Build Status](https://travis-ci.org/maximest-pierre/FantasticFiesta.svg?branch=master)](https://travis-ci.org/maximest-pierre/FantasticFiesta)
[![Maintainability](https://api.codeclimate.com/v1/badges/06d430c92fcc868c3377/maintainability)](https://codeclimate.com/github/maximest-pierre/FantasticFiesta/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/maximest-pierre/FantasticFiesta/badge.svg?branch=master)](https://coveralls.io/github/maximest-pierre/FantasticFiesta?branch=master)
## Running the application

### Requirements
- Docker engine
- Docker-Compose

### Running the application

```docker-compose build && docker-compose up```

The application should now be running

### Creating the super user

* `docker exec -it fantasticfiesta_web_1 bash`
* `python3 manage.py createsuperuser`

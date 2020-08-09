# Production-ready REST API in Flask

## Usage

### Install and run locally

* Create python3 virtual environment and activate it

      python3 -m venv venv
      source venv/bin/activate

* Install requirements

      pip install -r sample_project/requirements.txt

* Run development server

      python run.py

  You will find the development server starting like this:

         * Serving Flask app "sample_project.app" (lazy loading)
         * Environment: production
           WARNING: Do not use the development server in a production environment.
           Use a production WSGI server instead.
         * Debug mode: on
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: ...

* View the Swagger API docs in your browser:

   http://localhost:5000/sample_project/api/v1.0/doc/

* Static code analysis - run this command:

      flake8

* Run unit tests

      pytest .

* Generate test case coverage

      coverage run -m pytest && coverage report --omit='*lib/*.py,*test_*.py'
      coverage xml -i


## Running on docker

* Build image and run

      docker build -t project:1 .
      docker run --name project --env-file .env -d -p 8000:8000 project:1

* View Swagger API docs in the browser

  http://localhost:8000/sample_project/api/v1.0/doc/

* Run tests in the docker container

      docker exec -it project bash
      pytest .


## Features

### 1. Modular application ([application factory](https://flask.palletsprojects.com/en/master/patterns/appfactories/) & [blueprint](https://flask.palletsprojects.com/en/master/blueprints/))

Has a `create_app` function that can be passed the environment (dev, test, prod). Environments can be be defined in the `config.py` .

APIs for a particular version are packed into a blueprint. There is also a blueprint for a healthcheck URL.
These blueprints are registered in `create_app` and the URL prefixes can be customised there:

        app.register_blueprint(api, url_prefix=ROOT_URL + '/api/v1.0')
        app.register_blueprint(healthcheck, url_prefix=ROOT_URL + '/version')

### 2. REST APIs (Flask-restx, previously flask-resplus)

> Flask-RESTX is an extension for Flask ... Flask-RESTX encourages best practices with minimal setup... collection of
> decorators and tools to describe your API and expose its documentation properly (using Swagger).

The Swagger docs can be hosted at required path using `API_DOCS_URL` or can be disabled by setting its value to `False`.
Check out `config.py` for more examples.

### 3. Unit testing (flask-testing)

Defines `AppTestCase` in `sample_project.tests.conftest.py`. Tests can be found at `person.v1.test_views.py` and `user.v1.test_views.py`

**Structure**

### 4. WSGI app for hosting on production

Can be run using `gunicorn` like this:

    gunicorn -c gunicorn_config.py wsgi:app

If your application is hosted behind a reverse proxy like NGINX, the `X-Forwareded-*` headers can be corrected using
werkzeug's [ProxyFix](https://werkzeug.palletsprojects.com/en/1.0.x/middleware/proxy_fix/). This has already been done
in `wsgi.py`

### 5. Structure of the project

```
sample_project/
├── api_v1.py                     # Api() object associated to Blueprint() object, person and user namespaces are added to this
├── app.py                        # Flask() object, with blueprints registered
├── config.py
├── healthcheck.py
├── __init__.py
├── person
│         ├── __init__.py
│         └── v1                  # Namespace() object for person
│             ├── __init__.py
│             ├── test_views.py
│             └── views.py        # Resource() objects associated to person namespace
├── requirements.txt
├── tests
│         ├── conftest.py
│         └── __init__.py
└── user
    ├── __init__.py
    └── v1                       # Namespace() object for user
        ├── __init__.py
        ├── test_views.py
        └── views.py             # Resource() objects associated to user namespace
```

This layout explains an optimal way to use flask-restx with blueprints.

* Many `Resource`s are linked to a `Namespace`. A namespace pertains to URLs for a particular
model (say, person) and API version (say v1.0).
* For an API version, say v1.0 an `Api` instance is created and attached to a `Blueprint` for that versoin.
* All `Namespace`s for a specific API version are added to the previously created `Api`.
* All the `Blueprint`s are registered with the `Flask()` object in `app.py`.
`sample_project.api_v1`
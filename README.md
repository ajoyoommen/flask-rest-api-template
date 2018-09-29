# Flask starter project

## Deploying on docker

### Build and run the python service in Docker

    docker build -t project:1 .
    docker run --name project --env-file .env -d -p 8000:8000 project:1

### View restplus docs in the browser

    http://localhost:8000/sample_project/api/v1.0/doc/

### Run tests in the docker container

    docker exec -it project bash
    pytest .


## Running locally

### Install and run local server

* Create python3.6.6 virtual environment
* Activate new virtual evironment
*  Install requirements

        pip install -r sample_project/requirements.txt

* Run development server

        python run.py

### View restplus docs in the browser

    http://localhost:5000/sample_project/api/v1.0/doc/

### Static code analysis command

    flake8

### Run tests

    pytest .

### Generate test case coverage

    coverage run -m pytest && coverage report --omit='*lib/*.py,*test_*.py'
    coverage xml -i

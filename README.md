
# Wet My Plants Backend
![fastapi-0.108.0-informational](https://img.shields.io/badge/fastapi-0.108.0-informational) 

A Dockerized API Server and Database built using FastAPI and PostgreSQL

## Installation method: Docker

1. Ensure [Docker](https://docs.docker.com/install/) is installed.

2. Ensure [Docker Compose](https://docs.docker.com/compose/install/) is installed.

3. Clone this Repo

   `git clone https://github.com/dunbar-brett/wet-my-plants-api-v2.git`

4. Change into the directory

   ```cd wet-my-plants-api-v2```

5. Use Docker-Compose to spin up containers

   `docker-compose up -d --build`

6. If everything completes should be available on [wet-my-plants-api](http://127.0.0.1:8000)

7. Docs are generated on [docs](http://127.0.0.1:8000/docs)

## Installation method: Local

1. Clone this Repo

   `git clone https://github.com/dunbar-brett/wet-my-plants-api-v2.git`
2. Cd into the project folder

   `cd wet-my-plants-api-v2`
3. Create a virtual environment

   `python3 -m venv venv`
4. Activate virtualenv

   `source venv/bin/activate`

   For zsh users

   `source venv/bin/activate.zsh`

   For bash users

   `source venv/bin/activate.bash`
5. Install the required packages

   `python -m pip install -r requirements.txt`
6. Start the app using Uvicorn

   ```shell
   uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
   ```

8. Ensure you have a Postgres Database running locally.
   Additionally create a `fast_api_dev` database with user `**fast_api**` having required privileges.
   OR
   Duplicate the `**example.env**`, remove `example`. Change the Database variables in the **.env** file
   AND
   You can login to [pgadmin](http://127.0.0.1:16543/) using the credentials in `**.env***`

9. Check the app on [wet-my-plants-api](http://127.0.0.1:8000/)
Open your browser and navigate to [docs](http://127.0.0.1:8000/docs) to view the swagger documentation for the api.


## Gotchas

1. For alembic migrations and other commands with docker run `docker-compose run server alembic YOUR-COMMAND-HERE`  
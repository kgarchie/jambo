# Jambo

## Introduction

This project was made for the sole purpose of submission and assessment to [JamboPay](https://jambopay.com/v2).

Chosen stack: <br>
&nbsp; &nbsp; 1. Django - Django Rest Framework <br>
&nbsp; &nbsp; 2. Vitepress - For Documentation <br>
&nbsp; &nbsp; 3. Docker & Shell - For Containerization <br>
&nbsp; &nbsp; 4. Postgres - For Database <br>
&nbsp; &nbsp; 5. Redis - For Caching <br>
&nbsp; &nbsp; 6. GitHub - For Version Control <br>
&nbsp; &nbsp; 7. GitHub Actions - For Deployment (Docs only) <br>
&nbsp; &nbsp; 8. Nginx - For Reverse Proxy <br>

A thorough documentation of the API is online [here](https://kgarchie.github.io/jambo/).

Alternatively, the [docs/](./docs) folder is [vitepress](https://vitepress.dev/) powered and can be served locally
by using the following command in that directory.

```bash
pnpm run docs:dev
```

This is done automagically when running the server and is accessible
via [http://localhost/docs](http://localhost/docs).
You may as well just skim the raw markdown files in the [docs/](./docs) folder should you wish to.

## Installation

You can install this project in two ways, either via Docker or via Shell Scripting.

### Docker (Recommended)

I have provided a [Docker Compose](./docker-compose.yml) for the easiest deployment.
This however is only suitable if your computer is powerful enough to run the containers.

#### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) - You need docker installed.

Then run the following command in the root directory of the project.

```bash
docker-compose up
```

This will spin up all the needed containers and the default django-rest-framework API is accessible
via [http://localhost/api/](http://localhost/api/).

### Shell Scripting

I have also provided a [shell script](./run.sh) for easy non-docker deployment.
This time however, you need to have the following installed:

### Prerequisites

- [Python 3](https://www.python.org/downloads/) - You need at least python 3.10 installed. Due to the use of type hints
- [Node](https://nodejs.org/en/download/) - You need node installed. This is for the documentation.
- [Postgres](https://www.postgresql.org/download/) - You need postgres installed. Make sure there exists a database
  named `jambo`.
- [Redis](https://redis.io/download) - Optional, could be run as a container, wsl or vm
- Nginx is not implemented for Windows due to known issues - Skip

Then run the following command in the root directory of the project.

##### Linux

```bash
chmod +x run.sh && ./run.sh
```

##### Windows

```shell
./run.bat
````

**NB:** You may run into an Execution-Policy error on Windows, in that case, you need to execute the following command
in an admin window before retrying the step above in a fresh window again.

```shell
Set-ExecutionPolicy RemoteSigned
```

## Testing

I have included tests to ensure the API is working as expected.
Running tests can be done via the following command once the server is up

```shell
python manage.py test
```
# Quickstart

## Introduction

Howdy, how's the weather?

These docs are also available in the [docs/](./docs) folder of the project, it's [vitepress](https://vitepress.dev/)
powered and can be served locally
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
  whose URI string should be added to the `.env`.
- [Redis](https://redis.io/download) - Optional, could be run as a container, wsl or vm
- Nginx is not implemented outside docker due to known issues - Skip

Then run the following command in the root directory of the project.

##### Linux

```bash
chmod +x run.sh && ./run.sh
```

##### Windows

```shell
./run.bat
````

::: info
You may run into an Execution-Policy error on Windows, in that case, you need to execute the following command
in an admin window before retrying the step above in a fresh window again.
See [this](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4#:~:text=Copy-,Set%2DExecutionPolicy%20%2DExecutionPolicy%20RemoteSigned%20%2DScope%20LocalMachine,-Get%2DExecutionPolicy%20%2DList)
:::

```shell
Set-ExecutionPolicy RemoteSigned
```

## Secrets

Environment variables should be stored in a `.env` file in the root directory of the project. You can rename
the `.env.example` file to `.env` and fill in the necessary details. It's rudimentary and self-documented with comments.

You will notice that if the app will create a `SECRET_KEY` for you and store it in the `.env` file if you don't provide
one. This is not recommended for
production, so always define a `SECRET_KEY` in your `.env` file or environment. The `SECRET_KEY` is used for hashing and
encryption. It's just a long random string, can be anything.

## Testing

I have included tests to ensure the API is working as expected.
Running tests can be done via the following command once the server is up

```shell
python manage.py test
```

::: info
I used Faker for data generation, so there is a non-zero chance that some primary keys may clash.
If this happens, just run the tests again.
:::

::: warning
You need Redis running for the tests to pass.
:::

::: danger
Do not use Pycharm's built in test runner or debugger as it won't initialise settings and environment
variable therein properly
:::

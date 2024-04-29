# Quickstart

## Introduction

Howdy, how's the weather?

These docs are also available in the [docs/](https://github.com/kgarchie/jambo/tree/main/docs) folder of the project,
it's [vitepress](https://vitepress.dev/)
powered and can be served locally by using the following command in that directory.

```bash
pnpm run docs:dev
```

This is done automagically when running the server and is accessible
via http://localhost/jambo for or http://localhost:5173/jambo.
You may as well just skim the raw markdown files in the [docs/](https://github.com/kgarchie/jambo/tree/main/docs) folder
should you wish to.

Here's the PostMan collection:
[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/15264165-ff91f75b-81bb-4bda-b45e-24002ddad076?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D15264165-ff91f75b-81bb-4bda-b45e-24002ddad076%26entityType%3Dcollection%26workspaceId%3D91d100e3-340c-4dbd-b05b-e5eabbc100e7)

## Installation

You can install this project in two ways, either via Docker or via Shell Scripting.

### Docker (Recommended)

I have provided a [Docker Compose](./docker-compose.yml) for the easiest deployment.

#### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) - You need docker installed.

Then run the following command in the root directory of the project.

```bash
docker-compose up
```

This will spin up all the needed containers and the default django-rest-framework API is accessible
via http://localhost:{port}/api/. The port is determined by whether it's in docker or not. (Should be absent for docker)

### Shell Scripting

I have also provided a [shell script](https://github.com/kgarchie/jambo/tree/main/docs) for easy non-docker deployment.
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

Environment variables should be stored in a `.env` and a `.env.docker`(used in docker) file in the root directory of the
project. You can rename the `.env.example` file to `.env` and `.env.docker.example` to `.env.docker` for containerized environments, then fill in the
necessary details. It's rudimentary and self-documented with comments.

You will notice that if the app will create a `SECRET_KEY` for you and store it in the `.env` file if you don't provide
one. This is not recommended for
production, so always define a `SECRET_KEY` in your `.env` file or environment. The `SECRET_KEY` is used for hashing and
encryption. It's just a long random string, can be anything.

## Testing

I have included tests to ensure the API is working as expected.
Running tests can be done via the following command once the server is up

<video width="100%" controls muted>
    <source src="../media/video/tests_passing.mp4" type="video/mp4">
</video>

```shell
python manage.py test
```

::: danger
Do not use PyCharm's built in test runner or debugger as it won't initialise settings and environment
variable therein properly
:::

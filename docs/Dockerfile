FROM node:20.11-bullseye

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

RUN corepack enable

COPY . /app/

RUN pnpm install \
    && pnpm docs:build \
    && pnpm prune


EXPOSE 4173

CMD [ "pnpm", "run", "docs:preview", "--host" ]
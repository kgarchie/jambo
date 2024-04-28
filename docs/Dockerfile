FROM node:20.11-bullseye

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

RUN corepack enable

COPY . /app/

RUN pnpm install \
    && pnpm prune


EXPOSE 5173

CMD [ "pnpm", "run", "docs:dev" ]
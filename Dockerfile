FROM node:alpine


WORKDIR /app
COPY templates/package.json /app

RUN npm install
COPY . /app

CMD [ "npm", "start" ]

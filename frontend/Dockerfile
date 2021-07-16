FROM node

WORKDIR /app/frontend
COPY package*.json ./
EXPOSE 3000
RUN npm install

COPY . .

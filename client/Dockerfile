FROM nginx:latest

WORKDIR /app

# Копируем собранные файлы фронтенда
COPY ./dist /app/static

# Копируем файл конфигурации Nginx
COPY ./nginx.conf /etc/nginx/nginx.conf

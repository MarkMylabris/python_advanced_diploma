# Проект «Корпоративный сервис микроблогов»

## Описание

Это бэкенд и фронтенд части корпоративного сервиса микроблогов (аналог Twitter). Проект реализован с использованием **FastAPI** для API и **Nginx** для обслуживания фронтенда. Данные хранятся в базе данных **PostgreSQL**. Архитектура включает Docker-контейнеры для простого развертывания и управления.

Проект разделён на две части:
- **server** — бэкенд (API).
- **client** — фронтенд (сборка статических файлов).

## Содержание проекта

### 1. Корневая структура

- **client/** — фронтенд приложение, которое обслуживается через Nginx.
- **server/** — бэкенд приложение, работающее на FastAPI.
- **docker-compose.yml** — конфигурация для Docker Compose, объединяющая бэкенд, фронтенд и базу данных.
- **README.md** — этот файл, содержащий описание проекта и инструкции.
- **init_db.sh** — скрипт для инициализации базы данных PostgreSQL.

### 2. Client (Фронтенд)

Папка `client/` содержит готовую сборку фронтенда и конфигурации Nginx для работы с API и обслуживания статических файлов.

- **client/dist/** — здесь находятся собранные статические файлы фронтенда:
  - **css/** — папка со стилями фронтенда.
  - **js/** — папка с JavaScript кодом.
  - **index.html** — основная HTML страница приложения.
  - **favicon.ico** — иконка сайта.

- **client/nginx.conf** — конфигурационный файл для Nginx. В нем настроены правила для обслуживания статических файлов и проксирования запросов к API на бэкенд.

- **client/Dockerfile** — Dockerfile для создания контейнера с фронтендом на базе Nginx.

### 3. Server (Бэкенд)

Папка `server/` содержит код бэкенд-приложения, реализованного с использованием FastAPI. Оно обрабатывает запросы на создание твитов, загрузку медиафайлов, управление подписками и лайками.

- **server/api/** — содержит код API:
  - **server/api/main.py** — основной файл FastAPI с реализацией эндпоинтов для работы с твитами, медиа, лайками, подписками и фолловерами.
  
- **server/models/** — содержит описание моделей данных:
  - **server/models/tweet.py** — модель твита, включая поля для данных твита и медиафайлов.
  
- **server/db/** — папка для подключения и работы с базой данных PostgreSQL.

- **server/migrations/** — здесь расположены файлы миграций базы данных Alembic.

- **server/Dockerfile** — Dockerfile для создания контейнера с бэкендом на базе Python и FastAPI.

- **server/requirements.txt** — файл с зависимостями для Python-проектов. Содержит библиотеки, необходимые для работы бэкенда, такие как FastAPI, SQLAlchemy, и другие.

### 4. docker-compose.yml

Конфигурационный файл `docker-compose.yml` объединяет три сервиса:
1. **client** — фронтенд, который обслуживается через Nginx.
2. **server** — бэкенд с FastAPI.
3. **db** — база данных PostgreSQL.

#### Основные моменты:
- **client** и **server** подключены к общей сети `my_network`.
- **server** проксируется через Nginx для обработки запросов на API.
- **db** хранит данные пользователей, твитов, лайков, подписок и медиа.

### 5. Инструкция по запуску проекта

#### 1. Установка Docker и Docker Compose

Перед началом работы убедитесь, что Docker и Docker Compose установлены на вашей машине.

#### 2. Запуск проекта

1. Склонируйте проект.
   ```bash
   git clone https://gitlab.skillbox.ru/mark_poselenov/python_advanced_diploma
2. В корневой папке выполните команду для сборки и запуска контейнеров:
   ```bash
   docker-compose up -d
3. После успешного запуска:
   Фронтенд будет доступен по адресу: http://localhost:8080.
   API бэкенда доступно по адресу: http://localhost:5000.

#### 3. Инициализация базы данных
При первом запуске проект автоматически инициализирует базу данных PostgreSQL с помощью скрипта `init_db.sh`.
#### 4. Документация API
Документация к API доступна через интерфейс Swagger после запуска сервера:  
http://localhost:5000/docs
### 6. Запуск проекта
Необходимые библиотеки и инструменты:
- **FastAPI** — высокопроизводительный веб-фреймворк для Python.
- **PostgreSQL** — база данных для хранения данных пользователей и твитов.
- **Nginx** — веб-сервер для обслуживания фронтенда и проксирования запросов к API.

Статический анализ и тестирование:
- Все Python файлы проверены линтером и соответствуют рекомендациям по стилю кода.
- Приложение покрыто unit-тестами, которые проверяют ключевые функции API.
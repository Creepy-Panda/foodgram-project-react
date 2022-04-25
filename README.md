# Foodgram - продуктовый помощник
![example workflow](https://github.com/Creepy-Panda/foodgram-project-react/actions/workflows/main.yml/badge.svg)  

## Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
## Описание
"Продуктовый помощник": сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд. 

[Ссылка на проект](51.250.100.88)

## Системные требования
- Python 3.7+
- Docker

## Порядок локального запуска
Клонируйте репозиторий
```
git clone https://github.com/Creepy-Panda/foodgram-project-react.git
```
Переходим в папку infra и создаем файл .env в котором должно быть:
```
DB_ENGINE=django.db.backends.postgresq
DB_NAME=postgre
POSTGRES_PASSWORD=postgre
POSTGRES_USER=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=*
```
Запустить docker-compose
```
docker-compose up
```
Сделать миграции, создать супер-пользователя, собрать статику и сделать импорт игридиентов в базу данных
```
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py import_csv data/ingredients.csv
```
login - admin@admin.ru
password - admin
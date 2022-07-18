# Foodgram - продуктовый помощник
![example workflow](https://github.com/Creepy-Panda/foodgram-project-react/actions/workflows/main.yml/badge.svg)  

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
## Описание
"Продуктовый помощник": сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд. 


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

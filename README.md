[![Python 3.11](https://img.shields.io/badge/python-3.11-green.svg)](https://www.python.org/downloads/release/python-360/)
![Django 4.0](https://img.shields.io/badge/Django-5.0.2-green.svg)


# Меню ресторана
## 1. Описание проекта

#### Описание проекта
        Приложение для управления рестораном, предусматривает
        два вида пользователей: клиент, администратор ресторана.
        Клиент:
          - Просмотр меню
          - Просмотр корзины 
          - Добавление и удаление блюд в/из корзины
          - Добавление и удаление блюд в/из списка избранных
          - Написание отзывов о блюде

        Администратор:
          - Добавление, изменение и удаление категорий в меню
          - Добавление, изменение и удаление блюд (фотографии,
            описание, цены) 

        Регистрация, аутентифифкация:
          - Регистрация при помощи никнейма, почты, пароля + прохождение капчи
          - Аутентификация при помощи почты и пароля
          - Есть возможность восстановления пароля через почту, на нее придет 
            ссылка для сброса пароля
            
       - Добавлено кеширование с помощью django-cachalot
       - Отложенные задачи через celery + rabbitmq
        
## 2. Стек технологий
#### Frameworks
    - Django + DRF

#### SQL Database
    - PostgreSQL
    
#### NoSQL Database
    - Redis

#### Message Broker
    - RabbitMQ

#### Task Queues
    - Celery

#### Linters
    - Flake8
    - Black

## 3. Запуск проекта
#### Клонируйте репозиторий:
```
git clone https://github.com/TetherOne/project
```
#### Соберите docker-compose:
```
docker-compose build
```
#### Запустите docker-compose:
```
docker-compose up
```
#### Создайте superuser для создания блюд в меню
```
docker exec -it menu-wed-app-1 python manage.py createsuperuser
```
#### Перейдите в браузер по ссылке:
```
http://127.0.0.1:8000/api/v1/
```

# library API

Welcome to the library management application

This Django REST project provides a comprehensive API for managing a library system.  
It features a robust database storing information about books and clients.  
The core functionality revolves around a loan management system,  
enabling the tracking and administration of book borrowings.

---

## 🛠 Technologies

- Python 3.12
- Django 5.2.4
- Django REST Framework 3.16.0
- Telegram API
- PostgresQL
- Docker & Docker Compose
- Simple JWT 5.5.0 for authentication
- Spectacular documentation

---

## Features
- Creating & manage book and clients
- Borrowing books system
- Registration with email
- Telegram notifications
- Admin panel /admin/
- JWT authenticated
- Documentation is located at api/v1/doc/swagger/ or api/v1/doc/redoc/


## Installing using GitHub
This project use postgres db, so you need create it first  
Also you need create your telegram bot via @BotFather to generate a token  
You need it for fill in the file .env, there`s example - .env.sample

- git clone https://github.com/Komar88lvl/library.git
- cd library
- python3 -m venv venv | python -m venv venv (for windows)
- source venv/bin/activate | venv\Scripts\activate (for windows)
- pip install -r requirements.txt
- touch .env (fill in the .env file according to the .env.sample)
- python manage.py migrate
- python manage.py runserver  

After this steps service will be available at http://127.0.0.1:8000/  

you might create superuser
- python manage.py createsuperuser

Or create common user at http://127.0.0.1:8000/api/v1/user/register/

## Run with docker

docker should be installed  
your POSTGRES_HOST in .env file must be - db  
- docker-compose up --build  
service will be available at http://127.0.0.1:8001/


## Features of use

After getting access you can test swagger or redoc api documentation with your access token
- http://127.0.0.1:8000/api/v1/doc/swagger/
- http://127.0.0.1:8000/pi/v1/doc/redoc/

Also you can check if your token still available (it works for 3 hours) at:
- http://127.0.0.1:8000/api/v1/user/token/verify/

Refresh token, if it`s need (using a refresh token) at:
- http://127.0.0.1:8000/api/v1/user/token/refresh/

Check and update your account information at:

- http://127.0.0.1:8000/api/v1/user/me/
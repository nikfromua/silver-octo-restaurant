# Silver Octo Restaurant ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django?style=flat-square)

![restaurant_img](media/image-1.png)
## Опис
Silver Octo Restaurant - це внутрішня система для компаній, яка допомагає їхнім співробітникам приймати рішення щодо місця обіду. Ресторани можуть завантажувати меню на кожен день через API, а співробітники можуть голосувати за обране меню через мобільний додаток.

## Основні функції
- Аутентифікація
- Створення ресторану
- Завантаження меню для ресторану
- Створення співробітника
- Отримання меню поточного дня
- Отримання результатів голосування на поточний день

## Технічні вимоги
- **Backend**: Django + DRF, JWT, PostgreSQL
- **Інфраструктура**: Docker (з використанням docker-compose)
- **Тестування**: PyTests

## Встановлення та запуск

1. Клонуйте репозиторій:
```
git clone https://github.com/nikfromua/silver-octo-restaurant
```



2. Встановіть залежності:

```
pip install -r requirements.txt
```

3. Налаштування бази даних:

Вибір СУБД:
Django підтримує декілька систем управління базами даних (СУБД) "з коробки":

PostgreSQL
MySQL
SQLite
Oracle
Примітка: Переконайтеся, що ви встановили необхідні пакети для вашої СУБД. Наприклад, для PostgreSQL це psycopg2.

Оновіть settings.py:
У вашому файлі settings.py знаходиться розділ DATABASES. Ось приклад для PostgreSQL:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```



## Як запустити проект

1. Запустіть сервер:

```
python manage.py runserver
```

2. Відкрийте браузер та перейдіть на `http://127.0.0.1:8000/`.

## Використання API

Ось основні ендпойнти нашого API:

- `GET /api/items/`: отримання списку елементів.
- `POST /api/items/`: створення нового елемента.

**Приклад запиту**:
```
curl -X GET http://127.0.0.1:8000/api/items/
```
## Ліцензія

Цей проект розповсюджується під ліцензією MIT. Детальніше можна дізнатися в файлі [LICENSE](LICENSE).

## P.S.
Я новачок у Django, тож прошу вибачення за можливі неточності або недоліки у проекті. Я завжди відкритий до ваших підказок та порад, щоб робити свої проекти кращими. Дякую за розуміння!

<h1>EN Version</h1>

# Silver Octo Restaurant ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django?style=flat-square)

![restaurant_img](media/image-1.png)

## Description
Silver Octo Restaurant is an internal system for companies to help their employees decide where to have lunch. Restaurants can upload menus for each day via the API, and employees can vote for their chosen menu through a mobile app.

## Key Features
- Authentication
- Creation of a restaurant
- Uploading a menu for the restaurant
- Creation of an employee
- Retrieval of the day's menu
- Retrieval of voting results for the day

## Technical Requirements
- **Backend**: Django + DRF, JWT, PostgreSQL
- **Infrastructure**: Docker (using docker-compose)
- **Testing**: PyTests

## Installation and Setup

1. Clone the repository:
```
git clone https://github.com/nikfromua/silver-octo-restaurant
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Database Configuration:

DBMS Selection:
Django supports several out-of-the-box database management systems (DBMS):

- PostgreSQL
- MySQL
- SQLite
- Oracle

Note: Ensure you have installed the necessary packages for your DBMS. For example, for PostgreSQL, it's psycopg2.

Update `settings.py` 
In your `settings.py` file, there's a DATABASES section. Here's an example for PostgreSQL:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## How to Run the Project

1. Start the server:
```
python manage.py runserver
```

2. Open a browser and navigate to `http://127.0.0.1:8000/`.

## Using the API

Here are the main endpoints for our API:

- `GET /api/items/`: Retrieve a list of items.
- `POST /api/items/`: Create a new item.

**Example Request**:
```
curl -X GET http://127.0.0.1:8000/api/items/
```

## License

This project is distributed under the MIT license. More details can be found in the [LICENSE](LICENSE) file.

## P.S.
I'm a beginner with Django, so I apologize for any inaccuracies or deficiencies in the project. I'm always open to your suggestions and advice to make my projects better. Thank you for understanding!
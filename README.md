### Стек:
Python 3.11, Flask 2.3, SQLAlchemy 2.0, Flask-SQLAlchemy 3.0, SQLite | PostgreSQL, VK API


### Документация:
Примеры и параметры запросов, ответы и более подробная информация: http://127.0.0.1:5000/apidocs/
Доступна только во время запущенного сервера ```flask run```


### Возможности:
Используя VK API, позволяет осуществлять поиск групп (сообществ) по подстроке и (одновременно) в которые входит пользователь или его друзья.


### Как запустить проект:
Клонировать репозиторий:
```
git clone git@github.com:4kolesov/vk_user_groups.git
```

В командной строке перейти в директорию с проектом.

Cоздать и активировать виртуальное окружение:

```
python -3.11 -m venv env
```

```
source venv/Scripts/activate
```

Обновить менеджер пакетов "pip":

```
python -m pip install --upgrade pip

```
Установить зависимости из файла ```requirements.txt```:

```
pip install -r requirements.txt

```

В директории с файлом ```settings.py``` запустить проект

```
flask run
```


### Структура директорий и файлов:
```
vk_user_groups/
├── instance              ← БД SQLite3
├── migrations/           ← Миграции Alembic/
│   └── versions/         ← Версии миграций
├── vk_groups/            ← Flask app/
│   ├── __init__.py       ← пакет приложения Flask
│   ├── api_views.py      ← эндпоинты
│   ├── models.py         ← модель группы в БД
│   └── vk_services.py    ← vk api controllers
├── .ENV                  ← СОЗДАТЬ файл с переменными
├── .ENV.EXAMPLE          ← пример файла .ENV с описанием
├── requirements.txt      ← зависимости проекта
├── README.md             ← readme
└── settings.py           ← конфигурация приложения Flask
```

### PostgreSQL
Запустить PostgreSQL на локальной машине или в контейнере Docker.
Запустить утилиту psql для подключения и управления СУБД
```
psql -U postgres
```
Создать новую БД:
```
CREATE DATABASE vk_groups;
```

Создать пользователя и пароль для подключения к БД:
```
CREATE USER DigitalFutureSystems WITH ENCRYPTED PASSWORD 'OkLetsGo';
```

Выдать права на использование нужной БД нужным юзером:
```
GRANT ALL PRIVILEGES ON DATABASE vk_groups TO DigitalFutureSystems;
```

Не забыть добавить в .ENV файл конфигурацию для подключения к БД:

```
DATABASE_URI='postgresql://DigitalFutureSystems:OkLetsGo@localhost:5432/vk_groups'
```

### VK API
Необходимо получить Токен пользователя, подробнее:
https://dev.vk.com/api/access-token/getting-started
Полученный access token необходимо разместить в .ENV файле:
```
VK_TOKEN=vk1.a.2V9pzKkhavsCPqvevAKOj3VmO1ZhxPCHRwmt
```
Важно: токен имеет гораздо больше символов, чем указано в данном примере!

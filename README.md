### Стек:
Python 3.11, Flask 2.3, SQLAlchemy 2.0, Flask-SQLAlchemy 3.0, SQLite | PostgreSQL, VK API


### Документация:
http://127.0.0.1:5000/apidocs/
Доступна только во время запущенного сервера ```flask run```


### Возможности:
Используя VK API, позволяет осуществлять поиск групп (сообществ) по подстроке и (одновременно) в которые входит пользователь или его друзья.


### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:4kolesov/vk_user_groups.git
```

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
├── instance           ← БД SQLite3
├── migrations/        ← Миграции Alembic/
│   └── versions/      ← Версии миграций
├── vk_groups/         ← Flask app/
│   ├── __init__.py    ← не удалять =)
│   ├── api_views.py   ← эндпоинты
│   ├── models.py      ← модель группы в БД
│   └── vk_services.py ← vk api controllers
├── .ENV               ← СОЗДАТЬ файл с переменными
├── .ENV.EXAMPLE       ← пример файла .ENV с описанием
├── requirements.txt   ← зависимости проекта
├── README.md          ← readme
└── settings.py        ← конфигурация приложения Flask
```

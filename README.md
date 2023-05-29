### Стек:
Python 3.11, Flask 2.3, SQLAlchemy 2.0, Flask-SQLAlchemy 3.0, SQLite | PostgreSQL


### Документация:
http://127.0.0.1:5000/apidocs/

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

# API Yatube

### Описание проекта:

Yatube — это платформа для блогов. API предоставляет возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

### Как запустить проект:

Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Обновить PIP:

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```
python blogicum/manage.py migrate
```
Linux/macOS
```
python3 blogicum/manage.py migrate
```

Запустить проект:

Windows
```
python blogicum/manage.py runserver
```
Linux/macOS
```
python3 blogicum/manage.py runserver
```

### Примеры запросов:

По адресу  ```http://127.0.0.1:8000/redoc/``` доступна документация для API Yatube.
В документации описана, работа API. Там же можно увидеть примеры запросов.
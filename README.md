### Установка зависимостей
```bash
poetry shell
poetry install
```

### Запуск
```bash
wsgi --http :8001 --module my_server:hello
```

или

```bash
PORT=8002 gunicorn my_server:hello
```

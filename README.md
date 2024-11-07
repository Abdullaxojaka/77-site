```bash
pip install -r requirements.txt/development.txt
```

```bash
pre-commit install && pre-commit autoupdate
```
## 1. Create virtualenv and activate

```sh
python -m venv .venv
source .venv/bin/activate
```

## 3. Create superuser for Django Admin

```sh
python manage.py createsuperuser
```

## 4. Run django project

- Makemigrations

```sh
python manage.py makemigrations
```

- Migrations

```sh
python manage.py migrate
```

- Run server

```sh
python manage.py runserver
```

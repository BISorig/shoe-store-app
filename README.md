# Shoe Store App

Веб-приложение для компании по продаже обуви на **FastAPI + SQLAlchemy**.

## Что реализовано

- авторизация + роли пользователей;
- работа с товарами (просмотр, добавление, редактирование, удаление);
- работа с заказами (просмотр для менеджера/админа, CRUD для админа);
- загрузка изображений товаров;
- поиск, фильтрация, сортировка товаров (для менеджера/админа);
- UI страницы: логин, товары, заказы.

---

## Требования

- Python 3.11+ (рекомендуется);
- доступ к базе данных (указывается в `.env`).

---

## Быстрый старт

### 1) Клонировать репозиторий

```bash
git clone <repo_url>
cd shoe-store-app
```

### 2) Создать виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate
```

Для Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Установить зависимости

Если у вас есть свой lock/requirements файл — используйте его.  
Если нет, установите минимально необходимые пакеты:

```bash
pip install fastapi uvicorn sqlalchemy pydantic-settings python-jose passlib python-multipart jinja2
```

### 4) Создать файл `.env`

В корне проекта создайте `.env` со следующими переменными:

```env
APP_NAME=Shoe Store App
DEBUG=true
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=change_me
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

> Значения полей должны соответствовать вашей среде.  
> Имена переменных берутся из `app/core/config.py`.

### 5) Инициализировать таблицы в БД

```bash
python -c "from app.db.session import engine; from app.db.base import Base; import app.models; Base.metadata.create_all(bind=engine)"
```

### 6) Запустить приложение

```bash
uvicorn app.main:app --reload
```

После запуска откройте:

- `http://127.0.0.1:8000/` — редирект на страницу логина;
- `http://127.0.0.1:8000/login` — экран входа.

---

## Роли и доступ

- **Гость** — просмотр товаров без фильтрации и поиска;
- **Клиент** — просмотр товаров;
- **Менеджер** — просмотр + поиск/фильтрация/сортировка, просмотр заказов;
- **Администратор** — полный CRUD по товарам и заказам.

---

## Структура проекта (кратко)

- `app/main.py` — входная точка FastAPI;
- `app/routers/` — HTTP-роутеры;
- `app/services/` — бизнес-логика;
- `app/repositories/` — доступ к БД;
- `app/templates/` — HTML шаблоны;
- `app/static/` — JS/CSS/изображения.


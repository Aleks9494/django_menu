Запуск
pip install -r requirements.txt

Создать базу данных PostgreSQL
sudo -i -u postgres
psql
CREATE DATABASE menu_test

Затем применить миграции:
python3 manage.py makemigrations
python3 manage.py migrate

Создать пользователя
python3 manage.py createsuperuser

Затем создать в админ-панели меню для отображения.
Для добавления второго меню так же создать его в админ-панели,
и добавить в файле HTML 'django_menu/templates/django_menu/menu_list.html':
{% draw_menu 'имя созданного меню' %}
Запуск<br>
    - [X] pip install -r requirements.txt<br>
    - [X] Создать базу данных PostgreSQL<br>
    sudo -i -u postgres<br>
    psql<br>
    CREATE DATABASE menu_test<br>
    - [X] Затем применить миграции:<br>
    python3 manage.py makemigrations<br>
    python3 manage.py migrate<br>
    - [X] Создать пользователя<br>
    python3 manage.py createsuperuser<br>
    - [X] Затем создать в админ-панели меню для отображения.<br>
    Для добавления второго меню так же создать его в админ-панели,<br>
    и добавить в файле HTML 'django_menu/templates/django_menu/menu_list.html':<br>
    {% draw_menu 'имя созданного меню' %}<br>
    - [X] python3 manage.py runserver<br>
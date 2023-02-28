Запуск<br>
    - pip install -r requirements.txt<br>
    - Создать базу данных PostgreSQL<br>
        &emsp;-- sudo -i -u postgres<br>
        -- psql<br>
        -- CREATE DATABASE menu_test<br>
    - Затем применить миграции:<br>
        -- python3 manage.py makemigrations<br>
        -- python3 manage.py migrate<br>
    - Создать пользователя<br>
        python3 manage.py createsuperuser<br>
    - Затем создать в админ-панели меню для отображения.<br>
        Для добавления второго меню так же создать его в админ-панели,<br>
        и добавить в файле HTML 'django_menu/templates/django_menu/menu_list.html':<br>
        {% draw_menu 'имя созданного меню' %}<br>
    - python3 manage.py runserver<br>

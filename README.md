Запуск<br>
    &emsp;- pip install -r requirements.txt<br>
    &emsp;- Создать базу данных PostgreSQL<br>
        &emsp;&emsp;-- sudo -i -u postgres<br>
        &emsp;&emsp;-- psql<br>
        &emsp;&emsp;-- CREATE DATABASE menu_test<br>
    &emsp;- Затем применить миграции:<br>
        &emsp;&emsp;-- python3 manage.py makemigrations<br>
        &emsp;&emsp;-- python3 manage.py migrate<br>
    &emsp;- Создать пользователя<br>
        &emsp;&emsp;python3 manage.py createsuperuser<br>
    &emsp;- Затем создать в админ-панели меню для отображения.<br>
        &emsp;&emsp;Для добавления второго меню так же создать его в админ-панели,<br>
        &emsp;&emsp;и добавить в файле HTML 'django_menu/templates/django_menu/menu_list.html':<br>
        &emsp;&emsp;{% draw_menu 'имя созданного меню' %}<br>
    &emsp;- python3 manage.py runserver<br>

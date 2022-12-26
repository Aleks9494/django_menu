from django.shortcuts import render
from django.core.exceptions import *
from .models import Menu, MenuItem
import re
import os
from django.http import HttpResponse


def menu_list(request, menu_name=None):
    try:
        context = {
            'title': 'DJANGO-MENU',
        }
        if menu_name is not None:
            context['current_menu'] = menu_name
        else:
            context['current_menu'] = None

        return render(request, 'django_menu/menu_list.html', context)

    except Exception as e:
        print(e)
        return HttpResponse('Internal error')


def home(request):
    context = {
        'title': 'Home page'
    }
    return render(request, 'django_menu/base.html', context)

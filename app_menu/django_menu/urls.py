from django.urls import path, re_path
from django_menu import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('django_menu/', views.menu_list, name='menu_list'),
    re_path(r'^django_menu/?(?P<menu_name>[\w.-]+)/', views.menu_list, name='menu_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

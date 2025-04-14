from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_main_page, name='main_page'),
]
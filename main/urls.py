from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_main_page, name='main_page'),
    path('load-services/', views.load_services, name='load_services'),
    path('load-reviews/', views.load_reviews, name='load_reviews'),
]
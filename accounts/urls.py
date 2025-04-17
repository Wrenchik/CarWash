from django.urls import path
from . import views
from .views import register_view, CustomLoginView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

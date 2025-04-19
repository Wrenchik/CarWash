from django.urls import path
from .views import BookingCreateView, BookingSuccessView

urlpatterns = [
    path('', BookingCreateView.as_view(), name='booking_page'),
    path('success/', BookingSuccessView.as_view(), name='booking_success'),
]

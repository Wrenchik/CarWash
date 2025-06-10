from django.urls import path
from .views import CreateBookingView, AvailableSlotsView

urlpatterns = [
    path('available-slots/', AvailableSlotsView.as_view(), name='available_slots'),
    path('', CreateBookingView.as_view(), name='booking_page'),
]

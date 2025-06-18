from django.urls import path
from .views import BookingPageView, AvailableSlotsView, CreateBookingView

app_name = 'booking'

urlpatterns = [
    path('', BookingPageView.as_view(), name='booking_page'),
    path('available-slots/', AvailableSlotsView.as_view(), name='available_slots'),
    path('create/', CreateBookingView.as_view(), name='create_booking'),
]

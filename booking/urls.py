from django.urls import path
from .views import CreateBookingView, AvailableSlotsView, BookingPageView

urlpatterns = [
    path('', BookingPageView.as_view(), name='booking_page'),
    path('booking/create/', CreateBookingView.as_view(), name='create_booking'),
    path('available-slots/', AvailableSlotsView.as_view(), name='available_slots'),
]

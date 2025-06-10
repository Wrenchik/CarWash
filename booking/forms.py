from django import forms
from .models import Booking, Service

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'services', 'comment', 'payment_method']
        widgets = {
            'services': forms.CheckboxSelectMultiple(),
        }
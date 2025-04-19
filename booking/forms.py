from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        label='Дата (дд.мм.гггг)',
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(format='%d.%m.%Y')
    )
    time = forms.TimeField(
        label='Время (чч:мм)',
        input_formats=['%H:%M'],
        widget=forms.TimeInput(format='%H:%M')
    )

    class Meta:
        model = Booking
        fields = ['service', 'date', 'time', 'comment']

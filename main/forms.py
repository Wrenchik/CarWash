from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['car_model', 'text', 'img']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Напишите ваш отзыв'}),
            'car_model': forms.TextInput(attrs={'placeholder': 'Укажите модель автомобиля'}),
        }
from django.db import models
from django.contrib.auth import get_user_model
from main.models import Service

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.service.name} на {self.date} в {self.time}'

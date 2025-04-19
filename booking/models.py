from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('basic', 'Базовая мойка'),
        ('deluxe', 'Делюкс'),
        # …
    ]
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    date    = models.DateField()
    time    = models.TimeField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} — {self.get_service_display()} {self.date} {self.time}"

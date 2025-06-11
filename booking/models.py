from django.db import models
from accounts.models import CustomUser
from main.models import Service
from datetime import datetime, timedelta

class Booking(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Банковская карта'),
        ('online', 'СБП'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    date = models.DateField()
    start_time = models.TimeField()
    comment = models.TextField(blank=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cash')

    def calculate_end_time(self):
        total_duration = sum(service.duration for service in self.services.all())
        start_dt = datetime.combine(self.date, self.start_time)
        end_dt = start_dt + timedelta(minutes=total_duration)
        return end_dt.time()

    def __str__(self):
        return f"{self.user.username} — {self.date} {self.start_time}–{self.calculate_end_time()}"

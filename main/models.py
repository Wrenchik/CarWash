from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField('Имя', max_length=100)
    car_model = models.CharField('Модель авто', max_length=50, blank=True, null=True)
    text = models.TextField('Текст отзыва')
    date = models.DateTimeField('Дата', auto_now_add=True)
    img = models.ImageField('Фото', upload_to='reviews/', blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date']

    def __str__(self):
        return f'Отзыв от {self.name} ({self.date.date()})'
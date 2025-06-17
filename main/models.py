from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price_from = models.DecimalField("Цена от", max_digits=8, decimal_places=2, default=0)
    price_to = models.DecimalField("Цена до", max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Длительность в минутах")

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.CharField('Имя', max_length=100)
    car_model = models.CharField('Модель авто', max_length=50, null=True)
    text = models.TextField('Текст отзыва')
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    img = models.ImageField('Фото', upload_to='reviews_img/', blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Отзыв от {self.author} ({self.created_at.date()})'

    def save(self, *args, **kwargs):
        if self.img:
            user_id = self.id
            file_extension = os.path.splitext(self.img.name)[1]
            filename = f'{slugify(self.author)}_{user_id}{file_extension}'
            self.img.author = os.path.join('reviews', filename)
        super().save(*args, **kwargs)
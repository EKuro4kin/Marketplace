from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(verbose_name="название товара", max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(verbose_name="описание товара", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(verbose_name="дата создания объявления", auto_now_add=True)
    image = models.ImageField(upload_to='django_media/', null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(verbose_name="текст отзыва", max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(verbose_name="дата создания отзыва", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.text

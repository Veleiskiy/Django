from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)


    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse("news:blog_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural ="Новости"

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новости")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    text = models.TextField(verbose_name="Содержание комментария")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Дата Публикации")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
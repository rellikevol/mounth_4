from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    status = models.BooleanField(default=True, verbose_name="Статус публикации")
    cover = models.ImageField(upload_to='uploads/blog', blank=True, default='image.jpg',
                              verbose_name="Изображение")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.title} - {self.created}"


class Comment(models.Model):
    username = models.CharField(max_length=16, verbose_name="Имя ользователя")
    text = models.CharField(max_length=300, verbose_name="Текст комментария")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="post_comment")

    def __str__(self):
        return f'{self.username} - {self.post.title}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"






















from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(  # при добавлении записи ссылаться на group
        Group,                  # на что ссылаться
        on_delete=models.CASCADE,
        blank=True,       # сообщество не является обязательным полем
        null=True
    )

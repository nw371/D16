from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    # единственное поле: название категории. Поле должно быть уникальным
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    # автоматически добавляемая дата и время создания
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    # заголовок статьи/новости
    name = models.CharField(max_length=255, verbose_name='Название')
    # текст статьи/новости
    body = models.TextField(verbose_name='Tекст')
    # связь «один ко многим» с моделью Author
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    category = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

class PostCategory(models.Model):
    # связь «один ко многим» с моделью Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # связь «один ко многим» с моделью Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
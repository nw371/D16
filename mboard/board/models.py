from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    CATEGORIES = [
        ('tanks', 'Танки'),
        ('hills', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('gildmasters', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('smiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potionmasters', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    ]
    # связь «один ко одному» с моделью User
    author = models.OneToOneField(User, default=1, on_delete=models.CASCADE, verbose_name='Автор')
    # автоматически добавляемая дата и время создания
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    # заголовок статьи/новости
    name = models.CharField(max_length=255, verbose_name='Название')
    # текст статьи/новости
    body = models.TextField(verbose_name='Tекст')
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    category = models.CharField(max_length=255, choices=CATEGORIES, default='tanks', verbose_name='Категория')
    # поле для загрузки медиа
    upload = models.FileField(upload_to='uploads/', default='uploaded_file')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

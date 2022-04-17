from pyexpat import model
from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):

    name = models.CharField(max_length=70)
    articles = models.ManyToManyField(Article, related_name='tags', through='Tags')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tags(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='labels')
    tag = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='labels')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Промежуточная таблица'
        verbose_name_plural = 'Промежуточные таблицы'
        ordering = ['tag']

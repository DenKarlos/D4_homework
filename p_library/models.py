from tabnanny import verbose
from django.db import models

class Author(models.Model):
    full_name = models.TextField(verbose_name='Имя')
    birth_year = models.SmallIntegerField(verbose_name='Год рождения')
    country = models.CharField(max_length=2, verbose_name='Страна рождения')
    
    
    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'
        ordering = ['full_name']
    
    def __str__(self):
        return self.full_name
    
    
class  Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    year_release = models.SmallIntegerField(verbose_name='Год выпуска')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    copy_count = models.SmallIntegerField(default=1, verbose_name='Количество копий')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=None, verbose_name='Цена')
    publisher = models.ForeignKey('Publisher', null=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['publisher']


class Publisher(models.Model):
    name = models.CharField(max_length=32, db_index=True, verbose_name='Название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Издательства'
        verbose_name = 'Издательство'
        ordering = ['name']
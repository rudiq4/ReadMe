from django.db import models


class Author(models.Model):
    name = models.CharField('Імя і прізвище автора', max_length=64)
    image = models.ImageField('Фотографія', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'


class Genre(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'


class Book(models.Model):
    title = models.CharField('Назва', max_length=128)
    tagline = models.CharField('Слоган', max_length=128, blank=True)
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, verbose_name='Автори')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

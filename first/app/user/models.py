from django.contrib import admin
from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.ManyToManyField(
        'Author',
        related_name='books',
        verbose_name='Авторы'
    )
    description = models.TextField(verbose_name='Описание книги', null=True, blank=True)
    id_publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        related_name='publishinghouse_books',
        verbose_name='ID издательство',
        null=True,
        blank=True
    )

    date_creation = models.DateField(verbose_name='Дата написания книги', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')
    book_img = models.ImageField(
        upload_to='media/%Y/%m/%d/',
        verbose_name="Ссылка на изображение",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class PublishingHouse(models.Model):
    publishing_house_name = models.CharField(max_length=300, verbose_name='Название издательства')
    adress = models.CharField(max_length=1500, verbose_name='Адрес компании')
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефон')
    email = models.EmailField(verbose_name='Email')
    website_linck = models.URLField(verbose_name='Ссылка на сайт', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.publishing_house_name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия автора')
    father_name = models.CharField(max_length=100, verbose_name='Отчество автора', null=True, blank=True)
    country = models.CharField(max_length=200, verbose_name='Страна')
    birthday = models.DateField(verbose_name='Дата рождения')
    languages = models.JSONField(verbose_name='Языки на которых писал автор', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class BooksInAuthor(admin.TabularInline):
    model = Books.author.through


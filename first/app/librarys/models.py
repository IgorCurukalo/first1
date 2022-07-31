from django.contrib import admin
from django.db import models

#Библиотеки
class Librarys(models.Model):

    librarys_name = models.CharField(max_length=100, verbose_name='Название библиотеки')
    librarys_address = models.CharField(max_length=200, verbose_name='Адрес библиотеки')
    librarian = models.ManyToManyField(
        'Librarian',
        related_name='librarys'
    )

    description = models.TextField(verbose_name='Описание библиотеки', null=True, blank=True)
    id_librarys_storage = models.ForeignKey(
        'LibrarysStorage',
        on_delete=models.CASCADE,
        related_name='librarysstorage_librarys',
        verbose_name='Хранилище библиотеки',
        null=True,
        blank=True
    )

    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')
    library_img = models.ImageField(
        upload_to='media/%Y/%m/%d/',
        verbose_name="Ссылка на изображение",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.librarys_name

    class Meta:

        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'

#Хранилище библиотеки - адрес и т.д.
class LibrarysStorage(models.Model):

    librarys_storage_address = models.CharField(max_length=1500, verbose_name='Адрес хранилища библиотеки')
    date_creation = models.DateField(verbose_name='Дата отрытия библиотеки', null=True, blank=True)
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    website_linck = models.URLField(verbose_name='Ссылка на сайт', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.librarys_storage_address

    class Meta:

        verbose_name = 'Хранилище'
        verbose_name_plural = 'Хранилища'

#Библиотекари
class Librarian(models.Model):

    first_name = models.CharField(max_length=100, verbose_name='Имя библиотекаря')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия библиотекаря')
    father_name = models.CharField(max_length=100, verbose_name='Отчество библиотекаря', null=True, blank=True)
    date_creation = models.DateField(verbose_name='Дата устройства на работу библиотекаря', null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения библиотекаря')
    home_address = models.CharField(max_length=1500, verbose_name='Домашний адрес библиотекаря')
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.last_name

    class Meta:

        verbose_name = 'Библиотекарь'
        verbose_name_plural = 'Библиотекари'


class LibrarysInLibrarian(admin.TabularInline):

    model = Librarys.librarian.through
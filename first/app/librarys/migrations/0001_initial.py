# Generated by Django 4.0.5 on 2022-06-30 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя директора')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия директора')),
                ('fathername', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество директора')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'Директор',
                'verbose_name_plural': 'Директора',
            },
        ),
        migrations.CreateModel(
            name='LibrarysCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarys_city_name', models.CharField(max_length=300, verbose_name='Название города')),
                ('adress', models.CharField(max_length=1500, verbose_name='Адрес библиотеки')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='Номер телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('website_linck', models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Librarys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarys_name', models.CharField(max_length=100, verbose_name='Название библиотеки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание библиотеки')),
                ('date_creation', models.DateField(blank=True, null=True, verbose_name='Дата создания библиотеки')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('director', models.ManyToManyField(related_name='librarys', to='librarys.director')),
                ('id_librarys_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libraryscity_librarys', to='librarys.libraryscity', verbose_name='ID библиотеки')),
            ],
            options={
                'verbose_name': 'Библиотека',
                'verbose_name_plural': 'Библиотеки',
            },
        ),
    ]

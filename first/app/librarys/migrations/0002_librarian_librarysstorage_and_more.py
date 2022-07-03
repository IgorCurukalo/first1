# Generated by Django 4.0.5 on 2022-07-03 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('librarys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя библиотекаря')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия библиотекаря')),
                ('father_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество библиотекаря')),
                ('date_creation', models.DateField(blank=True, null=True, verbose_name='Дата устройства на работу библиотекаря')),
                ('birthday', models.DateField(verbose_name='Дата рождения библиотекаря')),
                ('home_address', models.CharField(max_length=1500, verbose_name='Домашний адрес библиотекаря')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'Библиотекарь',
                'verbose_name_plural': 'Библиотекари',
            },
        ),
        migrations.CreateModel(
            name='LibrarysStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarys_storage_address', models.CharField(max_length=1500, verbose_name='Адрес хранилища библиотеки')),
                ('date_creation', models.DateField(blank=True, null=True, verbose_name='Дата отрытия библиотеки')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('website_linck', models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'Хранилище',
                'verbose_name_plural': 'Хранилища',
            },
        ),
        migrations.RemoveField(
            model_name='librarys',
            name='date_creation',
        ),
        migrations.RemoveField(
            model_name='librarys',
            name='director',
        ),
        migrations.RemoveField(
            model_name='librarys',
            name='id_librarys_city',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='LibrarysCity',
        ),
        migrations.AddField(
            model_name='librarys',
            name='id_librarys_storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='librarysstorage_librarys', to='librarys.librarysstorage', verbose_name='ID библиотеки'),
        ),
        migrations.AddField(
            model_name='librarys',
            name='librarian',
            field=models.ManyToManyField(related_name='librarys', to='librarys.librarian'),
        ),
    ]

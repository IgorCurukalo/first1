# Generated by Django 4.0.5 on 2022-07-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarys', '0002_librarian_librarysstorage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarys',
            name='library_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/', verbose_name='Ссылка на изображение'),
        ),
    ]

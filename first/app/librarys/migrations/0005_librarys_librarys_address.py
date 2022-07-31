# Generated by Django 4.0.6 on 2022-07-31 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('librarys', '0004_alter_librarys_id_librarys_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarys',
            name='librarys_address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Адрес библиотеки'),
            preserve_default=False,
        ),
    ]

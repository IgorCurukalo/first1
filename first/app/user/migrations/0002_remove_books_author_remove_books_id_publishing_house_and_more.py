# Generated by Django 4.0.6 on 2022-07-24 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.RemoveField(
            model_name='books',
            name='id_publishing_house',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='PublishingHouse',
        ),
    ]

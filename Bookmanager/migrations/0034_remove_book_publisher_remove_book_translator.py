# Generated by Django 5.1.4 on 2025-01-09 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmanager', '0033_book_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='book',
            name='translator',
        ),
    ]

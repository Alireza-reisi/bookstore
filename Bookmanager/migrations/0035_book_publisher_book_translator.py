# Generated by Django 5.1.4 on 2025-01-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmanager', '0034_remove_book_publisher_remove_book_translator'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.CharField(max_length=100, null=True, verbose_name='مترجم'),
        ),
    ]
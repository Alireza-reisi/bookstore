# Generated by Django 5.1.4 on 2025-01-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmanager', '0037_alter_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
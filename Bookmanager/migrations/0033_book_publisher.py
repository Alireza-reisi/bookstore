# Generated by Django 5.1.4 on 2025-01-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmanager', '0032_book_translator'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
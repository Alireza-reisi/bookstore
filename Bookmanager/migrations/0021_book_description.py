# Generated by Django 5.1.4 on 2025-01-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmanager', '0020_book_english_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

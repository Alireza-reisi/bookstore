# Generated by Django 5.1.4 on 2025-01-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmanager', '0023_alter_book_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='english_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

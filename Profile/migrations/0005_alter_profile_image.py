# Generated by Django 5.1.4 on 2025-01-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='assets/img/default-profile.webp', upload_to='profile_pics'),
        ),
    ]

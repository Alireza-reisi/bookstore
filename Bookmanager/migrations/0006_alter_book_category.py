# Generated by Django 5.1.4 on 2025-01-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmanager', '0005_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('EDU', 'Educational'), ('HIS', 'Historical'), ('SPO', 'Sports'), ('POL', 'Political'), ('PSY', 'Psychology'), ('MED', 'Medical'), ('MUS', 'Music'), ('REL', 'Religious'), ('FIC', 'Fiction'), ('KID', 'Kids'), ('ART', 'Art'), ('SCI', 'Science')], default='NF', max_length=3),
        ),
    ]

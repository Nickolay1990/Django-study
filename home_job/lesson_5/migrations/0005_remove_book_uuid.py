# Generated by Django 4.1.7 on 2023-02-25 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0004_remove_book_date1_remove_book_date2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='uuid',
        ),
    ]

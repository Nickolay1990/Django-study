# Generated by Django 4.1.7 on 2023-02-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0014_alter_book_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='test',
            field=models.CharField(default='null', max_length=43, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-12 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_3E', '0003_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('sell', models.IntegerField()),
                ('disc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson_3E.games')),
            ],
        ),
    ]

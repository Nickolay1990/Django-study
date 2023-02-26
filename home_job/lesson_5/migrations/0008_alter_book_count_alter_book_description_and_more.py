# Generated by Django 4.1.7 on 2023-02-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0007_remove_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='ip',
            field=models.GenericIPAddressField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='on_shop',
            field=models.BooleanField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='site',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.FloatField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='wrape',
            name='color',
            field=models.ManyToManyField(default='', null=True, to='lesson_5.book', verbose_name='this wrape has the same color of this books'),
        ),
        migrations.AlterField(
            model_name='wrape',
            name='name',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='wrape',
            name='price',
            field=models.FloatField(default='', null=True),
        ),
    ]

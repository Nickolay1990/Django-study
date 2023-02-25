# Generated by Django 4.1.7 on 2023-02-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0002_wrape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='date1',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='date2',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='date3',
            field=models.DurationField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='ip',
            field=models.GenericIPAddressField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='on_shop',
            field=models.BooleanField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='site',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='uuid',
            field=models.UUIDField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='wrape',
            name='color',
            field=models.ManyToManyField(default='', to='lesson_5.book', verbose_name='this wrape has the same color of this books'),
        ),
        migrations.AlterField(
            model_name='wrape',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='wrape',
            name='price',
            field=models.FloatField(default=''),
        ),
    ]

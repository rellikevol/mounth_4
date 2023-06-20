# Generated by Django 4.2.2 on 2023-06-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default='image.jpg', upload_to='uploads/blog', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]

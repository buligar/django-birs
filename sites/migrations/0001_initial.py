# Generated by Django 4.0.6 on 2023-01-07 21:22

from django.db import migrations, models
import sites.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('data', models.DateTimeField(verbose_name='Дата публикации')),
                ('cover', models.ImageField(upload_to=sites.models.user_directory_path)),
                ('url', models.URLField(max_length=500, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('book', models.FileField(upload_to='books/')),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-12-08 22:37

from django.db import migrations, models
import melanomas.models


class Migration(migrations.Migration):

    dependencies = [
        ('melanomas', '0002_alter_articles_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='cover',
            field=models.ImageField(upload_to=melanomas.models.user_directory_path),
        ),
    ]
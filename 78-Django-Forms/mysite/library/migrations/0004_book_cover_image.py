# Generated by Django 4.1.4 on 2023-01-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_author_description_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='covers', verbose_name='Cover image'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-02-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_bookreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='content',
            field=models.TextField(max_length=2000, verbose_name='Review'),
        ),
    ]
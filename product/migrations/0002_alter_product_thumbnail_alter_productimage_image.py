# Generated by Django 4.2.2 on 2023-11-17 23:06

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=''),
        ),
    ]